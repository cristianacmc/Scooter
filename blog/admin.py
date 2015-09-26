from django.contrib import admin
from .models import Post
from .models import Categoria
from .models import Contato
from .models import Comentarios


admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Comentarios)
admin.site.register(Contato)
