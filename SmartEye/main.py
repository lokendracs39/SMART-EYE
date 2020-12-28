import cv2
import sys
from mail import sendEmail
from comp_trans import transfer

from flask import Flask, render_template, Response
from camera import VideoCamera #change camera file to camera1_check
from flask_basicauth import BasicAuth
import time
import threading



#
#####IMPLEMENTING ARRIVE SON FUNCTIONALITY##########
import datetime
import calendar
import time
now = datetime.datetime.now()
my_time_string1 = "20:00:00" # leap second
my_time_string2 = "21:00:00" # leap second
    
my_time_string1 = now.strftime("%Y-%m-%d") + " " + my_time_string1
my_time_string2 = now.strftime("%Y-%m-%d") + " " + my_time_string2 # I am supposing the date must be the same as now

my_time1 = time.strptime(my_time_string1, "%Y-%m-%d %H:%M:%S")
my_time2 = time.strptime(my_time_string2, "%Y-%m-%d %H:%M:%S")

my_datetime1 = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=calendar.timegm(my_time1))
my_datetime2 = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=calendar.timegm(my_time2))
############End###########

email_update_interval = 20 # sends an email only once in this time interval
video_camera = VideoCamera(flip=True) # creates a camera object, flip vertically
#object_classifier = cv2.CascadeClassifier("/home/pi/Downloads/SmartEye/models/facial_recognition_model.xml") # an opencv classifier
object_classifier = cv2.CascadeClassifier("/home/pi/Downloads/SmartEye/models/lbp_cascade.xml") # LBP an opencv classifier

# App Globals (do not edit)
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'CHANGE_ME_USERNAME'
app.config['BASIC_AUTH_PASSWORD'] = 'CHANGE_ME_PLEASE'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
last_epoch = 0
def check_for_objects(): #check for object
	global last_epoch
	while True:
		try:
		    frame, found_obj = video_camera.get_object(object_classifier)
			
			
		    print("smart eye watching......")
			
		    if found_obj and (time.time() - last_epoch) > email_update_interval:
			    last_epoch = time.time()
			    print("Smart Eye found object")
				#changes in
			    flag,person_exit=transfer(frame)
			    
			    print(person_exit)
			    if person_exit==True:
				    
				    if (now>my_datetime1) and (now<my_datetime2):
					    
					    if flag == True:
						    print("Specific family member arrived")
						    sendEmail(frame)
						    print ("Mail has been sent for corresponding family member")
					    else:
						    print("General Family member arrived....")
			    else:
				    print("Alert... Intruder detected")
				    print ("Sending email to user...")
				    sendEmail(frame)
				    print ("done!")
				    
		except:
			print ("Error sending email: ", sys.exc_info()[0])

#cv2.destroyAllWindows()

@app.route('/')
@basic_auth.required
def index():
    return render_template('index.html')


@app.route('/meow')
@basic_auth.required
def meow():
    return render_template('family_photo.html')
    
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    #camera.close()
@app.route('/video_feed')
def video_feed(): #for live video streeming
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    t = threading.Thread(target=check_for_objects, args=())
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', debug=False)
