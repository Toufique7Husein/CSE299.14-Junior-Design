from django.contrib import admin
from short_story.models import Comment
from short_story.models import ShortStory

# Register your models here.

admin.site.register(ShortStory)
admin.site.register(Comment)

