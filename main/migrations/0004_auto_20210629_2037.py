# Generated by Django 2.2 on 2021-06-30 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210610_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consignment',
            name='itemImages',
            field=models.ImageField(blank=True, upload_to='upload_images/'),
        ),
        migrations.AlterField(
            model_name='junkremoval',
            name='itemImages',
            field=models.ImageField(blank=True, upload_to='upload_images/'),
        ),
        migrations.AlterField(
            model_name='moving',
            name='itemImages',
            field=models.ImageField(blank=True, upload_to='upload_images/'),
        ),
    ]
