# Generated by Django 3.2.6 on 2021-08-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0002_alter_genre_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='delete_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]