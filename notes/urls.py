from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/', views.NoteListView.as_view(), name='notes_list'), # 3rd argument is used to name the url
    path('notes/<int:pk>/', views.NoteDetailView.as_view(), name='notes_detail'),
    path('', views.NoteWelcomeView.as_view(), name='index'),
    path('notes/create/', views.NoteCreateView.as_view(), name='notes_create'),
    path('notes/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='notes_update'),
    path('notes/<int:pk>/delete/', views.NoteDeleteView.as_view(), name='notes_delete'),
    path('login/', views.NoteLoginView.as_view(), name='login'),
    path('logout/', views.NoteLogoutView.as_view(), name='logout'),
    path('signup/', views.NoteSignupView.as_view(), name='signup'),
]
