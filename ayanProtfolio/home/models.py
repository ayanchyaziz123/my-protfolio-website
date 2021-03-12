from django.db import models

# Create your models here.






class Project(models.Model):
    postCreator = models.CharField(max_length=200)
    projectTitle = models.CharField(max_length=200)
    projectDescriptions = models.TextField()
    projectVideoUrl = models.TextField(blank=True)
    projectGithubUrl = models.TextField(blank=True)
    projectImage = models.ImageField(blank=True, null=True)
    projectViews = models.IntegerField(default=0)
    projectTimeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)


    def get_photo_url(self):
        if self.projectImage and hasattr(self.projectImage, 'url'):
            return self.projectImage.url
        else:
            return "/static/no-logo.jpg"