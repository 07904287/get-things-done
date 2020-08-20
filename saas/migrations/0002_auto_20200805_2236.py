# Generated by Django 3.0.8 on 2020-08-05 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number_of_cookies',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=180)),
                ('deadline', models.DateTimeField(blank=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('attachment', models.FileField(blank=True, upload_to='')),
                ('percentage_done', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Snoozed', 'Snoozed'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Active', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
