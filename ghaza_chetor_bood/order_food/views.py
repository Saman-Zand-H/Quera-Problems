from django.shortcuts import render
from django_comments.models import Comment
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django_comments.forms import CommentForm
from order_food.models import *
from django.shortcuts import redirect
from django.contrib import messages


def menu_view(request):
    if request.method == "GET":
        foods = Food.objects.all()
        return render(request, 'order_food/menu.html', {
            'foods': foods,
        })
    elif request.method == "POST":
        data = CommentForm(request.POST)
        if data.is_valid():
            content_type = data.cleaned_data.get("content_type")
            object_id = data.cleaned_data.get("object_pk")
            content_obj = ContentType.get_object_for_this_type(pk=object_id)
            comment = Comment.objects.create(
                content_type=content_type,
                content_object=content_obj,
                object_pk=object_id,
                user=request.user,
                user_name=data.cleaned_data.get("name"),
                user_email=data.cleaned_data.get("email"),
                user_url=data.cleaned_data.get("url"),
                comment=data.cleaned_data.get("comment"),
                site_id=settings.SITE_ID,
                is_public=True,
                is_removed=False
            )
            comment.save()
            messages.success(request, "your comment successfully submitted.")
    return redirect("menu")
