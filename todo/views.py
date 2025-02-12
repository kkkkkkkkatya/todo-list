from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, get_object_or_404

from todo.forms import TaskForm
from todo.models import Task, Tag


class TaskListView(generic.ListView):
    """View class for home/tasks page."""
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "task_list"
    paginate_by = 2


def toggle_task_status(request, pk):
    """View funktion for task is_done status."""
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:task-list")


class TaskCreateView(generic.CreateView):
    """View class for task create page."""
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    """View class for task update page."""
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    """View class for task confirm deletion page."""
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    """View class for tags page."""
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tag_list"
    paginate_by = 6


class TagCreateView(generic.CreateView):
    """View class for tag create page."""
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    """View class for tag update page."""
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    """View class for confirm deletion page."""
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
