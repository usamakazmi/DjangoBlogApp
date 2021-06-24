from django.urls import path
from .  import views
from .views import ArticleDetailView, AddPostView, UpdatePostView, DeletePostView,AddCategoryView, CategoryView
#HomeView, 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    
    #path('', HomeView.as_view(), name="home"),

    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete-post"),
    path('category/<str:cats>/', CategoryView, name="category"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('addsent/', views.addsent, name="addsent"),

    path('pie-chart/', views.pie_chart, name='pie-chart'),
    path('population-chart/', views.population_chart, name='population-chart'),
    path('line-chart/', views.line_chart, name='line-chart'),
    
    
    path('startanalysis/', views.startanalysis, name="startanalysis"),
    
    path('facebook/', views.facebook, name="facebook"),
    path('youtube/', views.youtube, name="youtube"),
    path('twitter/', views.twitter, name="twitter"),
   
    path('uploadfile/', views.uploadfile, name="uploadfile"),
    path('logout_view/', views.logout_view, name="logout_view"),
    path('single/', views.single, name="single"),
    
    
   
    #path('population-chart/', views.population_chart, name='population-chart'),
]
