from django.shortcuts import render
from django.http import JsonResponse
import numpy as np
import imutils
import pytesseract
import cv2
import base64
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from docxtpl import DocxTemplate
from firebase import firebase
firebaseuser = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/UserRegister/', None)
firebaseadmin = firebase.FirebaseApplication('https://login-system-73453.firebaseio.com/Admin/', None)

#cluster=MongoClient("mongodb+srv://MeterReaderDB:MeterReaderDB@cluster0.u4k67.mongodb.net/MeterReaderDB?retryWrites=true&w=majority")

#db=cluster["MeterReaderDB"]
#collection=db["MeterReaderCollection"]


#pytesseract.pytesseract.tesseract_cmd=r'MeterReaderApp/Tesseract-OCR/tesseract.exe'
#pytesseract.pytesseract.TESSDATA_PREFIX=r'MeterReaderApp/Tesseract-OCR/tessdata/'


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_coad(receiver_address,mail_content):
    sender_address = 'fruit.basket.team.14@gmail.com'
    sender_pass = 'FruitBasket'
    #receiver_address = 'honeykatiyar1436@gmail.com'
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Fruit Basket Email Verification Code '   #The subject line
    message.attach(MIMEText(mail_content, 'plain'))
    session1 = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session1.starttls() #enable security
    session1.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session1.sendmail(sender_address, receiver_address, text)
    session1.quit()
# Create your views here.


def opencamera(request):
    if request.session['login_confirm'] == True:
        return render(request,'opencamera.html')
    else:
        return render(request, 'login.html')
