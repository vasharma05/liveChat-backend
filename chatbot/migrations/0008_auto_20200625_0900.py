# Generated by Django 3.0.7 on 2020-06-25 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_auto_20200625_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chatbot.Room'),
        ),
    ]