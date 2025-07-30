from django.shortcuts import render, redirect

from cerita5.forms import CourseForm
from cerita5.models import Course


# Create your views here.
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_course')


    else:
        form = CourseForm(request.POST)

    return render(request, 'Add-Course.html', {'form': form})


def detail_all_course(request):
    course = Course.objects.all()
    context = {'all_course': course}

    return render(request, 'List-AllCourse.html', context)


def detail_course(request, code):
    course = Course.objects.get(code=code)

    context = {
        'course': course
    }

    return render(request, 'Detail-Course.html', context)


def edit_course(request, code):
    return render(request, 'Edit-Course.html')


def remove_course(request):
    context = {}

    if request.method == 'POST':
        obj = Course.objects.get(code=request.POST['code_dan_name_matkul'])
        obj.delete()
        course_list = Course.objects.all()
        context['course_list'] = course_list
        context['success'] = True

        return render(request, 'Delete-Course.html', context)

    else:
        course_list = Course.objects.all()
        context['course_list'] = course_list
        return render(request, 'Delete-Course.html', context)
