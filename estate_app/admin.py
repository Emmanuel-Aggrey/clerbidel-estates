from django.contrib import admin
from .models import Property,Propertytype,Agent,Gallary,Phone
# Register your models here.

class FlatPageAdmin(admin.ModelAdmin):
    list_display = ['created_by','name','price','property_type','location','sale_type','available','created_by']
    list_editable = ['available','price']
    list_display_links = ['created_by','name','location']
    prepopulated_fields = {"slug": ("location",)}

    fieldsets = (
        ('ALL PROPERTIIES', {
            'fields': ('property_type',('location','slug'),'description','sale_type','available','created_by','image','image1','image2','image3','image4')
        }),
        ('HOUSE OR BUILDING', {
            'classes':  ('wide', 'extrapretty'),
            'fields': ('name','price','bed', 'bath','sqrt',),
        }),
    )
admin.site.register(Property,FlatPageAdmin)

class PropertytypeAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Propertytype,PropertytypeAdmin)

class AgentAdmin(admin.ModelAdmin):
    list_display = ['name','position','facebook_url','linkedin_url','twitter_url','available']

admin.site.register(Agent,AgentAdmin)


admin.site.register(Gallary)

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['user','phonenumber',]
    list_editable = ['phonenumber',]



admin.site.register(Phone,PhoneAdmin)