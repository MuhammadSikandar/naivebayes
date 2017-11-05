#__author__ udicity

import warnings
warnings.filterwarnings("ignore")

import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import matplotlib.image as mpimg
#import Image
#########################################
#x = np.arange(-5, 5, 1)
#y = np.arange(-5, 5, 1)
#xx, yy = np.meshgrid(x, y, sparse=True)
#plt.plot(xx,yy, marker = '.', color = 'k')
#z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)

#h = plt.contourf(x,y,z)

#plt.interactive(False)
#xvalues = np.array([0, 1, 2, 3, 4]);
#yvalues = np.array([0, 1, 2, 3, 4]);
#xx, yy = np.meshgrid(xvalues, yvalues)

#plt.plot(xx, yy, marker='.', color='k', linestyle='none')
#plt.savefig("test.png")

#plt.imshow(mpimg.imread('test.png'))
#plt.show(block=True)
#plt.imshow('test.png')
#plt.show()  # display it


#img=mpimg.imread('test.png')
#imgplot = plt.imshow(img)
#plt.show()

#image = Image.open('test.png')
#image.show()

#points = np.arange(-5, 5, 0.01)
#dx, dy = np.meshgrid(points, points)
#z = (np.sin(dx)+np.sin(dy))
#plt.imshow(z)
#plt.colorbar()
#plt.title('plot for sin(x)+sin(y)')
#plt.show()
########################################
def prettyPicture(clf, X_test, y_test):

    x_min = 0.0; x_max = 1.0
    y_min = 0.0; y_max = 1.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = .01  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    #vrb =np.c_[xx.ravel(), yy.ravel()]
    #print(vrb)
    #print(vrb.shape)
    #vrb
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)
    plt.savefig("test1.png")

    # Plot also the test points
    grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 1]
    bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 1]

    plt.scatter(grade_sig, bumpy_sig, color="b", label="fast")
    plt.scatter(grade_bkg, bumpy_bkg, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")

    plt.savefig("test.png")


import base64
import json
import subprocess

def output_image(name, format, bytes):
    image_start =  "BEGIN_IMAGE_f9825uweof8jw9fj4r8"
    image_end = "END_IMAGE_0238jfw08fjsiufhw8frs"
    data = {}
    data['name'] = name
    data['format'] = format
    data['bytes'] = base64.encodestring(bytes)
    print image_start + json.dumps(data) + image_end