from django.contrib import admin

from milestones.models import ProjectsTable, MilestonesTable

# Register your models here.
admin.site.register(ProjectsTable)
admin.site.register(MilestonesTable)
