# Generated by Django 2.1.7 on 2019-03-07 03:43

from django.db import migrations, models
import django.db.models.deletion
import uuid
import web.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('kind', models.CharField(choices=[('dog', 'Dog')], default='dog', max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('not_identified', 'Not Identified')], max_length=32)),
                ('kind', models.CharField(choices=[('dog', 'Dog')], default='dog', max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
                ('breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='pet.Breed')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_file_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('image', models.ImageField(upload_to=web.utils.UploadToFactory('pet/picture/image'))),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'ordering': ('date_changed',),
            },
        ),
        migrations.AddField(
            model_name='pet',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet.Picture'),
        ),
        migrations.AddField(
            model_name='pet',
            name='pictures',
            field=models.ManyToManyField(blank=True, related_name='pets', to='pet.Picture'),
        ),
    ]
