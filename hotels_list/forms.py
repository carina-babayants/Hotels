from django.forms import ModelForm
from .models import Comments


class CommentForm(ModelForm):
    """Форма комментариев к отелю
    """
    class Meta:
        model = Comments
        fields = ('typ_comment','text',)