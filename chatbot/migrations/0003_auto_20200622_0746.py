# Generated by Django 3.0.7 on 2020-06-22 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_auto_20200622_0604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatbot',
            name='background_picture',
        ),
        migrations.AddField(
            model_name='chatbot',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=256),
            preserve_default=False,
        ),
    ]
