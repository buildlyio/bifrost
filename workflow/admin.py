from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import (CoreUser, CoreGroup, Role, Organization, WorkflowLevel1, WorkflowLevel2,
                     WorkflowLevel2Sort, WorkflowTeam, EmailTemplate)


class WorkflowTeamAdmin(admin.ModelAdmin):
    list_display = ('workflow_user', 'workflowlevel1')
    display = 'Workflow Team'
    search_fields = ('workflow_user__user__username', 'workflowlevel1__name',
                     'workflow_user__user__last_name')
    list_filter = ('create_date',)


class CoreSitesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    display = 'Core Site'
    list_filter = ('name',)
    search_fields = ('name',)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'edit_date')
    display = 'Organization'


class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'edit_date')
    display = 'Milestone'


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    display = 'Role'
    search_fields = ('role',)


class CoreGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization')
    display = 'Core Group'
    list_filter = ('organization',)
    search_fields = ('name', 'organization__name')


class CoreUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'is_active')
    display = 'Core User'
    list_filter = ('user__is_staff', 'organization')
    search_fields = ('user__first_name', 'title')


class WorkflowLevel1Admin(admin.ModelAdmin):
    list_display = ('name',)
    display = 'Workflow Level1'
    list_filter = ('name',)
    search_fields = ('name',)


class WorkflowLevel2Admin(admin.ModelAdmin):
    list_display = ('name',)
    display = 'Workflow Level1'
    list_filter = ('name',)
    search_fields = ('name',)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'edit_date')
    display = 'Portfolio'
    list_filter = ('create_date',)
    search_fields = ('name',)


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('organization', 'type')
    display = 'Email Template'


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(WorkflowLevel2, SimpleHistoryAdmin)
admin.site.register(WorkflowLevel1, SimpleHistoryAdmin)
admin.site.register(WorkflowLevel2Sort)
admin.site.register(WorkflowTeam, WorkflowTeamAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(CoreGroup, CoreGroupAdmin)
admin.site.register(CoreUser, CoreUserAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
