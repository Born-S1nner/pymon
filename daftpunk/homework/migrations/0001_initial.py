# Generated by Django 3.2.2 on 2021-05-11 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('composer', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SoundBass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insturment', models.CharField(max_length=300)),
                ('tempo', models.IntegerField(default=0)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.song')),
            ],
        ),
    ]
