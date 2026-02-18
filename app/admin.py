from django.contrib import admin
from django.utils.html import format_html
from .models import *


# =============================
# Banner Admin
# =============================
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'banner_image')
    search_fields = ('title',)
    ordering = ('title',)

    def banner_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" />', obj.image.url)
        return "-"
    banner_image.short_description = "Preview"


# =============================
# Location Admin
# =============================
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('state', 'location_image')

    def location_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return "-"
    location_image.short_description = "Preview"


# =============================
# Course Category Admin
# =============================
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_image')
    search_fields = ('title',)

    def category_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return "-"
    category_image.short_description = "Preview"


# =============================
# University Admin
# =============================
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'university_logo')
    search_fields = ('name',)

    def university_logo(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return "-"
    university_logo.short_description = "Logo"


# =============================
# Testimonial Admin
# =============================
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'photo')
    list_filter = ('rating',)
    search_fields = ('name',)

    def photo(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return "-"
    photo.short_description = "Photo"


# =============================
# Branch Location Admin
# =============================
@admin.register(Branch)
class BranchLocationAdmin(admin.ModelAdmin):
    list_display = ('town', 'district', 'map_url')
    search_fields = ('town', 'district')


# =============================
# Course Admin
# =============================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# =============================
# College Admin (Advanced)
# =============================
@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type', 'image_preview')
    list_filter = ('location', 'type')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ('courses',)

    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "slug", "description", "since", "type")
        }),
        ("Courses & Location", {
            "fields": ("courses", "location")
        }),
        ("Images", {
            "fields": ("image1", "image2", "image3")
        }),
    )

    def image_preview(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="70" />', obj.image1.url)
        return "-"
    image_preview.short_description = "Preview"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'course', 'location', 'created_at')
    search_fields = ('name', 'phone', 'course')
    list_filter = ('location', 'created_at')

