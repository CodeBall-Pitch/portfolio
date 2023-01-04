from django.contrib import admin
from .models import Portfolio,About,Services,Skills,Contact,Education
# Register your models here.


admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Area"
admin.site.index_title = "Welcome to the Portfolio Admin Area"

        
admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Skills)
admin.site.register(Contact)
admin.site.register(Education)

