# Generated by Django 3.1.2 on 2020-10-27 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_entry_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='menu_media'),
        ),
    ]
