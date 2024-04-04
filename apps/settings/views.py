from django.shortcuts import render
from apps.settings.models import Settings, Slide, Services, Video
from apps.secondary.models import About,News, Gallery
from apps.team.models import Team,Founder
from apps.contact.models import Contacts,PageContact

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)
    settings = Settings.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest('id')
    news = News.objects.all()
    video = Video.objects.latest('id')
    services = Services.objects.all()
    team = Team.objects.all()
    founder = Founder.objects.latest('id')
    return render(request, 'base/index.html', locals())

def about(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)
    settings = Settings.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest('id')
    news = News.objects.all()
    video = Video.objects.latest('id')
    service = Services.objects.all()
    team = Team.objects.all()
    founder = Founder.objects.latest('id')
    return render(request, 'about.html', locals())

def contact(request):
#     if request.method =="POST":
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         date = request.POST.get('date')
#         message = request.POST.get('message')
#         # reserv = Reserv.objects.create(name = name,phone = phone,date = date,message=message)

    settings = Settings.objects.latest('id')
    
    return render(request, 'contact.html', locals())

def gallery(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)
    settings = Settings.objects.latest('id')
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', locals())

def news(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        contacts = Contacts.objects.create(name=name, number=number, data=data)
    settings = Settings.objects.latest('id')
    news = News.objects.all()
    return render(request, 'news.html', locals())

def post(request):
    return render(request, 'post.html', locals())

def team(request):
    if request.method=="POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        data = request.POST.get('data')
        subject = request.POST.get('subject')
        contacts = PageContact.objects.create(name=name, number=number, data=data, subject=subject)
    settings = Settings.objects.latest('id')
    team = Team.objects.all()
    return render(request, 'team.html', locals())
    

