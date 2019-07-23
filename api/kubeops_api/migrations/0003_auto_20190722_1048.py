# Generated by Django 2.1.2 on 2019-07-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0002_auto_20190722_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='created_by',
        ),
        migrations.AddField(
            model_name='storage',
            name='comment',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Comment'),
        ),
    ]