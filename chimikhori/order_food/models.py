from django.db import models
from django_comments.moderation import CommentModerator, moderator
from django_comments.abstracts import BaseCommentAbstractModel
from django_comments.forms import CommentSecurityForm
from django import forms
from django.conf import settings


class Comment(BaseCommentAbstractModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment = models.TextField()


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    
    
class CommentForm(CommentSecurityForm):
    comment = forms.CharField(widget=forms.Textarea())


class FoodModerator(CommentModerator):
    def allow(self, comment, content_object, request):
        return request.user.is_authenticated
    
    def get_form(self, *args, **kwargs):
        return CommentForm
    
    def get_mode(self, *args, **kwargs):
        return Comment
    

moderator.register(Food, FoodModerator)
