from django.contrib import admin
from .models import Announcement, LeadershipMember, LeadershipPosition

# Register your models here.
admin.site.register(Announcement)

@admin.register(LeadershipPosition)
class LeadershipPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'display_order')
    ordering = ['display_order']

@admin.register(LeadershipMember)
class LeadershipMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('position',)
