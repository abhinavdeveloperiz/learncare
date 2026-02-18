from django.shortcuts import render,redirect,get_object_or_404
from app.models import Branch, Contact, Course, College, Location, University, Banner, Testimonial, CourseCategory
from .mail import send_contact_notification
from django.contrib import messages
from django.db.models import Prefetch,Q



def home(request):
    banner = Banner.objects.first()
    locations = Location.objects.all()
    university = University.objects.all()
    branch = Branch.objects.all()
    testimonials = Testimonial.objects.all()
    course_home = CourseCategory.objects.all()
    context = {
        'banner': banner,
        'locations': locations,
        'university': university,
        'branch': branch,
        'testimonials': testimonials,
        'course': course_home,
    }
    return render(request,'home.html',context)

def aboutus(request):
    location= Location.objects.all()
    context = {
        'location': location,
    }
    return render(request,'about.html',context)

def colleges_nd_courses(request):
    # Base queryset with prefetching for optimization
    colleges = College.objects.select_related('location').prefetch_related('courses').order_by('name')

    # --- FILTER BY LOCATION ---
    location_id = request.GET.get('location')  # Expecting a location ID
    if location_id:
        colleges = colleges.filter(location_id=location_id)

    # --- FILTER BY COURSES ---
    course_id = request.GET.get('course')  # Expecting a course ID
    if course_id:
        colleges = colleges.filter(courses__id=course_id).distinct()

    # --- SEARCH ---
    search_query = request.GET.get('q') 
    if search_query:
        colleges = colleges.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(courses__name__icontains=search_query) 
        ).distinct()

    all_courses = Course.objects.all()
    all_locations = Location.objects.all()

    context = {
        'colleges': colleges,
        'all_courses': all_courses,
        'all_locations': all_locations,
        'search_query': search_query,
        'selected_location': location_id,
        'selected_course': course_id,
    }
    return render(request, 'colleges_nd_courses.html', context)


def college_details(request,slug):
    college_details = get_object_or_404(College, slug=slug)
    return render(request,'college_details.html', {'college': college_details})





def contactus(request):
    branch = Branch.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        course = request.POST.get("course")
        location = request.POST.get("location")
        message = request.POST.get("message")

        # Save inquiry
        contact = Contact.objects.create(
            name=name,
            phone=phone,
            course=course,
            location=location,
            message=message
        )

        
        send_contact_notification(contact)
        messages.success(request, "Your inquiry has been submitted successfully!")
        return redirect("contact") 

    context = {
        'branch': branch,
    }

    return render(request, 'contact.html', context)

