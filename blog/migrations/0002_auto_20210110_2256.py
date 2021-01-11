# Generated by Django 3.0.5 on 2021-01-11 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='imag2',
            field=models.ImageField(default='posts/default.jpg', upload_to='posts/'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]