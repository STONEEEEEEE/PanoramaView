from pylab import *
from numpy import *
from PIL import Image

# If you have PCV installed, these imports should work
from PCV.geometry import homography, warp
from PCV.localdescriptors import sift
import os

"""
This is the panorama example from section 3.3.
"""

tempPath = ['竹轩b', '操场', '东北门外', '东北门内', '静湖', '静湖水体广场', '体育馆', '丸美学生活动中心', '休闲健身步道', '中山图书馆']
numA = 9
numB = 1

featname = ['..\\data\\sift\\'+ tempPath[numA] + '\\' + str(numB) + '-' + str(i+1)+'.sift' for i in range(5)]
imname = ['..\\data\\srcfile\\'+ tempPath[numA] + '\\' + str(numB) + '-' + str(i+1)+'.jpg' for i in range(5)]

# extract features and match
l = {}
d = {}
for i in range(5):
    sift.process_image(imname[i],featname[i])
    l[i],d[i] = sift.read_features_from_file(featname[i])

matches = {}
for i in range(4):
    matches[i] = sift.match(d[i+1],d[i])

# visualize the matches (Figure 3-11 in the book)
for i in range(4):
    im1 = array(Image.open(imname[i]))
    im2 = array(Image.open(imname[i+1]))
    figure()
    imMatch = sift.plot_matches(im2, im1, l[i + 1], l[i], matches[i], show_below=True)
    imMatchPath = '..\\data\\outfile\\' + tempPath[numA] + '\\match' + str(numB) + '-' + str(i) + '.jpg'
    savefig(imMatchPath)



# function to convert the matches to hom. points
def convert_points(j):
    ndx = matches[j].nonzero()[0]
    fp = homography.make_homog(l[j+1][ndx,:2].T)
    ndx2 = [int(matches[j][i]) for i in ndx]
    tp = homography.make_homog(l[j][ndx2,:2].T)

    # switch x and y - TODO this should move elsewhere
    fp = vstack([fp[1],fp[0],fp[2]])
    tp = vstack([tp[1],tp[0],tp[2]])
    return fp,tp


# estimate the homographies
model = homography.RansacModel()

fp,tp = convert_points(1)
H_12 = homography.H_from_ransac(fp,tp,model)[0] #im 1 to 2

fp,tp = convert_points(0)
H_01 = homography.H_from_ransac(fp,tp,model)[0] #im 0 to 1

tp,fp = convert_points(2) #NB: reverse order
H_32 = homography.H_from_ransac(fp,tp,model)[0] #im 3 to 2

tp,fp = convert_points(3) #NB: reverse order
H_43 = homography.H_from_ransac(fp,tp,model)[0] #im 4 to 3


# warp the images
delta = 2000 # for padding and translation

im1 = array(Image.open(imname[1]), "uint8")
im2 = array(Image.open(imname[2]), "uint8")
im_12 = warp.panorama(H_12,im1,im2,delta,delta)

im1 = array(Image.open(imname[0]), "f")
im_02 = warp.panorama(dot(H_12,H_01),im1,im_12,delta,delta)

im1 = array(Image.open(imname[3]), "f")
im_32 = warp.panorama(H_32,im1,im_02,delta,delta)

im1 = array(Image.open(imname[4]), "f")
im_42 = warp.panorama(dot(H_32,H_43),im1,im_32,delta,2*delta)


figure()
imshow(array(im_42, "uint8"))
axis('off')
outfile = '..\\data\\outfile\\' + tempPath[numA] + '\\' + tempPath[numA] + str(numB) + '.jpg'
imsave(outfile, array(im_42, "uint8"))
# show()

