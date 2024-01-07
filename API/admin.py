from django.contrib import admin

from .models import Project, Contributor, Issue, Comment

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):

    fields = ['author_user', 'title', 'description', 'type']
    list_display = ['project_id', 'title', 'description', 'author_user', 'type']


admin.site.register(Project, ProjectAdmin)


class ContributorsAdmin(admin.ModelAdmin):

    fields = ['user', 'project', 'permission', 'role']
    list_display = ['user', 'project', 'permission', 'role']


admin.site.register(Contributor, ContributorsAdmin)


class IssuesAdmin(admin.ModelAdmin):

    fields = ['title', 'description', 'tag', 'priority', 'project', 'status', 'author_user', 'assignee_user']
    list_display = ['title', 'description', 'tag', 'priority', 'project', 'status', 'author_user', 'assignee_user',
                    'created_time']


admin.site.register(Issue, IssuesAdmin)


class CommentsAdmin(admin.ModelAdmin):

    fields = ['author_user', 'issue', 'description']
    list_display = ['author_user', 'issue', 'description', 'created_time']


admin.site.register(Comment, CommentsAdmin)
