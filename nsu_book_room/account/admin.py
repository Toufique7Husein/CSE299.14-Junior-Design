from django.contrib import admin
from short_story.models import Comment
from short_story.models import ShortStory
from long_story.models import LongStory
from .models import User

# Register your models here.

admin.site.register(ShortStory)
admin.site.register(Comment)
admin.site.register(LongStory)

admin.site.register(User)