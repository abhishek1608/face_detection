# import the necessary packages
import cv2
import glob
 
# load the image and show it

for infile in glob.glob("/Users/abhishekgupta/Documents/custom_dataset/dataset/katrina/**/*.jpg", recursive=True):
	image = cv2.imread(infile)
	print(image.shape)
	r = 100.0 / image.shape[1]
	dim = (100, int(image.shape[0] * r))
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	cv2.imwrite(infile,resized)


