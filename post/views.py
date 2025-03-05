from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic

from .models import Video

class Wellcome(generic.TemplateView):
    template_name = 'post/wellcome.html'


class Home(generic.TemplateView):
    template_name = 'post/home.html'


class listCourse(generic.ListView):
    queryset = Video.objects.all()
    template_name = 'post/list-course.html'
    context_object_name = 'lists'
    
    
class Post_Detail(generic.DetailView):
    #  جای تابع زیر میتونا این مدل را نوشت
    model = Video
    template_name = 'post/about.html'
    context_object_name = 'lists'  
    
# def post_detail(request,pk): # pk:این  همون عددی که در urlمیگیره اینجا و  یو ار ال باید یکی باشه
#     posts= Video.objects.get(pk=pk)
#     context = {'posts': posts}
#     return render(request,  'posts/post_detail.html',context)

