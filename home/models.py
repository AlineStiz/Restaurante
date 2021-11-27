import uuid  #gera valores hexadecimais aleatorios
from django.db import models

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)  #auto incremento , na criação
    modificado = models.DateField('Atualização', auto_now=True) #auto incremento, na modificação
    ativo = models.BooleanField('Ativo?', default=True) #

    class Meta:
        abstract = True

class Prato(Base):
    nome = models.CharField('Nome', max_length=100)
    ingrediente = models.CharField('Ingrediente', max_length=500)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':700, 'height':700, 'crop': True}})

    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Pratos'

    def __str__(self):
        return self.nome



class Receita(Base):
    nome = models.CharField('Nome', max_length=100)
    ingrediente = models.CharField('Ingrediente', max_length=500)
    preparo = models.CharField('Preparo', max_length=5000)
    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'

    def __str__(self):
        return self.nome


class Atividade(Base):
    descricao = models.CharField('Descrição', max_length=50)
    fazer = models.CharField('Fazer', max_length=5000)
    fazendo = models.CharField('Fazendo', max_length=5000)
    feito = models.CharField('Feito', max_length=5000)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.descricao


