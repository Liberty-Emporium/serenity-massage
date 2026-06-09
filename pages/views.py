from django.shortcuts import render, get_object_or_404
from .models import Service, Review, BlogPost

def home(request):
    featured_services = Service.objects.filter(is_featured=True)[:4]
    featured_reviews = Review.objects.filter(is_featured=True)[:3]
    recent_posts = BlogPost.objects.filter(published=True)[:3]
    return render(request, 'pages/home.html', {
        'featured_services': featured_services,
        'featured_reviews': featured_reviews,
        'recent_posts': recent_posts,
    })

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    services_list = Service.objects.all()
    return render(request, 'pages/services.html', {'services': services_list})

def red_light_therapy(request):
    return render(request, 'pages/red_light_therapy.html')

def reviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'pages/reviews.html', {'reviews': reviews_list})

def contact(request):
    return render(request, 'pages/contact.html')

def blog(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'pages/blog.html', {'posts': posts})

def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, 'pages/blog_post.html', {'post': post})
