from django.shortcuts import render
from django.http import JsonResponse
import random
import smtplib
from django.http import HttpResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import firebase_admin
from firebase_admin import credentials, initialize_app, storage
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


def handler404(request,exception):
    return render(request, '404.html', status=404)
def handler500(request):
    return render(request, 'login.html', status=500)


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
# Create your views here.

# ##################################################################################################################
# def opencamera(request):
#     if request.session['login_confirm'] == True:
#         return render(request,'opencamera.html')
#     else:
#         return render(request, 'login.html')
# def success(request):
#     ##print(request.POST)
#     ##print(request.FILES)
#     if request.method=='POST':
#         #print('in POST ')
#
#         uri=request.POST['check_this']
#         ##print(uri)
#         ##print(type(uri))
#         encoded_data = uri.split(',')[1]
#         nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
#         image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#         ##print(type(image))
#         #cv2.imwrite('MeterReaderApp/Static/image.png',image)
#         height, width = image.shape[:2]
#         y=((height // 2) - 100)
#         y1=((height //2) + 100)
#         x=((width // 2) - (round(width // 2.5)))
#         x1=((width // 2) + (round(width//2.5)))
#         image = image[y: y1,x:x1]
#         #cv2.imwrite('MeterReaderApp/Static/generated/image111.png', image)
#         image = imutils.resize(image, height=200, width=400)
#         ##print(type(image))
#         #image = cv2.imread('new111.png')
#         gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#         thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU + 1)[1]
#         kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
#         thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
#         # cv2.imshow('thresh',ret)
#
#         #cv2.imwrite('MeterReaderApp/Static/generated/thresh.png', thresh)
#
#         #out_below = pytesseract.image_to_string(thresh, config='--oem 3 --psm 7 outbase digits')
#
#         ##print('output',out_below)
#
#         kernel = np.ones((5, 5), np.uint8)
#
#         erosion = cv2.erode(thresh, kernel, iterations=1)
#
#         img_dilation = cv2.dilate(thresh, kernel, iterations=2)
#
#
#
#         #cv2.imwrite('MeterReaderApp/Static/generated/erosion.png', erosion)
#
#         #cv2.imwrite('MeterReaderApp/Static/generated/dilation.png', img_dilation)
#
#         out_below1 = pytesseract.image_to_string(erosion, config='--oem 3 --psm 7 outbase digits')
#         ##print("OUTPUT222:", out_below1)
#
#         context={
#             "reading":out_below1,
#             'image':image
#         }
#         return render(request,'after_capture.html',context=context)
#     else:
#         ##print('inget')
#         #print(request.GET)
#         return render(request,'j.html')
#
# def generated_bill(request):
#
#     doc = DocxTemplate("MeterReaderApp/Static/SampleBill.docx")
#
#     context_doc = {'meterNumber': '123456789',
#                     'customer_name': 'avsss',
#                     'previousYear':123,
#                     'currentYear':123
#                    }
#     doc.render(context_doc)
#     doc.save("MeterReaderApp/Static/generated/GeneratedBill.docx")
#
#
#
#     return render(request,'generated_bill.html')
#
# def dashboard(request):
#
#     if request.method == 'POST':
#         global login_confirm
#         Loggedin_user_ivrs_no = request.POST['ivrs_no']
#         Loggedin_user_psw = request.POST['psw']
#
#         check_user = firebaseuser.get('/UserRegister', name=Loggedin_user_ivrs_no)
#         if check_user != None :
#             if str(check_user['ivrs']) == Loggedin_user_ivrs_no and check_user['pasword'] == Loggedin_user_psw:
#                 if check_user['auth']==True:
#                     login_confirm = True
#                     request.session['login_confirm'] = login_confirm
#                     return render(request, 'dashboard.html')
#                 else:
#                     login_confirm = False
#                     request.session['login_confirm'] = login_confirm
#                     return render(request, 'j.html')
#
#             else :
#                 login_confirm = False
#                 request.session['login_confirm'] = login_confirm
#                 return render(request, 'login.html',context={'notcorrect':True})
#
#
#         else:
#             return render(request, 'login.html',context={'nouser':True})
#     else:
#         if request.session['login_confirm'] == False :
#             return render(request, 'login.html')
#         elif request.session['login_confirm'] == True :
#             return render(request, 'dashboard.html')
################################################################################################################
def adminlogin(request):
    allusers = searched_user = firebaseuser.get('/UserRegister', '')
    verified_user = 0
    not_verified_user = 0
    user_complaint = 0
    total_user = len(allusers)
    Complaints = 0
    Appli_suggetion = 0
    Emergency_Complaints = 0
    reply = 0
    for i in allusers:
        if allusers[i]['auth'] == 'true':
            verified_user += 1
        else:
            not_verified_user += 1
        if 'Complaints' in allusers[i].keys():
            user_complaint += 1
            for j in allusers[i]['Complaints']:
                if j:
                    if j['complaintType'] == 'Emergency Complaints':
                        Emergency_Complaints += 1
                    elif j['complaintType'] == 'Application/Suggestions':
                        Appli_suggetion += 1
                    else:
                        Complaints += 1
                    if 'reply' in j.keys():
                        reply += 1
    context = {
        "verified_user": verified_user,
        "not_verified_user": not_verified_user,
        "user_complaint": user_complaint,
        "total_user": total_user,
        "Complaints": Complaints,
        "Appli_suggetion": Appli_suggetion,
        "TotalComplaints": Appli_suggetion + Complaints + Emergency_Complaints,
        "Emergency_Complaints": Emergency_Complaints,
        "reply": reply


    }
    if request.method=='POST':
        Loggedin_admin_user_name = request.POST['admin_uname']
        Loggedin_admin_psw = request.POST['admin_psw']
        search_admin = firebaseadmin.get('/Admin', name=Loggedin_admin_user_name)
        if search_admin != None:
            if search_admin['admin_username'] == Loggedin_admin_user_name and search_admin['admin_pswrd'] == Loggedin_admin_psw:
                login_admin_confirm = True
                request.session['login_admin_confirm']=login_admin_confirm
                request.session['admin_name']=Loggedin_admin_user_name
                #print(search_admin['admin_designation'])
                request.session['admin_designation']=search_admin['admin_designation']
                request.session['admin_full_name']=search_admin['admin_fullname']
                context['admin_name']= request.session['admin_full_name']
                return render(request, 'Admin_dasboard.html',context=context)
            else:
                login_admin_confirm = False
                request.session['login_admin_confirm'] = login_admin_confirm
                return render(request, 'login.html',context={'admin_pswrd':True})
        else :
            login_admin_confirm = False
            request.session['login_admin_confirm']=login_admin_confirm
            return render(request, 'login.html',context={'no_admin':True})
    else:
        if request.session['login_admin_confirm']==True:
            context['admin_name'] = request.session['admin_full_name']
            return render(request, 'Admin_dasboard.html',context=context)
        else:
            return render(request, 'login.html')

