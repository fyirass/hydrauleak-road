from django.contrib import admin
from .models import Intervention

class InterventionAdmin(admin.ModelAdmin):
    intervention_display = ('id', 'intervention_title', 'is_published', 'intervention_status', 'intervention_date', 'client')
    intervention_display_display_links = ('id', 'intervention_title')
    intervention_display_filter = ('client', )
    intervention_display_editable = ('is_published', )
    search_fields = ('intervention_title', 'intervention_description', 'address', 'city', 'state', 'zipcode', 'intervention_status')
    intervention_display_per_page = 25

admin.site.register(Intervention, InterventionAdmin)
 