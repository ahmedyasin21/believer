from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from videos.models import VideosModel
from django.views.generic import ListView,TemplateView
from django.utils import timezone
from django.contrib import auth 
from videos.models import VideosModel,VideosList
from notes.models import Notes
from quiz.models import Questions
from django.contrib.auth.models import User
# from django.shortcutes 

class HomeView( TemplateView):
    template_name = "base.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_count"] = Notes.objects.filter(author=self.request.user).count()
        context["quiz_count"] = Questions.objects.count()
        context["notes_count"] = Notes.objects.count()
        context["count"] = VideosModel.objects.count()
        return context

class Thanksbeingpart( TemplateView):
    template_name = "thankyoubeingpart.html"

class IndexView(TemplateView):
    template_name='index.html'
    
    

class AboutView(TemplateView):
    template_name = "about.html"
    # create_date = 2019-12-22
    # time = timezone.now()
    # day = create_date - timezone
    # if time > yer:
    #     yes 
    # else: 
    #     time

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["week"] = week
    #     return context
    


class TestPage(LoginRequiredMixin,TemplateView):
    login_url ='/accounts/login/'
    template_name = "test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_count"] = Notes.objects.filter(author=self.request.user).count()
        context["quiz_count"] = Questions.objects.count()
        context["notes_count"] = Notes.objects.count()
        context["count"] = VideosModel.objects.count()
        return context
    



        
 
class Todolist(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'test.html'
    paginate_by = 3
    def get_queryset(self):
        return Notes.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

    
    

class ThanksPage(TemplateView):
    template_name = "thanks.html"

class VideosView(TemplateView):
    template_name = "pages/videos.html"

# class VidosallListView(ListView):
#     model = VideosModel
#     template_name = "base/video_count.html"
#     context_object_name = 'videos_counts'  
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["count"] = VideosModel.objects.count()
#         return context
    
#     def get_queryset(self):
#         return VideosModel.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')

    