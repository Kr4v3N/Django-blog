from django import forms

from pyblog.models import Comment


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text', ]
