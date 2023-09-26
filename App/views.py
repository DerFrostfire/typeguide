from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import os
from django import template

register = template.Library()

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    if is_ajax(request):
        ts_code = request.POST.get("ts_code")
        with open("temp.ts", "w") as f:
            f.write(ts_code)
        print(ts_code)
        ts_file_path = 'C:/Users/Дмитрий/Desktop/univer/mk/TypeGuide/temp.ts'
        js_file_path = 'C:/Users/Дмитрий/Desktop/univer/mk/TypeGuide/temp.js'
        command = f"npx tsc {ts_file_path} --outFile {js_file_path}"
        os.system(command)
        with open("temp.js", "r") as f:
            js_code = f.read()
        print(js_code)
        return HttpResponse(js_code, content_type="application/html")
    context = {
       "Modules": Module.objects.all()
    }
    return render(request, "App/index.html", context)

def lesson(request, id):
    context = {
       "lesson": Lesson.objects.get(id = id)
    }

    return render(request, "App/lesson.html", context)
