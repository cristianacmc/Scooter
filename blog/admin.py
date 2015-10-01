from django.contrib import admin
from .models import Post, Comment
from .models import Categoria


admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comment)
