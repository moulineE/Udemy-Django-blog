from django.shortcuts import render

from django.views.generic import ListView

from posts.models import BlogPost

# Create your views here.
class BlogHome(ListView):
    """Home page view."""
    model = BlogPost
    context_object_name = "posts"

    def get_queryset(self):
        """
        Override get_queryset method to filter unpublished posts
        for anonymous users.
        """
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)