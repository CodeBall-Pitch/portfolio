from django.contrib import admin
from .models import Portfolio,About,Services,Skills,Contact,Education
# Register your models here.


admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin Area"
admin.site.index_title = "Welcome to the Portfolio Admin Area"

class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ["title","image","description","url"]
    list_display_links = ["title"]
    list_filter = ["title"]
    search_fields = ["title","description"]
    class Meta:
        model = Portfolio
        
admin.site.register(Portfolio,PortfolioModelAdmin)
admin.site.register(About,PortfolioModelAdmin)
admin.site.register(Services,PortfolioModelAdmin)
admin.site.register(Skills,PortfolioModelAdmin)
admin.site.register(Contact,PortfolioModelAdmin)
admin.site.register(Education,PortfolioModelAdmin)
    