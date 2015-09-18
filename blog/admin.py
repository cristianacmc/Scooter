from django.contrib import admin
from .models import Post
from .models import categoria
from .models import contato
from .models import comentarios


admin.site.register(categoria)
admin.site.register(Post)
admin.site.register(comentarios)
admin.site.register(contato)
