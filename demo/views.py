from django.core import paginator
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersforms
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contactenquiry.models import contactEnquiry
from django.core.mail import send_mail,EmailMultiAlternatives




import math

def homePage(request):
    subject='Testing Mail'
    form_email='shukladeepti293@gmail.com'
    msg='<p>Welcome to <b>Adventure Awaits</b></b>'
    to='deeptishukla515@gmail.com'
    msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    msg.content_subtype='html'
    msg.send()
    # send_mail(
    #     'Testing Mail',
    #     'Here is the message.',
    #     'shukladeepti293@gmail.com',
    #     ['deeptishukla515@gmail.com'],
    #     fail_silently=False,
    # )



    newsData=News.objects.all();
    servicesData=Service.objects.all().order_by('-service_title')[:4]
    # for a in servicesData:
    #     print(a.service_icon)
    # print(services)

    data={
        'newsData':newsData,
        'servicesData':servicesData
    }
    return render(request,"index.html",data)

def newsDetails(request,slug):
    newsDetails=News.objects.get(news_slug=slug)
    data={
        'newsDetails':newsDetails
    }
    return render(request,"newsdetails.html",data)


def submitform(request):

        try:
            if request.method=="POST":
        
                n1=int(request.POST.get('num1'))
                n2=int(request.POST.get('num2'))
                finalans=n1+n2

                data={
                    'n1':n1,
                    'n2':n2,
                    'output': finalans
                }

                return HttpResponse(finalans)

        except:
            pass
    

def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('output')
    
    return render(request,"aboutUs.html",{'output':output})

def contact(request):
    return render(request,"contact.html")

def saveEnquiry(request):

    n=''

    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        en=contactEnquiry(name=name,email=email,message=message)
        en.save()
        n='Thank you for your message!'

    return render(request,"contact.html",{'n' :n})

    
def services(request):
    ServicesData=Service.objects.all()
    paginator=Paginator(ServicesData,2)
    page_number=request.GET.get('page')
    ServiceDataFinal=paginator.get_page(page_number)
    totalpage=ServiceDataFinal.paginator.num_pages  #3
    data={
        'servicesData':ServiceDataFinal,
        'lastpage':totalpage,
        'totalPagelist':[n+1 for n in range (totalpage)]
    }
    
    
    
    
    
    
    # filter  option
    
    # if request.method=="GET":
    #     st=request.GET.get('servicename')
    #     if st!=None:
    #         servicesData=Service.objects.filter(service_title__icontains=st)

    # data={
    #     'servicesData':servicesData,
    # }
    return render(request,"services.html",data)
    

def destinations(request):
    return render(request,"destinations.html")

def gallery(request):
    return render(request,"gallery.html")


def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500;

        if p>=60:
            d="first Division"
        elif p>=48:
            d="Second Division"

        elif p>=35:
            d="Third Division"

        else:
            d="Fail"



        data={
            'total':t,
            'percentage':p,
            'division' :d
        }
        

    
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")



def saveevenodd(request):
    result=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render (request,"saveevenodd.html",{'error':True})



        n=eval(request.POST.get('num1'))
        if n%2==0:
            result="Even Number"
        else:
            result="odd Number"
    return render(request,"saveevenodd.html",{'result':result})

def calculator(request):

    result= ''

    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')

            if opr=="+":
                result=n1+n2

            elif opr=="-":
                result=n1-n2
            
            elif opr=="*":
                result=n1*n2
            
            elif opr=="/":
                result=n1/n2

    except:
        result="Invalid operator......"     
    print(result)
        


    return render(request,"calculator.html",{'result':result})

def userform(request):
    finalans=0
    fn=usersforms()
    # try:
    #     # n1=int(request.GET['num1'])
    #     # n2=int(request.GET['num2'])
    #     n1=int(request.GET.get('num1'))
    #     n2=int(request.GET.get('num2'))
    #     finalans=n1+n2

    #     # print(n1+n2);
    # except:
    #     pass

    data={'form':fn}
    try:
        if request.method=="POST":
        
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2

            data={
                'form':fn,
                'output':finalans

            }
            url="/about-us/?output=()".format(finalans)

            return redirect(url)

    except:
        pass

    return render(request,"userform.html", data)




def AdvanceCalculator(request):

    result= ''

    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')

            if opr=="+":
                result=n1+n2

            elif opr=="-":
                result=n1-n2
            
            elif opr=="*":
                result=n1*n2
            
            elif opr=="/":
                result=n1/n2

            elif opr=="math.remainder(n1,n2)":
                result=math.remainder(n1,n2)

    except:
        result="Invalid operator......"     
    print(result)
        


    return render(request,"calculator.html",{'result':result})


