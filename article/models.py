from django.db import models

class Article(models.Model):
    title          = models.CharField(max_length = 100)
    image_url      = models.URLField(max_length = 2000)
    created_date   = models.DateTimeField(blank=True)
    caption_date   = models.CharField(max_length = 50)
    caption        = models.CharField(max_length = 300)
    article_detail = models.OneToOneField('ArticleDetail', on_delete=models.CASCADE)

    category       = models.ManyToManyField('Category', through ='CategoryTagArticle')
    tag            = models.ManyToManyField('Tag', through ='CategoryTagArticle')

    class Meta:
        db_table = 'articles'

class ArticleDetail(models.Model):
    title        = models.CharField(max_length = 100)
    caption_date = models.CharField(max_length = 50)
    caption      = models.CharField(max_length = 200, null=True)
    description  = models.TextField()

    class Meta:
        db_table = 'article_details'

class Category(models.Model):
    name = models.CharField(max_length = 50)
    tag  = models.ManyToManyField('Tag', through ='CategoryTagArticle')

    class Meta:
        db_table = 'categories'

class Tag(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'tags'

class CategoryTagArticle(models.Model):
    article  = models.ForeignKey('Article', on_delete= models.SET_NULL, null=True)
    category = models.ForeignKey('Categorie', on_delete= models.SET_NULL, null=True)
    tag      = models.ForeignKey('Tag', on_delete= models.SET_NULL, null=True)

    class Meta:
        db_table = 'category_tag_articles'

class Video(models.Model):
    title            = models.CharField(max_length=100)
    date             = models.CharField(max_length=50)
    background_image = models.URLField(max_length=2500)
    category         = models.ForeignKey('Category', on_delete=models.SET_NULL, null= True)
    video_url        = models.URLField(max_length=2500)
    content          = models.CharField(max_length = 5000, null=True)

    class Meta:
        db_table = 'videos'
