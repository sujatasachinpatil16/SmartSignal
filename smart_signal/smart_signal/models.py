from django.db import models
from django.contrib.auth.models import User

class CompanyDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=264)
    company_url = models.URLField(blank=True)
    company_logo = models.ImageField(upload_to='company_logo',blank=True)
    contact_details = models.CharField(max_length=12)

    def __str__(self):
        return self.company_name

class SignalDetails(models.Model):
    company_name = models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    junction_name = models.CharField(max_length=264)
    no_of_crossings = models.PositiveSmallIntegerField(default=2)

    def __str__(self):
        return self.junction_name

class VideoDetails(models.Model):
    #company_name = models.OneToOneField(CompanyDetails,on_delete=models.CASCADE)
    junction_name = models.ForeignKey(SignalDetails,on_delete=models.CASCADE)
    created_on = models.DateTimeField()
    size_of_video = models.IntegerField(default = 0)
    video_title = models.CharField(max_length = 200)
    video_duration = models.CharField(max_length=264)
    subscription_period = models.IntegerField(default = 0)
    priority = models.CharField(max_length=20)
    priority_timings = models.CharField(max_length=20)

    def __str__(self):
        return self.video_title
