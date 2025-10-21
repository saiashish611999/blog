from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
  categories = Category.objects.all()
  featured_posts = Blog.objects.filter(is_featured = True)
  print(featured_posts)
  context = {
    'categories':categories,
    'featured_posts':featured_posts
  }
  return render(request, "home.html", context)