def user_register_view(request):

    if request.method=='POST':
        register_data = request.session['register']
        data={
        'name' : register_data[0],
        'address' : register_data[1],
        'phoneno' : register_data[2],
        'ivrs' : register_data[3],
        'email' : register_data[4],
        'pasword':request.POST['pswrd'],
        'auth':'false'
        }
        firebaseuser.put('/UserRegister/',name=str(register_data[3]),data=data)
    return render(request, 'login.html')


#############################################################################################################
def email_verification(request):
    if request.method=='POST':
        ##print('fffffffffffffffffffffffffff',request.POST)
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
#############################################################################################################

def forgotpassword(request):
    if request.method == 'POST':

        return render(request, "forgotpassword.html")

def logout(request):
    request.session['login_admin_confirm'] = False
    return render(request, 'login.html')

def login(request):

    # if request.method=="POST":
    #     ##print(request.POST)
    #     if request.POST['pswrd'] == request.POST['cnfirm_pswrd']:
    #         pswrd=request.POST['cnfirm_pswrd']
    #         register_value = request.session["register"]
    #         data = {"pasword": pswrd, "ivrs": register_value[3], "name": register_value[0], "address": register_value[1], "phoneno": register_value[2], "auth": False,
    #         "email":register_value[4]}
    #         ##print(firebaseuser.get('/UserRegister',name=str(register_value[3])))
    #         if firebaseuser.get('/UserRegister',name=str(register_value[3])) == None:
    #             firebaseuser.put('/UserRegister',data=data,name=register_value[3])
    #             context = {
    #                 'register': True
    #             }
    #         else:
    #             context={
    #             'Already_register': True
    #             }
    #         return render(request, 'login.html',context=context)
    #     else :
    #         context={
    #             'not_match': True
    #         }
    #         return render(request, 'password.html',context=context)
    try :
        if request.session['login_admin_confirm'] ==False:
            return render(request, 'login.html')
        elif request.session['login_admin_confirm'] == True:
            return render(request, 'Admin_dasboard.html', context={'admin_name':request.session['admin_full_name']})
    except:
        #print(request.session)
        return render(request, 'login.html')

