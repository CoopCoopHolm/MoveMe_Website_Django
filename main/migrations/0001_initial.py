# Generated by Django 2.2 on 2021-06-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('itemAddress', models.CharField(max_length=1024)),
                ('moveDateTime', models.DateTimeField()),
                ('itemImages', models.ImageField(blank=True, upload_to='<django.db.models.fields.CharField>_images/')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='JunkRemoval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('itemAddress', models.CharField(max_length=1024)),
                ('moveDateTime', models.DateTimeField()),
                ('itemImages', models.ImageField(blank=True, upload_to='<django.db.models.fields.CharField>_images/')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Moving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('currentAddress', models.CharField(max_length=1024)),
                ('movingAddress', models.CharField(max_length=1024)),
                ('moveDateTime', models.DateTimeField()),
                ('itemImages', models.ImageField(blank=True, upload_to='<django.db.models.fields.CharField>_images/')),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]