# Generated by Django 3.1.2 on 2020-11-30 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_delete_seatlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='section',
            field=models.CharField(max_length=50, null=True),
        ),
    ]