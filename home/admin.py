from django.contrib import admin
from home.models import Setting, ContactMessage
# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'status', 'update_at']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'status', 'update_at']
    readonly_fields = ('name', 'subject', 'email', 'message', 'ip')
    list_filter = ['status']

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
