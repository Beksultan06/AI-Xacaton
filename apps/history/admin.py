from django.contrib import admin
from apps.history.models import Daily, Weekly, History

@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description',  'user', 'date']
    list_filter = ['id', 'title', 'description',  'user', 'date']
    search_fields = ['id', 'title', 'description',  'user', 'date']

@admin.register(Weekly)
class WeeklyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'date']
    list_filter = ['user', 'date']
    search_fields = ['id', 'title', 'user__username', 'date']


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_day', 'title_week']
    list_filter = ['id', 'title_day', 'title_week']
    search_fields = ['id', 'title_day__title', 'title_week__title']
    
    def title_day(self, obj):
        return obj.title_day.title if obj.title_day else None
    title_day.admin_order_field = 'title_day__title'
    title_day.short_description = 'Title Day'

    def title_week(self, obj):
        return obj.title_week.title if obj.title_week else None
    title_week.admin_order_field = 'title_week__title'
    title_week.short_description = 'Title Week'
