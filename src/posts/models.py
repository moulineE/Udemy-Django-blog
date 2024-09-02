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
    created_on = models.DateField(blang=True, null=True)
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
