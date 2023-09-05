from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def main(req):
    if req.method == 'POST':
        email = req.POST['mainemail']

        obj = main_page_email()
        obj.Email = email
        obj.save()

    lat = latest.objects.all()
    sli = slider.objects.all()

    return render(req,'index.html',{'lat':lat,'sli':sli})

def about_us(req):
    return render(req,'about-us.html')


# View Blogs in details/-------

def blog_post_details(req,pk):
    blog = get_object_or_404(blog_main,pk=pk)

    return render(req,'blog-post-details.html',{'blog':blog})

def lat_blog_post_details(req,pk):
    lat = get_object_or_404(latest,pk=pk)

    return render(req,'latest-blog-post-details.html',{'lat':lat})

#BLoGS/---

def blog_post(req):
    blog = blog_main.objects.all()

    return render(req,'blog-posts.html',{'blog':blog})

def special_offer(req):
    return render(req,'special-offer.html')
def team(req):
    return render(req,'team.html')

# Contact Details From User :
def B_contact(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        message = req.POST['message']

        obj = contact_details()
        obj.Name = name
        obj.Email = email
        obj.Msg = message
        obj.save()

    return render(req,'contact.html')

