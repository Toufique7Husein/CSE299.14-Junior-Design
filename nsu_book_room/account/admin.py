from django.contrib import admin
from short_story.models import Comment
from short_story.models import ShortStory
from long_story.models import LongStory
from discussion.models import Topic
from discussion.models import Discussion
from discussion.models import Message
from .models import User

# Register your models here.

admin.site.register(ShortStory)
admin.site.register(Comment)
admin.site.register(LongStory)
admin.site.register(Topic)
admin.site.register(Discussion)
admin.site.register(Message)

admin.site.register(User)