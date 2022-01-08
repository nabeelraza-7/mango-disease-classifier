import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
print(os.getcwd())
from script import predict_class

def index(request):
    return render(request, "classify_pest/index.html")

def about(request):
    return render(request, "classify_pest/about.html")

def classify_here(request):
    if request.method == "POST" and len(request.FILES) != 0:
        uploaded_file = request.FILES['image_file']
        fs = FileSystemStorage()
        # deleting image.jpeg if already exists
        if os.path.exists('media/image.jpeg'):
            os.remove("media/image.jpeg")
        fs.save("media/image.jpeg", uploaded_file)
        print(predict_class("media/image.jpeg"))
    return render(request, "classify_pest/classify.html")