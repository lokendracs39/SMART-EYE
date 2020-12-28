from __future__ import print_function, unicode_literals 
from facepplib import FacePP, exceptions 
import base64
import cv2
import os
from PIL import Image as PImage
#
from ftplib import FTP



#####IMPLEMENTING ARRIVE SON FUNCTIONALITY##########
import datetime
import calendar
import time

##############import some date fucn####################




#from PIL import Image
#
#
# define global variables 
face_detection = "" 
faceset_initialize = "" 
face_search = "" 
face_landmarks = "" 
dense_facial_landmarks = "" 
face_attributes = "" 
beauty_score_and_emotion_recognition = "" 
#####
api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

		# create a logo of app by using iteration, 
		# unicode and emoji module------------- 
		# call api 
app_ = FacePP(api_key = api_key,api_secret = api_secret) 
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

	
# define transfer function for transfer images to ftp server
def transfer(frame):
		dir_list=[]
		try:
			
			print("...enter into file transfer mode.....")
			ftp=FTP('files.000webhost.com',timeout=120)
			ftp.login(user='smarteye-sgsits',passwd='Root@1234')
			ftp.cwd("/public_html/images/")
			ftp.dir()
			ftp.retrlines('NLST',dir_list.append)
			print(dir_list)
	
		
			with open("a.jpg", "wb") as img:
				img.write(frame)
				local=open('/home/pi/Downloads/SmartEye/a.jpg','rb')
				ftp.storbinary('STOR a.jpg',local)
			print("check")
			flag,c=face_comparing(app_,dir_list)#yhaa detec ho rhi error
			
			
			ftp.delete("a.jpg")
			#ftp.close()
				
			if c==True:
				return flag,True
			else:
				return False,False
			ftp.close()
		except:
			#print("error in comp_trans file")
			print("Oops!",sys.exc_info()[0],"occured.")

			


# define face comparing function 
def face_comparing(app_,dir_list): 
	
	print() 
	print('-'*30) 
	print('Comparing Photographs......') 
	print('-'*30) 
	#
	img='https://smarteye-sgsits.000webhostapp.com/images/'
	i=3
	#######################ADDED TIME FUNCTION##########################
	
	now = datetime.datetime.now()

	my_time_string = "21:00:00" # leap second
	my_time_string = now.strftime("%Y-%m-%d") + " " + my_time_string # I am supposing the date must be the same as now

	my_time = time.strptime(my_time_string, "%Y-%m-%d %H:%M:%S")

	my_datetime = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=calendar.timegm(my_time))
	print(now)#this line can comment
	print(my_datetime)#this line can be comment
	if (now < my_datetime):
		
		###added just to compare specific family member#####
		#image1A='https://smarteye-sgsits.000webhostapp.com/Specific_FamilyMember/lokendr.jpg'
		image1A='https://smarteye-sgsits.000webhostapp.com/Specific_FamilyMember/fam1 (1).jpg'
		image2A='https://smarteye-sgsits.000webhostapp.com/images/a.jpg'
		cmp_ = app_.compare.get(image_url1 = image1A,image_url2 = image2A) 
		 
		if cmp_.confidence > 70: 
			
			#check(1)
			print('Both photographs are of the same person......')
		
			return True,True 
			
		else:
			pass 
	###################################end##################
	
	
	
	
	while(i<len(dir_list)):#check
		image1=img +''.join(dir_list[i])
		print(image1)
		#image stores 
		image2='https://smarteye-sgsits.000webhostapp.com/images/a.jpg'
		#
		print("check2")
	
		
		cmp_ = app_.compare.get(image_url1 = image1,image_url2 = image2) 
		print('Photo1', '=', cmp_.image1) 
		print('Photo2', '=', cmp_.image2) 
		i=i+1
		# Comparing Photos 
		
		if cmp_.confidence > 70: 
			
			#if check(0) == False:
			print('Both photographs are of same person......')
			
			return False,True 
		else:
			pass 
			
	print('Both photographs are of two different persons......') 
		
	return False,False

