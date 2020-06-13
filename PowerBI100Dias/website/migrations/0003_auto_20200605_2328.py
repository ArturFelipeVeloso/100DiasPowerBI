# Generated by Django 3.0.7 on 2020-06-06 02:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_auto_20200605_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aula',
            name='publicado',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 2, 28, 48, 474745, tzinfo=utc)),
        ),
    ]
