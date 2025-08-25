from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import Worker, Task, Team, Project, Tag, TaskType, Position


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("email", "position", "team")
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position", "team",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                       "position",
                        "team",
                    )
                },
            ),
        )
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "priority", "deadline", "is_completed")
    list_filter = ("priority", "deadline", "is_completed")
    search_fields = ("name", "description")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")
    filter_horizontal = ("teams",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
