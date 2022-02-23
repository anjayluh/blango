from django.shortcuts import render
import logging
from .models import Post, Comment

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    posts = Post.objects.all()
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html")

def post_detail(request):
    Comment.objects.create(message=request.data)
    logger.info(
        "Created comment on Post %d for user %s", post.pk, request.user
    )
    return render(request, "blog/index.html")