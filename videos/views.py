from django.shortcuts import render,get_object_or_404
from videos.models import VideosList,VideosModel
from django.utils import timezone
from django.views.generic import ListView ,DetailView ,TemplateView
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

class VideosListView(LoginRequiredMixin,ListView):
    model = VideosList
    context_object_name = 'videos_lists'  
    template_name = "videos/videos_lists.html"

    def get_queryset(self):
        return VideosList.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')





class VideosModelListView(LoginRequiredMixin,ListView):
    model = VideosModel
    template_name = "videos/list_videos.html"
    context_object_name = 'videos_list'  

    def get_queryset(self,*args, **kwargs):
        videoslist = get_object_or_404(VideosList, list_title=self.kwargs.get('list_title'))
        return VideosModel.objects.filter(videos_lists=videoslist).order_by('-create_date')


# class VideosModelDetailView(DetailView):
#     model = VideosModel
#     template_name = "VideosList/videos_detail.html"
#     context_object_name = 'videos_lists' 
#     def get_queryset(self):
#         return VideosModel.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')
