# Generated by Django 2.1.7 on 2019-03-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=1000, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='web/banner/picture')),
                ('button_one', models.CharField(blank=True, max_length=32, null=True)),
                ('button_two', models.CharField(blank=True, max_length=32, null=True)),
                ('button_one_link', models.URLField(blank=True, null=True)),
                ('button_two_link', models.URLField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'ordering': ('date_changed',),
            },
        ),
    ]
