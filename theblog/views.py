from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Sum
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, City, Country
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# detail is 1, list is all
# Create your views here.

#def home(request):
#    return render(request,'home.html', {})
def line_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    #return JsonResponse(data={
    #    'labels': labels,
    #    'data': data,
    #})
    return render(request, 'line_chart.html', {
        'labels': labels,
        'data': data,
    })

def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by('-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])
    
    #return JsonResponse(data={
    #    'labels': labels,
    #    'data': data,
    #})
    return render(request, 'population_chart.html', {
        'labels': labels,
        'data': data,
    })


def pie_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'pie_chart.html', {
        'labels': labels,
        'data': data,
    })

def dashboard(request):
    return render(request,'dashboard.html', {})


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    #ordering = ['-id']
    ordering = ['-post_date']

    #def get_context_date(self, *args, **kwargs):


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request,'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts' :category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    #fields = "__all__"
    #fields = ('title', 'body')

class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = "add_category.html"
    fields = "__all__"
    #fields = ('title', 'body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
   
    template_name = 'update_post.html'
    #fields = ('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')