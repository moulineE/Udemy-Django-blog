from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()

# Create your models here.


class BlogPost(models.Model):
    """Model for blog post."""
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    class Meta:
        """Meta options for BlogPost model."""
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        """Return title of blog post as name of the object."""
        return self.title

    def save(self, *args, **kwargs):
        """Override save method to generate slug."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def author_or_default(self):
        """Return author username or 'Anonyme'."""
        return self.author.username if self.author else "Anonyme"

    @property
    def date_or_default(self):
        """Return created_on date or 'N/A'."""
        return self.created_on.strftime("%d %B %Y") if self.created_on else "N/A"

    def get_absolute_url(self):
        """Return absolute URL of the object."""
        return reverse('posts:home')
