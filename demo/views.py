from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersforms
import math

def homePage(request):

    return render(request,"index.html")

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

def services(request):
    return render(request,"services.html")

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


