from django.urls import path 
from . import views

app_name = 'notes'

urlpatterns = [
    path ('create/',views.NotesCreateView.as_view(),name = 'notes_create'),
    path ('detail/<int:pk>',views.NotesDetailView.as_view(),name = 'notes_detail'),
    path('list/<str:username>',views.NotesListView.as_view(),name='notes_list'),
    path('delete/<int:pk>',views.NotesDeleteView.as_view(),name='notes_delete'),
    path('update/<int:pk>',views.NotesUpdateView.as_view(),name ='notes_update'),
]
