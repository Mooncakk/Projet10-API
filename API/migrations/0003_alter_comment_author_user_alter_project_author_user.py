# Generated by Django 4.2.7 on 2023-11-19 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0002_alter_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='author_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_auhtor_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
