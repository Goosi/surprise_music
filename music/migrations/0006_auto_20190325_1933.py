# Generated by Django 2.1.7 on 2019-03-25 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20190325_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musichistory',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='music.MusicList'),
        ),
    ]