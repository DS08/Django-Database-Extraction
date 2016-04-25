
##Created Superuser 
## user: scholfin
## password = deepak123
## this same user has been used in login page as well

## if the Registration is done It creates the user iin database too


from django.contrib import admin

# Register your models here.

from app1.models import Scholarship

class ScholarshipAdmin(admin.ModelAdmin):
	list_display = ('name','amount_in_rupees','deadline','created','procedure','eligibility')
admin.site.register(Scholarship,ScholarshipAdmin)