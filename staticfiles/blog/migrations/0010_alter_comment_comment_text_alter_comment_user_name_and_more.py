# Generated by Django 5.0.2 on 2024-03-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]