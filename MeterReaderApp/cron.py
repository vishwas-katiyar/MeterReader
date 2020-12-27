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
    send_coad('honeykatiyar1436@gmail.com','helloww this is from cron job')
    return print('print')