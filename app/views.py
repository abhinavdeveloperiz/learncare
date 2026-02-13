from django.shortcuts import render,redirect



def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about.html')

def colleges_nd_courses(request):
    return render(request,'colleges_nd_courses.html')

def college_details(request):
    return render(request,'collage_details.html')

def contactus(request):
    return render(request,'contact.html')