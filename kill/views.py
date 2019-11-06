from django.shortcuts import render
from django.http import JsonResponse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Create your views here.
def index(request):
    return render(request,'index.html')

def valid(request):
    username = request.GET.get('username', None)
    email = request.GET.get('email', None)
    msg = request.GET.get('msg', None)
    message = MIMEMultipart("alternative")
    data = """
Subject: UserData\n
"""
    html = f"""\
<html>
  <body><div style="background:tomato;width:200px;height:200px; color:gray;padding:20px;">
       <b>username:{username}!</b>
        email: {email}!</b>
        message:{msg}!</b>
    </div>
    </p>
  </body>
  <style>
</html>
"""
    thanks = 'thank you'
    part1 = MIMEText(data, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pythoncode15@gmail.com','code@you')
    lol = True
    try:
        print('df')
        server.sendmail('pythoncode15@gmail.com', email, thanks)
        server.sendmail('pythoncode15@gmail.com', 'subhashlamichhane4@gmail.com', message.as_string())
    except:
        print('23')
        lol = False    
    server.close()
    return JsonResponse({'valid':lol})


     