from django.shortcuts import render

def runoob(request):
    views_dict = {"name":"text"}
    return render(request, "runoob.html", {"views_dict": views_dict})