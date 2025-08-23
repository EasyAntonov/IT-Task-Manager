from django.urls import path

from task_manager.views import index, TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, \
    CompletedTaskListView, UserTaskListView, WorkerListView, WorkerDetailView, WorkerCreateView, WorkerUpdateView, \
    WorkerDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("completed-tasks/", CompletedTaskListView.as_view(), name="completed-task-list"),
    path("tasks/assigned", UserTaskListView.as_view(), name="user-tasks"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
]