# Generated by Django 2.1.5 on 2019-01-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_center_monitor', '0002_add_application_process_report_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationprocess',
            name='recommendation',
            field=models.CharField(default='adasd', max_length=225),
            preserve_default=False,
        ),
    ]