from django.contrib import admin
from .models import listing



class listingAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','list_date','realtor')
    list_display_links=('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','city','address',)
    list_per_page = 10


admin.site.register(listing,listingAdmin)