# Generated by Django 3.0.7 on 2020-06-25 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0009_auto_20200625_0912'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ['created']},
        ),
    ]