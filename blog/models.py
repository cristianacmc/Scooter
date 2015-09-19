from django.db import models
from django.utils import timezone

class contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    Assunto = models.TextField()
    Mensagem = models.TextField()

    def __unicode__(self):
        return self.nome

class categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

class Post(models.Model):
    categorias = models.ManyToManyField(categoria)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.titulo

class comentarios(models.Model):
    autor = models.CharField(max_length=100)
    comentario = models.TextField(max_length=1024)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return sel.autor
