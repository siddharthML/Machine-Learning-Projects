# Computer Vision

This repository contains code from OpenCV tutorial by [Sentdex](https://pythonprogramming.net/loading-images-python-opencv-tutorial/)

A youtube playlist for this tutorial exists [here.](https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)

OpenCV is an excellent library for programming functions related to real-time computer vision.

My aim through this tutorial was to understand the range of applicability of OpenCV library and to implement a Haar Cascade that would be able to recognize objects on the road for the self-driving car project. 

## Installation Guide:

```

pip3 install numpy or apt-get install python3-numpy. 

pip3 install matplotlib or apt-get install python3-matplotlib.

apt-get install python3-OpenCV
```

You may need to apt-get install python3-pip.

Matplotlib is an optional choice for displaying frames from video or images. Only couple of examples in this repository have it. Numpy is used for all things "numbers and Python." 

## Haar Cascades:

Steps to creating your own Haar Cascade:
1) Collect "Negative" or "background" images
- Any image will do, just make sure your object is not present
in them.
2) Collect or create "positive" images.
- Thousands of images of your object. Can make these
based on one image, or manually create them. (Ideally
double the amount of positive to negative images)
3) Create a positive vector file by stitching together
all positives.
- This is done with an OpenCV command.

4) Train cascade.

- Done with OpenCV command. (Uses adaboost)

Negative and Positive images need description files:

Negative images:
Generally a bg.txt file that contains the path to each
image, by line.

Positive images:
somtimes called "info" pos.txt or something of this
sort. Contains path to each image, by line along with
how many objects and where they located.

We are manually saying where the image is located which
is a real pain.

You want dimension of negative images larger than positive
images generally, if you are going to "create samples"
rather than collect and label positives.

Try to use small images. 100x100 for negatives, 50x50 for
positives. Will get even smaller when it comes to training.
You will superimpose the positive images on the negative image
backgrounds so ultimately the image size will be the same.

Have ~ double the positive images compare to negative for training.

(For more detailed look see [Quora.](https://www.quora.com/How-do-Haar-cascades-work))
