import smtplib
#from email.MIMEMultipart import MIMEMultipart
from email.mime.multipart import MIMEMultipart
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText
#from email.MIMEImage import MIMEImage
from email.mime.image import MIMEImage
# Email you want to send the update from (only works with gmail)
fromEmail = 'harish.lohare1998@gmail.com'
fromEmail = 'lokendra.singh0801cs39@gmail.com'
# You can generate an app password here to avoid storing your password in plain text
# https://support.google.com/accounts/answer/185833?hl=en
#fromEmailPassword = 'deepchand1998'
fromEmailPassword = 'Lokendra@123'

# Email you want to send the update to
#toEmail = 'hdlohare98@gmail.com'
toEmail = 'slokendra238@gmail.com'
#toEmail = 'yashpathakmmps1@gmail.com'

def sendEmail(image):
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'Security Update'
	msgRoot['From'] = fromEmail
	msgRoot['To'] = toEmail
	msgRoot.preamble = 'Smart Eye Security Camera Update'

	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgText = MIMEText('Smart security camera found object') #convert plain text into mime text
	msgAlternative.attach(msgText)     #attach msg within a mail

	msgText = MIMEText('<img src="cid:image1">', 'html') #image address converted as mime type
	msgAlternative.attach(msgText)     #attach image address within a mail

	msgImage = MIMEImage(image)
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)

	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.starttls()
	smtp.login(fromEmail, fromEmailPassword)
	smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
	smtp.quit()
