from django.contrib import admin
from django.contrib.auth.models import Group, User
from . models import TodoList, Managers, Products, Departments, Profile
from member.models import CustomUser, CustomUserManager


# Unregister Models Here.
admin.site.unregister(Group)

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = CustomUser
    # fields = ['username']
    inlines = [ProfileInline]


# Register User
admin.site.register(CustomUser, UserAdmin)


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'status', 'date_created', 'due_date',)
    search_fields = ('name', 'status', 'date_created', 'due_date',)
    list_filter = ('status', 'date_created', 'due_date',)
    ordering = ('name',)


admin.site.register(Managers)
admin.site.register(Products)
admin.site.register(Departments)
# admin.site.register(Profile)
