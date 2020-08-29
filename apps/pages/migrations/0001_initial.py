# Generated by Django 3.1 on 2020-08-29 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, unique=True, verbose_name='Titlu')),
                ('text', models.TextField(max_length=10000000, verbose_name='Fulltext')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(blank=True, related_name='contents_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
