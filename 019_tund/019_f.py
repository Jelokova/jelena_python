import smtplib
from email.message import EmailMessage

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# with smtplib.SMTP('smtp.zone.eu', 587) as server:
#     server.ehlo()
#     server.starttls()
#     server.ehlo()

with smtplib.SMTP_SSL('smtp.zone.eu', 465) as server:
    server.login('tester@mrartful.com','test1269bfg90')

    msg=EmailMessage()
    msg['From']='Python <tester@mrartful.com>'
    msg['To']='Jelena <jelokova.ee@gmail.com>'
    msg['Subject']='Hello python'
    msg.set_content('This is a test email sent by Python script')
    msg.add_alternative(f'<h1>Hello world!</h1>'
                        f'<p style="color: red;>"This is a test email sent by Python script</p>', subtype='html')
    server.send_message(msg)


   #  body='This is a test email sent by Python script'
   #  body2=  f'<h1>Hello world!</h1>'\
   #          f'<p style="color:red;>"This is a test email sent by Python script</p> '
   # # msg.attach(MIMEText(body,'plain'))
   #  msg.attach(MIMEText(body2, 'html'))
   #  text=msg.as_string()
   #  server.sendmail('tester@mrartful.com','jelokova.ee@gmail.com',text)