def success(request):
    if request.method=='GET':
        print('in get ')

        uri=request.GET['check_this']
        encoded_data = uri.split(',')[1]
        nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print(type(image))
        cv2.imwrite('MeterReaderApp/Static/image.png',image)
        height, width = image.shape[:2]
        y=((height // 2) - 100)
        y1=((height //2) + 100)
        x=((width // 2) - (round(width // 2.5)))
        x1=((width // 2) + (round(width//2.5)))
        image = image[y: y1,x:x1]
        cv2.imwrite('MeterReaderApp/Static/generated/image111.png', image)
        image = imutils.resize(image, height=200, width=400)
        print(type(image))
        #image = cv2.imread('new111.png')
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU + 1)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        # cv2.imshow('thresh',ret)

        cv2.imwrite('MeterReaderApp/Static/generated/thresh.png', thresh)

        out_below = pytesseract.image_to_string(thresh, config='--oem 3 --psm 7 outbase digits')

        print('output',out_below)

        kernel = np.ones((5, 5), np.uint8)

        erosion = cv2.erode(thresh, kernel, iterations=1)

        img_dilation = cv2.dilate(thresh, kernel, iterations=2)

        cv2.imwrite('MeterReaderApp/Static/generated/erosion.png', erosion)

        cv2.imwrite('MeterReaderApp/Static/generated/dilation.png', img_dilation)

        out_below1 = pytesseract.image_to_string(erosion, lang="lets", config='--oem 3 --psm 7 outbase digits')
        #print("OUTPUT222:", out_below1)

        context={
            "reading":out_below1,
            'image':image
        }
        return render(request,'after_capture.html',context=context)
    else:
        #print('inget')
        return render(request,'j.html')

def generated_bill(request):

    doc = DocxTemplate("MeterReaderApp/Static/SampleBill.docx")

    context_doc = {'meterNumber': '123456789',
                    'customer_name': 'avsss',
                    'previousYear':123,
                    'currentYear':123
                   }
    doc.render(context_doc)
    doc.save("MeterReaderApp/Static/generated/GeneratedBill.docx")



    return render(request,'generated_bill.html')

def dashboard(request):

    if request.method == 'POST':
        global login_confirm
        Loggedin_user_ivrs_no = request.POST['ivrs_no']
        Loggedin_user_psw = request.POST['psw']

        check_user = firebaseuser.get('/UserRegister', name=Loggedin_user_ivrs_no)
        print(check_user)
        if check_user != None :
            if str(check_user['ivrs']) == Loggedin_user_ivrs_no and check_user['pasword'] == Loggedin_user_psw:
                login_confirm = True
                request.session['login_confirm'] = login_confirm
                return render(request, 'dashboard.html')
            else :
                login_confirm = False
                request.session['login_confirm'] = login_confirm
                return render(request, 'login.html',context={'notcorrect':True})


        else:
            return render(request, 'login.html',context={'nouser':True})
    else:
        if request.session['login_confirm'] == False :
            return render(request, 'login.html')
        elif request.session['login_confirm'] == True :
            return render(request, 'dashboard.html')

def adminlogin(request):

    if request.method=='POST':
        Loggedin_admin_user_name = request.POST['admin_uname']
        Loggedin_admin_psw = request.POST['admin_psw']

        allusers = firebaseadmin.get('/Admin', '')
        for i in allusers:
            if allusers[i]['nameadmin'] == Loggedin_admin_user_name and allusers[i]['paswordadmin'] == Loggedin_admin_psw:
                login_admin_confirm = True
                request.session['login_admin_confirm']=login_admin_confirm
                return render(request, 'Admin_dasboard.html')
        else :
            login_admin_confirm = False
            request.session['login_admin_confirm']=login_admin_confirm
            return render(request, 'j.html')
    else:
        if request.session['login_admin_confirm']==True:
            return render(request, 'Admin_dasboard.html')
        else:
            return render(request, 'login.html')
def email_verification(request):
    if request.method=='POST':
        #print('fffffffffffffffffffffffffff',request.POST)
        Full_Name = request.POST['name']
        Address = request.POST['Add']
        Phone_No = request.POST['phone']
        ivrs_no = request.POST['ivrs_no']
        email = request.POST['email']

        generated_otp = random.randint(100000, 999999)
        mail_content = '''OTP For U : '''+str(generated_otp)+ '''  ::look'''
        send_coad(email, mail_content)

        request.session['generated_otp']=generated_otp
        request.session['register']=[Full_Name,Address,Phone_No,ivrs_no,email,generated_otp]


        #collection.insert_one({"_id": ivrs_no, "Full_Name": Full_Name,"Address": Address, "Phone_No": Phone_No,"auth": True,"Meter_no":Meter_no})

        return render(request,"email_verification.html")
    return render(request, "email_verification.html")


def password(request):
    if request.method == 'POST':
        generated_otp=request.session["generated_otp"]
        if request.POST['otp'] == str(generated_otp):
            return render(request,"password.html")
        else :
            return render(request, "email_verification.html")


def forgotpassword(request):
    if request.method == 'POST':

        return render(request, "forgotpassword.html")


def login(request):

    if request.method=="POST":
        #print(request.POST)
        if request.POST['pswrd'] == request.POST['cnfirm_pswrd']:
            pswrd=request.POST['cnfirm_pswrd']
            register_value = request.session["register"]
            data = {"pasword": pswrd, "ivrs": register_value[3], "name": register_value[0], "address": register_value[1], "phoneno": register_value[2], "auth": False,
            "email":register_value[4]}
            print(firebaseuser.get('/UserRegister',name=str(register_value[3])))
            if firebaseuser.get('/UserRegister',name=str(register_value[3])) == None:
                firebaseuser.put('/UserRegister',data=data,name=register_value[3])
                context = {
                    'register': True
                }
            else:

                context={
                'Already_register': True
                }
            return render(request, 'login.html',context=context)
        else :
            context={
                'not_match': True
            }
            return render(request, 'password.html',context=context)

    context = {
        'register': False
    }
    request.session['login_confirm'] = False
    return render(request, 'login.html',context=context)


def register(request):

    return render(request, 'register.html')


def new_user_request(request):
    allusers = firebaseadmin.get('/UserRegister', None)
    requestlist = []
    for i in allusers:
        if allusers[i]['auth']:
            #print(allusers[i]['auth'])
            requestlist.append(allusers[i])
    return render(request,'new.html',context={'requestlist':requestlist})

def all_user(request):
    allusers = firebaseadmin.get('/UserRegister', None)


    context={
        'all_user':allusers
    }
    return render(request,'AllUser.html',context=context)