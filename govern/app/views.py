from django.shortcuts import render,redirect
from .models import Feedback,Government
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import requests,json
from django.db.models import Q
from django.contrib.auth.models import User

API_KEY = '7822d63ca35b4c81b7f068612db11ed7'
NEPAL_API = 'pub_41650693d6a27411873926057635a4d126354'


# Create your views here.

def home(request):
    national = f'https://newsdata.io/api/1/news?country=np&apikey={NEPAL_API}&domain=onlinekhabar,Nagarik News,The Himalayan Times'
    national_news = requests.get(national).json()['results'][:8]
    
    return render(request,'home.html',{'national_news':national_news})

def register(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        username = data['username']
        email = data['email']
        password = data['password']
        password1 = data['password1']

        if(password==password1):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists!')
                return redirect('register')
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                messages.success(request,'Registered successfully!')
                return redirect('log_in')

        else:
            messages.error(request, "Password doesn't match")
            return redirect('register')


    return render(request, 'auth/register.html')

def log_in(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Welcome")
            return redirect('home')
        else:
            messages.error(request,"Try again!")
            return redirect('log_in')
    return render(request,'auth/login.html')


def log_out(request):
    logout(request)
    return redirect('log_in')

def feedback(request):
    if request.method == 'POST' and request.FILES:
        data = request.POST
        name = data['name']
        email = data['email']
        desc = data['desc']
        image = request.FILES['image']
        ob = Feedback(name=name, email=email, desc=desc,image=image)
        ob.save()
        messages.success(request, "Successfully added!")
        return redirect('feedback')
    
    data = Feedback.objects.all()
    return render(request, 'feedback.html',{'data':data})

def news(request):
    url = f'https://newsapi.org/v2/everything?domains=bbc.co.uk&apiKey={API_KEY}'
    articles = requests.get(url).json()['articles']
    international_news = articles[:8]
    

    national = f'https://newsdata.io/api/1/news?country=np&apikey={NEPAL_API}&domain=onlinekhabar,Nagarik News'
    national_news = requests.get(national).json()['results'][:8]
    latest_news = national_news[:1]
    trending_news = national_news[2:5]

    finance1 = f'https://newsdata.io/api/1/news?apikey={NEPAL_API}&country=np&category=business '
    financial_news = requests.get(finance1).json()['results'][:8]

    sports1 = f'https://newsdata.io/api/1/news?apikey={NEPAL_API}&q=sports&country=np&category=sports'
    sports_news = requests.get(sports1).json()['results'][:8]

    
    
    return render(request,'news.html',
                  {'articles':articles,
                   'latest_news':latest_news,
                   'national_news':national_news,
                   'financial_news':financial_news,
                   'sports_news':sports_news,
                   'international_news':international_news,
                   'trending_news':trending_news,

                   })

def about(request):
    return render(request,'about.html')


def government(request):
    data = Government.objects.all()
    return render(request,'government.html',{'data':data})

# for searching among the listed government sites
def searchGov(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        finds = Government.objects.filter(title__contains=searched)
        return render(request, 'searchGov.html', {'finds': finds})
    

def notices(request):
    return render(request,'notices.html')

KHALTI_API = 'key test_secret_key_1f343049d02d4944ab23b6a442f4947a'

def initkhalti(request):
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    return_url = request.POST.get('return_url')
    website_url = request.POST.get('return_url')
    amount = '200'
    purchase_order_id = request.POST.get('purchase_order_id')
    purchase_order_name = request.POST.get('purchase_order_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')


    print("url",url)
    print("return_url",return_url)
    print("web_url",website_url)
    print("amount",amount)
    print("purchase_order_id",purchase_order_id)
    print('username',username)
    print('email',email)
    print('phone',phone)
    payload = json.dumps({
        "return_url": return_url,
        "website_url": return_url,
        "amount": '1000',
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": purchase_order_name,
        "customer_info": {
            "name": username,
            "email": email,
            "phone": phone,
        }
    })

    # put your own live secet for admin
    headers = {
        'Authorization': 'key test_secret_key_1f343049d02d4944ab23b6a442f4947a',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    new_res = json.loads(response.text)

    print(type(new_res))
    # return redirect('notices')
    # print(response.json())
    return redirect(new_res['payment_url'])

# def verifyKhalti(request):
#     url = "https://a.khalti.com/api/v2/epayment/lookup/"
#     if request.method == 'GET':
#         headers = {
#             'Authorization': 'key test_secret_key_dcba60e58f5349b98c95feb9fca2bc46',
#             'Content-Type': 'application/json',
#         }
#         pidx = request.GET.get('pidx')
#         data = json.dumps({
#             'pidx':pidx
#         })
#         res = requests.request('POST',url,headers=headers,data=data)
#         print(res)
#         print(res.text)

#         new_res = json.loads(res.text)
#         print(new_res)
        

#         if new_res['status'] == 'Completed':
#             # user = request.user
#             # user.has_verified_dairy = True
#             # user.save()
#             # perform your db interaction logic
#             pass
        
#         # else:
#         #     # give user a proper error message
#         #     raise BadRequest("sorry ")

#         return redirect('notices.html')
