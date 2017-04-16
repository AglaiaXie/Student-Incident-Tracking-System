from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from ed4all.models import Course, Review

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['Course_Name', 'Ranking']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review']

def home(request, template_name='ed4all/home.html'):
    courses = Course.objects.all()
    ctx = {}
    ctx['courses'] = courses
    return render(request, template_name, ctx)


def course_view(request, pk, template_name='ed4all/course_view.html'):
    course = get_object_or_404(Course, pk=pk)
    reviews = Review.objects.filter(course=course)
    ctx = {}
    ctx["courses"] = course
    ctx["reviews"] = reviews
    return render(request, template_name, ctx)

def course_create(request, template_name='ed4all/course_form.html'):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('ed4all:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)

def course_update(request, pk, template_name='ed4all/course_form.html'):
    course= get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('ed4all:home')
    ctx = {}
    ctx["form"] = form
    ctx["course"] = course
    return render(request, template_name, ctx)

def course_delete(request, pk, template_name='ed4all/course_confirm_delete.html'):
    course= get_object_or_404(Course, pk=pk)
    if request.method=='POST':
        course.delete()
        return redirect('ed4all:home')
    ctx = {}
    ctx["object"] = course
    ctx["book"] = course
    return render(request, template_name, ctx)


def review_create(request, parent_pk, template_name='books_pc_multi_view/review_form.html'):
    book = get_object_or_404(Course, pk=parent_pk)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.save()
        return redirect('books_pc_multi_view:book_view', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["book"] = book
    return render(request, template_name, ctx)

def review_update(request, pk, template_name='ed4all/review_form.html'):
    review = get_object_or_404(Review, pk=pk)
    parent_pk = review.course.pk
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('ed4all:course_view', parent_pk)
    ctx = {}
    ctx["form"] = form
    ctx["course"] = review.course
    return render(request, template_name, ctx)

def review_delete(request, pk, template_name='ed4all/review_confirm_delete.html'):
    review = get_object_or_404(Review, pk=pk)
    parent_pk = review.course.pk
    if request.method=='POST':
        review.delete()
        return redirect('ed4all:course_view', parent_pk)
    ctx = {}
    ctx["object"] = review
    ctx["course"] = review.course
    return render(request, template_name, ctx)