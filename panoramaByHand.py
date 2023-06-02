import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

MIN = 10
starttime = time.time()
img1 = cv2.imread('data\\caochangA\\1-10.png')  # query
img2 = cv2.imread('data\\caochangA\\1-11.png')  # train

# img1gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
# img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# 创建surf对象
surf = cv2.xfeatures2d.SURF_create(10000, nOctaves=4, extended=False, upright=True)

# 获取特征点的位置和特征向量
kp1, descrip1 = surf.detectAndCompute(img1, None)
kp2, descrip2 = surf.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
searchParams = dict(checks=50)
# 快速匹配器
flann = cv2.FlannBasedMatcher(indexParams, searchParams)
match = flann.knnMatch(descrip1, descrip2, k=2)
# 过滤掉一些异常的特征点
good = []
for i, (m, n) in enumerate(match):
    if (m.distance < 0.75 * n.distance):
        good.append(m)
# 匹配到的特征点要大于MIN
if len(good) > MIN:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    ano_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    # 计算单应性矩阵
    M, mask = cv2.findHomography(src_pts, ano_pts, cv2.RANSAC, 5.0)
    # 透视变换
    warpImg = cv2.warpPerspective(img2, np.linalg.inv(M), (img1.shape[1] + img2.shape[1], img2.shape[0]))
    # 拼接
    direct = warpImg.copy()
    direct[0:img1.shape[0], 0:img1.shape[1]] = img1
    simple = time.time()

    cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    cv2.imshow("Result",warpImg)
    cv2.imwrite('data\\caochangA\\10to11_warp.png', warpImg)
    rows, cols = img1.shape[:2]

    for col in range(0, cols):
        if img1[:, col].any() and warpImg[:, col].any():  # 开始重叠的最左端
            left = col
            break
    for col in range(cols - 1, 0, -1):
        if img1[:, col].any() and warpImg[:, col].any():  # 重叠的最右一列
            right = col
            break

    res = np.zeros([rows, cols, 3], np.uint8)
    for row in range(0, rows):
        for col in range(0, cols):
            if not img1[row, col].any():  # 如果没有原图，用旋转的填充
                res[row, col] = warpImg[row, col]
            elif not warpImg[row, col].any():
                res[row, col] = img1[row, col]
            else:
                srcImgLen = float(abs(col - left))
                testImgLen = float(abs(col - right))
                alpha = srcImgLen / (srcImgLen + testImgLen)
                res[row, col] = np.clip(img1[row, col] * (1 - alpha) + warpImg[row, col] * alpha, 0, 255)

    warpImg[0:img1.shape[0], 0:img1.shape[1]] = res
    final = time.time()
    img3 = cv2.cvtColor(direct, cv2.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(img3)
    img4 = cv2.cvtColor(warpImg, cv2.COLOR_BGR2RGB)
    plt.figure()
    plt.imshow(img4)
    plt.axis('off')
    plt.show()
    print("拼接用时 %f" % (simple - starttime))
    print("\n消除拼缝用时 %f" % (final - starttime))
    cv2.imwrite("data\\操场A\\10to11_source.png", direct)
    cv2.imwrite("data\\操场A\\10to11_best.png", warpImg)

else:
    print("特征点不足以匹配!")
