from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.






class Project(models.Model):
    projectPrority = models.IntegerField(blank=True, null=True)
    postCreator = models.CharField(max_length=200)
    projectTitle = models.CharField(max_length=200)
    projectDescriptions = models.TextField(blank=True, null=True)
    projectBody = RichTextUploadingField(blank=True, null=True)
    projectVideoUrl = models.TextField(blank=True)
    projectViews = models.IntegerField(default=0)
    projectTimeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    projectImage =  models.ImageField(blank=False, null=False)


    def get_photo_url(self):
        if self.projectImage and hasattr(self.projectImage, 'url'):
            return self.projectImage.url
        else:
            return "/static/no-logo.jpg"

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)
    reply = models.BooleanField(default=False)

class MySelf(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)

class Skill(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)

class Education(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)   

class Testimonial(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)

class Exprience(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True) 

class Achievement(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)  

class Certificate(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextUploadingField(blank=True, null=True)  

class CV(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    cv = models.FileField()    