def register(request):

    return render(request, 'register.html')


def new_user_request(request):
    if request.session['login_admin_confirm'] == True:
        allusers = firebaseadmin.get('/UserRegister', None)
        requestlist = []
        for i in allusers:
            if allusers[i]['auth']!='true':
                ##print(allusers[i]['auth'])
                requestlist.append(allusers[i])
        return render(request,'new.html',context={'requestlist':requestlist,'admin_name':request.session['admin_full_name']})
    else:
        return render(request, 'login.html')

def all_user(request):
    if request.session['login_admin_confirm'] == True:
        allusers = firebaseadmin.get('/UserRegister', None)
        context={
            'all_user':allusers,'admin_name':request.session['admin_full_name']
        }
        return render(request,'AllUser.html',context=context)
    else:
        return render(request, 'login.html')

def search_user(request):
    if request.session['login_admin_confirm'] == True:
        return render(request,'search_user.html',context={'admin_name':request.session['admin_full_name']})
    else:
        return render(request, 'login.html')

def user_profile(request):

    if request.method=="POST":
        #print(request.POST)
        search_ivrs=request.POST['ivrs']
        searched_user = firebaseuser.get('/UserRegister', name=search_ivrs)
        #print(searched_user)
        #print(searched_user['name'])
        if searched_user == None :
            context={
                'nouserfound':True
            }
            return render(request,'search_user.html',context=context)
        else:
            context={
                'searched_user':searched_user,'admin_name':request.session['admin_full_name']
            }
        return render(request,'userprofile.html',context=context)
    else:
        if request.session['login_admin_confirm'] == True:
            return render(request, 'search_user.html',context={'admin_name':request.session['admin_full_name']})
        else:
            return render(request, 'login.html')

def update_user_profile(request):
    if request.method=="POST":
        #print(request.POST)
        search_ivrs=request.POST['ivrs']
        #print(searched_user)
        firebaseuser.put('/UserRegister/'+str(search_ivrs),'name',request.POST['name'])
        firebaseuser.put('/UserRegister/'+str(search_ivrs),'ivrs',request.POST['ivrs'])
        firebaseuser.put('/UserRegister/'+str(search_ivrs),'address',request.POST['address'])
        firebaseuser.put('/UserRegister/'+str(search_ivrs),'phoneno',request.POST['phoneno'])
        firebaseuser.put('/UserRegister/'+str(search_ivrs),'email',request.POST['email'])
        searched_user = firebaseuser.get('/UserRegister', name=search_ivrs)
        #print(searched_user)
        context={
                'searched_user':searched_user,
            'admin_name':request.session['admin_full_name']
        }
        return render(request,'userprofile.html',context=context)
    else:
        if request.session['login_admin_confirm'] == True:
            return render(request, 'userprofile.html', context=context)
        else:
            return render(request, 'login.html')

def add_new_user_request(request):
    if request.session['login_admin_confirm'] == True:
        if request.method == "POST":
            #print(request.POST)
            ivrs=request.POST['ivrs']
            initial_date=request.POST['initial_date']
            initial_reading=request.POST['initial_reading']
            email=request.POST['email']
            name=request.POST['name']
            firebaseuser.put('/UserRegister/' + str(ivrs), 'auth', 'true')
            initial_date=str(initial_date).replace('-','_')
            firebaseuser.put('/UserRegister/' + str(ivrs) + '/MeterReading/'+str(ivrs)+'00'+initial_date[5:7]+initial_date[:4]+'/',initial_date, initial_reading)
            firebaseuser.put('/UserRegister/' + str(ivrs) + '/' ,'Reading_Date',initial_date[8:])
            mail_content='''
            Hello, {0}
            
            You are Verified for your Ivrs No. : {1}
            
            Please Try to login 
            
            Thanks 
            Team MVAR   
            
            '''.format(name,ivrs)
            send_coad(email, mail_content)

            allusers = firebaseadmin.get('/UserRegister', None)
            requestlist = []
            for i in allusers:
                if allusers[i]['auth']!='true':
                    ##print(allusers[i]['auth'])
                    requestlist.append(allusers[i])
            return render(request,'new.html',context={'requestlist':requestlist,'admin_name':request.session['admin_full_name']})
    else:
        return render(request, 'login.html')



