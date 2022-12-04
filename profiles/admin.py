from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from . models import UserProfile
# Register your models here.

class UserAdminConfig(UserAdmin):
    model = UserProfile
    search_fields = ('email', 'user_name', 'first_name', 'examNo','exam_yr',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff',
                    'examNo','exam_yr',)
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name', 'start_date',
                    'is_active', 'is_staff','examNo','exam_yr',)
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name','start_date',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('examNo','exam_yr','points',)}),
    )
    # formfield_overrides = {
    #     UserProfile.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 
            'is_active', 'is_staff', 'examNo','exam_yr')}
         ),
    )
    
    

admin.site.register(UserProfile, UserAdminConfig)