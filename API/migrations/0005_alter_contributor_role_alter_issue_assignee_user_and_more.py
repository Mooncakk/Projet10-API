# Generated by Django 4.2.7 on 2023-11-19 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0004_project_user_alter_contributor_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='role',
            field=models.CharField(choices=[('author', 'Author'), ('contributor', 'Contributor')], max_length=50),
        ),
        migrations.AlterField(
            model_name='issue',
            name='assignee_user',
            field=models.ForeignKey(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_of_the_issue', to=settings.AUTH_USER_MODEL), on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('to do', 'To Do'), ('in progress', 'In Progress'), ('done', 'Done')], default='Open', max_length=20),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tag',
            field=models.CharField(choices=[('bug', 'Bug'), ('task', 'Task'), ('improvement', 'Improvement')], max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('back-end', 'Back-end'), ('front-end', 'Front-end'), ('ios', 'iOS'), ('android', 'Android')], max_length=50),
        ),
    ]
