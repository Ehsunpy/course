from django.shortcuts import render
from django.views import generic

from .models import Video

class listCourse(generic.ListView):
    queryset = Video.objects.all()
    template_name = 'post/list-course.html'
    context_object_name = 'lists'
    
    
class Post_Detail(generic.DetailView):
    #  جای تابع زیر میتونا این مدل را نوشت
    model = Video
    template_name = 'post/post_detail.html'
    context_object_name = 'lists'  
    
# def post_detail(request,pk): # pk:این  همون عددی که در urlمیگیره اینجا و  یو ار ال باید یکی باشه
#     posts= Video.objects.get(pk=pk)
#     context = {'posts': posts}
#     return render(request,  'posts/post_detail.html',context)