def Not_Verify_user(request):
    if request.session['login_admin_confirm'] == True:
        if request.method == "POST":
            ivrs = request.POST['ivrs']
            email = request.POST['email']
            name = request.POST['name']
            message = request.POST['message']

            mail_content = '''
                Hello, {0}
        
                Sorry {0} we can't verify you for your Ivrs No. : {1}.
                
                Message from our admin : {2} 
        
                Please Try to contact our Admin Team . 
        
                Thanks 
                Team MVAR   
                
                '''.format(name, ivrs,message)
            send_coad(email, mail_content)
            firebaseuser.put('/UserRegister/' + str(ivrs), 'message', message)
            allusers = firebaseadmin.get('/UserRegister', None)
            requestlist = []
            for i in allusers:
                if allusers[i]['auth'] != 'true':
                    ##print(allusers[i]['auth'])
                    requestlist.append(allusers[i])

            return render(request, 'new.html',
                          context={'requestlist': requestlist, 'admin_name': request.session['admin_full_name']})
    else:
        return render(request, 'login.html')

def AdminProfile(request):
    if request.session['login_admin_confirm'] == True:

        admin_name=request.session['admin_name']
        admin_designation=request.session['admin_designation']
        admin_full_name=request.session['admin_full_name']
        context={'admin_name':admin_name,
                 'admin_designation':admin_designation,
                 'admin_full_name':admin_full_name
                 }
        return render(request,'AdminProfile.html',context=context)
    else:
        return render(request, 'login.html')

def AddAdmin(request):
    if request.session['login_admin_confirm'] == True:
        if request.method=='POST':
            admin_fullname=request.POST['admin_name']
            admin_username=request.POST['admin_username']
            pswrodadmin=request.POST['paswrd']
            c_pswrodadmin=request.POST['cpaswrd']
            admin_Designation=request.POST['admin_Designation']
            if c_pswrodadmin == pswrodadmin:
                data={'admin_fullname':admin_fullname,
                    'admin_username':admin_username,
                     'admin_pswrd': pswrodadmin,
                      'admin_designation':admin_Designation
                      }
                search_admin=firebaseuser.get('/Admin', name=admin_username)
                #print(search_admin)
                if search_admin == None:
                    firebaseadmin.put('/Admin', data=data, name=admin_username)
                    return render(request, 'AddAdmin.html', context={'Added': True,'admin_name':request.session['admin_full_name']})
                else:
                    return render(request, 'AddAdmin.html',context={'already':True,'admin_name':request.session['admin_full_name']})
            else:
                return render(request, 'AddAdmin.html',context={'notmatch':True,'admin_name':request.session['admin_full_name']})
        return render(request, 'AddAdmin.html',context={'admin_name':request.session['admin_full_name']})
    else:
        return render(request, 'login.html')




def complaints(request):
    if request.session['login_admin_confirm'] == True:

        if request.method=='POST':
            print(request.POST)
            ivrs_complaint=request.POST['ivrs_complaint']
            ivrs_complaint_no=request.POST['ivrs_complaint_no']
            reply_complaint=request.POST['reply_complaint']
            complaint=request.POST['complaint']
            complaint_type=request.POST['complaint_type']
            searched_user = firebaseuser.get('/UserRegister', ivrs_complaint)
            count = -1
            for i in searched_user['Complaints']:
                count += 1
                if i:
                    if i['complaintMessage'] == complaint and i['complaintType']==complaint_type:
                        #print(i)
                        firebaseuser.put('/UserRegister/' + str(ivrs_complaint) + '/Complaints/' + str(count) + '/' , 'reply', reply_complaint)
        searched_user = firebaseuser.get('/UserRegister', '')
        complaint = []
        emergency_ivrs = []
        emergency_dict = {}
        emergency_ivrs_complaint = []
        complaint_ivrs = []
        complaint_dict = {}
        complaint_ivrs_complaint = []
        appli_sugg_ivrs = []
        appli_sugg_dict = {}
        appli_sugg_ivrs_complaint = []
        for i in searched_user:
            # print(i)
            if 'Complaints' in searched_user[i].keys():
                complaint.append(i)
                for j in searched_user[i]["Complaints"][1:]:
                    val = j.values()
                    if 'Emergency Complaints' in val:
                        emergency_ivrs_complaint.append(j['complaintMessage'])
                        if i in emergency_dict.keys():
                            emergency_dict[i].append(j['complaintMessage'])
                        else:
                            emergency_ivrs.append(i)
                            emergency_dict[i] = [j['complaintMessage']]
                    elif 'Complaints' in val:
                        complaint_ivrs_complaint.append(j['complaintMessage'])
                        if i in complaint_dict.keys():
                            complaint_dict[i].append(j['complaintMessage'])
                        else:
                            complaint_ivrs.append(i)
                            complaint_dict[i] = [j['complaintMessage']]
                    elif 'Application/Suggestions' in val:
                        appli_sugg_ivrs_complaint.append(j['complaintMessage'])
                        if i in appli_sugg_dict.keys():
                            appli_sugg_dict[i].append(j['complaintMessage'])
                        else:
                            appli_sugg_ivrs.append(i)
                            appli_sugg_dict[i] = [j['complaintMessage']]

        complaint_ivrs = list(set(complaint_ivrs))
        context={
            'emergency_ivrs':emergency_ivrs,
            'emergency_dict':emergency_dict,
            'emergency_ivrs_complaint':emergency_ivrs_complaint,
            'complaint_ivrs':complaint_ivrs,
            'complaint_ivrs_complaint':complaint_ivrs_complaint,
            'complaint_dict':complaint_dict,
            'appli_sugg_ivrs':appli_sugg_ivrs,
            'appli_sugg_ivrs_complaint':appli_sugg_ivrs_complaint,
            'appli_sugg_dict':appli_sugg_dict,
            'admin_name': request.session['admin_full_name']
        }
        return render(request,'All_Complaints.html',context=context)
    else:
        return render(request, 'login.html')



