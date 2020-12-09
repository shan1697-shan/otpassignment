
from django.shortcuts import render,redirect,HttpResponse
from twilio.rest import Client
import random
from django.contrib.sessions.models import Session

def login(request):
    if request.method=='POST':
        if 'generate' in request.POST:
            num = request.POST['num']
            number='+91'+num
            otp = str(random.randint(100000, 999999))
            request.session['otpcarrier'] = otp
            account_sid = 'AC412XXXXXXXXXXX'
            auth_token = 'XXXXXXXXXXXXX'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                    body='This is a test otp '+otp+'.',
                    from_='+19282359504',
                    to=number
                )
            # print(message.sid)
            return render(request, 'mainapp/index.html',{'data':num})

        elif 'validate' in request.POST:
            checkval = request.session['otpcarrier']
            val = request.POST['otp']
            if val==checkval:
                request.session['otpcarrier']=''
                request.session['logged']=True
                return redirect('/home')
            else:
                msg = 'Incorrect OTP'
                return render(request, 'mainapp/index.html',{'error':msg})

        else:
            return render(request, 'mainapp/index.html')

    else:
        return render(request, 'mainapp/index.html')


def home(request):
    if request.session['logged']==True:
        return render(request,'mainapp/home.html')
    else:
        return redirect('/')

def logout(request):
    request.session['logged']=False
    return render(request, 'mainapp/index.html')

# +19282359504
