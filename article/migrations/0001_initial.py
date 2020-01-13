# Generated by Django 3.0.1 on 2020-01-12 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('caption_date', models.CharField(max_length=50)),
                ('caption', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'article_detail',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img_url', models.URLField(max_length=2000)),
                ('created_date', models.DateTimeField(blank=True)),
                ('caption_date', models.CharField(max_length=50)),
                ('article_detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='article.ArticleDetails')),
            ],
            options={
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
                ('background_image', models.URLField(max_length=2500)),
                ('video_url', models.URLField(max_length=2500)),
                ('content', models.CharField(max_length=5000, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Categories')),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='CategoryTagArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Articles')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Categories')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Tags')),
            ],
            options={
                'db_table': 'category_tag_articles',
            },
        ),
        migrations.AddField(
            model_name='categories',
            name='tag',
            field=models.ManyToManyField(through='article.CategoryTagArticles', to='article.Tags'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(through='article.CategoryTagArticles', to='article.Categories'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tag',
            field=models.ManyToManyField(through='article.CategoryTagArticles', to='article.Tags'),
        ),
    ]