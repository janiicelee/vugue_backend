from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'category'

class SubCategories(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'subcategory'

class Video(models.Model):
    title = models.CharField(max_length = 50)
    date  = models.CharField(max_length = 50)
    background_image = models.URLField(max_length = 2500)
    category = models.ForeignKey( Categories, on_delete=models.SET_NULL, null=True)
    video_url = models.URLField(max_length = 2500)
    content  = models.CharField(max_length = 1000)

    class Meta:
        db_table = 'videos'
