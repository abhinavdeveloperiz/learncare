from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
        ordering = ['title']

    def __str__(self):
        return self.title


class Location(models.Model):
    state = models.CharField(max_length=255)
    image = models.ImageField(upload_to='locations/')

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.state


class CourseCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')

    class Meta:
        verbose_name = "Home Course Details"
        verbose_name_plural = "Home Course Details"

    def __str__(self):
        return self.title


class University(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='universities/')

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    rating = models.IntegerField()
    name = models.CharField(max_length=255)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/',null=True, blank=True)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    map_url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Branch Location"
        verbose_name_plural = "Branch Locations"

    def __str__(self):
        return f"{self.town}, {self.district}"



class Course(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name


class College(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    since = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(
        max_length=255,
        default='Private Medical College',
        blank=True
    )
    courses = models.ManyToManyField(Course)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='colleges/')
    image2 = models.ImageField(upload_to='colleges/', null=True, blank=True)
    image3 = models.ImageField(upload_to='colleges/' , null=True, blank=True)

    class Meta:
        verbose_name = "College"
        verbose_name_plural = "Colleges"
        ordering = ['name']

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.course}"
    
