from django.contrib import admin
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'is_active', 'start_date', 'end_date')
    list_filter = ('is_active', 'plan', 'start_date')
    search_fields = ('user__username', 'plan')
    ordering = ('-start_date',)

admin.site.register(Subscription, SubscriptionAdmin)
