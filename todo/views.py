from django.views import generic
from django.shortcuts import redirect, get_object_or_404

from .models import Task


class TaskListView(generic.ListView):
    """View class for home/tasks page."""
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "task_list"
    paginate_by = 5


def toggle_task_status(request, pk):
    """View funktion for task is_done status."""
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("task_list")
