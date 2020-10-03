from django.contrib import admin
from accounts.models import UserProfile,Contact


class NameingAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = UserProfile

admin.site.register(UserProfile,NameingAdmin)
admin.site.register(Contact)


# Register your models here.
