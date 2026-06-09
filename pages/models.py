from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=50, default='✨')
    price = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Review(models.Model):
    author_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=5)
    text = models.TextField()
    source = models.CharField(max_length=100, default='Google')
    date = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.author_name} - {self.rating}★"

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    excerpt = models.CharField(max_length=500)
    content = models.TextField()
    meta_description = models.CharField(max_length=160, blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
