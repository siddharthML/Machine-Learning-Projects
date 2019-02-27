# Check Video 17 on Sentdex OpenCV playlist https://www.youtube.com/playlist?list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq for details.

"""
Code is in Linux so only going over some notes here:

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
- Done with OpenCV command.

Negative and Positive images need description files:

Negative images:
Generally a bg.txt file that contains the path to each
image, by line.
Example line:
neg/1.jpg

Positive images:
somtimes called "info" pos.txt or something of this
sort. Contains path to each image, by line along with
how many objects and where they located.

Example line:
post/1.jpg 1 00 50 50 > image, num objects, start point,
rectangle cooredinates.

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

"""
