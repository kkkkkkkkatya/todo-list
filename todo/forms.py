from django import forms
from django.contrib.auth import get_user_model

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=forms.SelectDateWidget(),
        required=True
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"

