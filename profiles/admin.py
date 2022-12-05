from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from . models import UserProfile
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = UserProfile
    search_fields = ('email', 'user_name', 'first_name', )
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'start_date','is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','start_date',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('points',)}),
    )
    # formfield_overrides = {
    #     UserProfile.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 
            'is_active', 'is_staff', )}
         ),
    )
    
    

admin.site.register(UserProfile, UserAdminConfig)