@csrf_exempt
def test(request):
    ivrs_no = request.POST['ivrs']
    current_reading = request.POST['CurrentReading']
    current_date = request.POST['CurrentDate']
    current_date = current_date.replace('_',',')
    user = firebaseuser.get('/UserRegister', name=ivrs_no)
    # if len(list(user['MeterReading'].keys())) >= 1:
    a = user['MeterReading'][list(user['MeterReading'].keys())[-2]]
    customer_name=user['name']
    customer_email=user['email']
    customer_address=user['address']
    customer_phoneno=user['phoneno']
    customer_auth=user['auth']
    if customer_auth=='true':
        customer_auth='Verified User'
    elif customer_auth=='false' :
        customer_auth = 'Not Verified '

    previous_date = list(a.keys())[0].replace('_',',')
    previous_reading = list(a.values())[0]
    date_format = "%Y,%m,%d"
    pd = datetime.strptime(previous_date, date_format)
    cd = datetime.strptime(current_date, date_format)
    days = (cd - pd).days

    units = int(current_reading) - int(previous_reading)


    if (units < 50):
        amount = units * 2.60
        surcharge = 25
    elif (units <= 100):
        amount = 130 + ((units - 50) * 3.25)
        surcharge = 35
    elif (units <= 200):
        amount = 130 + 162.50 + ((units - 100) * 5.26)
        surcharge = 45
    else:
        amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
        surcharge = 75

    total = amount + surcharge


    doc = DocxTemplate("staticfiles/SampleBill.docx")
    avg_unit=units/days
    context_doc = {'ivrs': ivrs_no,
               'customer_name': customer_name,
               'customer_address': customer_address,
               'previous_date': previous_date,
               'current_date': current_date,
               'current_reading': current_reading,
               'previous_reading': previous_reading,
               'days': days,
               'supplycharges': surcharge,
               'units': units,
               'amount': amount,
               'total_amount': total,
               'customer_email': customer_email,
               'avg_unit': avg_unit,
               'customer_status': customer_auth,
               'customer_phoneno': customer_phoneno
               }
    doc.render(context_doc)
    doc.save("staticfiles/generated/GeneratedBill.docx")

    # Init firebase with your credentials
    if not firebase_admin._apps:
        cred = credentials.Certificate("login-system-73453-5ca66a2acaee.json")
        initialize_app(cred, {'storageBucket': 'login-system-73453.appspot.com'})

    # Put your local file path
    fileName = "staticfiles/generated/GeneratedBill.docx"
    bucket = storage.bucket()
    blob = bucket.blob(ivrs_no+'/'+current_date+'.docx')
    blob.upload_from_filename(fileName)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    firebaseuser.put('/UserRegister/' + ivrs_no + '/MeterReading', ivrs_no + '00'+str(cd.month)+str(cd.year)+'/Bill/', blob.public_url)
    firebaseuser.put('/UserRegister/' + ivrs_no + '/MeterReading', ivrs_no + '00'+str(cd.month)+str(cd.year)+'/Bill_Amount/', total)
    return  HttpResponse({blob.public_url}, list(user['MeterReading'].keys()))
