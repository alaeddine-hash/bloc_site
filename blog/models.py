from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
   
class PublishedManager(models.Manager):
       def get_queryset(self):
           return super().get_queryset()\
           .filter(status=Post.STATUS_CHOICES.PUBLISHED)
class Post(models.Model):
   
   STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('PUBLISHED', 'Published'),
    )
   
   title=models.CharField(max_length=250)
   slug=models.SlugField(max_length=250)
   body=models.TextField(default="", blank=True)
   publish = models.DateField(default=timezone.now())
   created = models.DateField(auto_now_add=True)
   update = models.DateField(auto_now=True)
   status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
   
   # Clé étrangère pour associer l'article à un utilisateur
   author = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='blog_posts')

   objects = models.Manager()
   published = PublishedManager()
    
   class Meta:
        ordering = ['-publish']
        indexes = [
             models.Index(fields=['-publish']),
        ]

   def __str__(self):
        return self.title
   

