# Python program for face 
# comparision 


from __future__ import print_function, unicode_literals 
from facepplib import FacePP, exceptions 
#from urllib.parse import urljoin
#from urllib.request import pathname2url
#import emoji 
import cv2
import os
from PIL import Image as PImage

# define global variables 
face_detection = "" 
faceset_initialize = "" 
face_search = "" 
face_landmarks = "" 
dense_facial_landmarks = "" 
face_attributes = "" 
beauty_score_and_emotion_recognition = "" 


# define face comparing function 
def face_comparing(app): 
	
	print() 
	print('-'*30) 
	print('Comparing Photographs......') 
	print('-'*30) 
	
	#load images
	'''inPath ="/home/pi/Desktop/face/"
	images=[]
	x=0
	for imagePath in os.listdir(inPath): 
		# imagePath contains name of the image 
		inputPath = os.path.join(inPath, imagePath) 
		images.insert(x,inputPath)
		x=x+1
	'''	
	#image1=cv2.imread("file:///home/pi/Desktop/face/harish1.jpg")
	#image2=cv2.imread("file:///home/pi/Desktop/face/harish1.jpg")
	#image1='http://192.168.0.104:5000/meow/static/image/face/harish1.jpg'
	#image2='http://192.168.0.104:5000/meow/static/image/face/harish2.jpg'
	
	image1='https://smarteye-sgsits.000webhostapp.com/images/harish11.jpg'
	image2='https://smarteye-sgsits.000webhostapp.com/images/image1.jpg'
	#local drive image url.... 
	#image1 = 'https://i.postimg.cc/50TLX65v/harish1.jpg'
	#image2 = 'https://i.postimg.cc/sx5Q1Kgd/harish2.jpg'	
	#image3= 'ht0tps://i.postimg.cc/L5Q7YkCD/yash.jpg'
	#website link
	
	cmp_ = app.compare.get(image_url1 = image1, 
						image_url2 = image2) 

	print('Photo1', '=', cmp_.image1) 
	print('Photo2', '=', cmp_.image2) 

	# Comparing Photos 
	if cmp_.confidence > 70: 
		print('Both photographs are of same person......')
		#
		#return "compare" 
		#
	else: 
		print('Both photographs are of two different persons......') 
		#
		#return "not compare"
		#
# Driver Code 
if __name__ == '__main__': 

	# api details 
	api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
	api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

	try: 

		# create a logo of app by using iteration, 
		# unicode and emoji module------------- 
		# call api 
		app_ = FacePP(api_key = api_key, 
					api_secret = api_secret) 
		funcs = [ 
			face_detection, 
			#face_comparing_localphoto, 
			#face_comparing_websitephoto, 
			faceset_initialize, 
			face_search, 
			face_landmarks, 
			dense_facial_landmarks, 
			face_attributes, 
			beauty_score_and_emotion_recognition 
		] 
		face_comparing(app_)
		
		
	except exceptions.BaseFacePPError as e: 
		print('Error:', e) 

