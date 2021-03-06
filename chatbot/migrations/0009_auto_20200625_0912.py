# Generated by Django 3.0.7 on 2020-06-25 09:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatbot', '0008_auto_20200625_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='consumer',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('user', 'consumer')},
        ),
    ]
