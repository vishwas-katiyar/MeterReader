from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from firebase import firebase
firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/UserRegister/', None)


from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='*' ,minute='*')
def scheduled_job():
    def send_coad(receiver_address,mail_content):
        sender_address = 'meterreading1628@gmail.com'
        sender_pass = 'MvarProject@1436'
        #receiver_address = 'honeykatiyar1436@gmail.com'
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'MVAR Administrations '   #The subject line
        message.attach(MIMEText(mail_content, 'plain'))
        session1 = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session1.starttls() #enable security
        session1.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session1.sendmail(sender_address, receiver_address, text)
        session1.quit()

    def check():
        all_user = firebaseuser.get('/UserRegister','')
        today = today = date.today()

        for i in all_user:

            if str(today)[8:] == all_user[i]['Reading_Date'] :
                msg='''
    
    Hello, {0} 

    Today is the date for your Meter Reading of 
    IVRS No. {1} .
    Please take reading by today otherwise penulty will be fined .

    Ignore if reading is already taken .

    Thanks
    Team MVAR


    '''.format(all_user[i]['name'],i)
                send_coad(all_user[i]['email'],msg)

    check()
    print('This job is run every weekday at 5pm.')

sched.start()

