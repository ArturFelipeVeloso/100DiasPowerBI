# Generated by Django 3.0.7 on 2020-06-06 02:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subTitle', models.CharField(max_length=200)),
                ('aulaNumber', models.IntegerField()),
                ('video', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('publicado', models.DateTimeField(default=datetime.datetime(2020, 6, 6, 2, 27, 7, 532187, tzinfo=utc))),
                ('cadastrado', models.DateTimeField(auto_now_add=True)),
                ('alterado', models.DateTimeField(auto_now=True)),
                ('ativado', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]