# Generated by Django 3.1.2 on 2020-11-15 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_auto_20201114_1911'),
        ('customer', '0003_auto_20201114_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='seat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='learning_logs.seat'),
            preserve_default=False,
        ),
    ]
