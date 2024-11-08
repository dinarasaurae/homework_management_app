from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Homework)
admin.site.register(Subject)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['homework', 'student', 'submitted_text', 'submitted_at', 'grade']
    list_filter = ['homework', 'student']
    search_fields = ['student__username', 'homework__subject__name']
    readonly_fields = ['homework', 'student', 'submitted_text', 'submitted_at']

    def has_change_permission(self, request, obj=None):

        if request.user.role == 'teacher' or request.user.is_superuser:
            return True
        return False

admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Class)
