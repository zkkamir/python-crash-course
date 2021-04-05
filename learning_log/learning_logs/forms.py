from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "Entry:"}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
