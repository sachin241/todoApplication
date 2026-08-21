from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="list"),
    path("tasks/new/", views.task_create, name="create"),
    path("tasks/<int:pk>/edit/", views.task_edit, name="edit"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="delete"),
    path("tasks/<int:pk>/toggle/", views.task_toggle, name="toggle"),
    path("calendar/", views.calendar_view, name="calendar"),
    path("api/calendar-events/", views.calendar_events, name="calendar_events"),
    path("export/", views.export_tasks, name="export"),
    path("import/", views.import_tasks, name="import"),
]
