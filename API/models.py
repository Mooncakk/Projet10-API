
from django.db import models

from SoftDesk import settings
from accounts.models import CustomUser


# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=[('back-end', 'Back-end'), ('front-end', 'Front-end'),
                                                    ('ios', 'iOS'), ('android', 'Android')])
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='project_author_id')
    user = models.ManyToManyField(CustomUser, through="Contributor")

    def __str__(self):
        return self.title


class Contributor(models.Model):

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='contributor_user_id')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                   related_name='contributor_project_id')
    permission = models.CharField(max_length=6, choices=[('True', 'Yes'), ('False', 'No')])
    role = models.CharField(max_length=50, choices=[('author', 'Author'), ('contributor', 'Contributor')])


class Issue(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=50, choices=[('bug', 'Bug'), ('task', 'Task'), ('improvement', 'Improvement')])
    priority = models.CharField(max_length=20, choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='project_id')
    status = models.CharField(max_length=20, choices=[('to do', 'To Do'), ('in progress', 'In Progress'), ('done', 'Done')], default='Open')
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       related_name='author_of_the_issue')
    assignee_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                         related_name='assigned_user_id', default=author_user)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):

    description = models.CharField(max_length=255)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='comment_author_id')
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
