# Generated by Django 5.0.2 on 2024-04-25 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0015_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='playlists',
            field=models.ManyToManyField(related_name='songs', to='music.playlist'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='description',
            field=models.TextField(),
        ),
    ]
