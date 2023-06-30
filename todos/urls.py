from django.urls import path
from todos.views import index, task_all, task_toggle, task_edit, task_eliminar

urlpatterns = [
    path("", index),
    path("task.json", task_all),
    path("task/<int:task_id>/toggle.json", task_toggle),
    path("task/<int:task_id>/edit.json", task_edit),
    path("task/<int:task_id>/eliminar.json", task_eliminar)

   
]

