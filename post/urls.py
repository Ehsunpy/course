from . import views
from django.urls import path
app_name = 'post'  # اگر از namespace استفاده می‌کنید

urlpatterns = [
    path('wellcome/',view=views.Wellcome.as_view(),name='wellcome'),
    path('home/',view=views.Home.as_view(),name='home'),
    path('',view=views.listCourse.as_view(),name='lists'),
    path('<int:pk>/',view=views.Post_Detail.as_view(),name='post_detail')
    
    
]