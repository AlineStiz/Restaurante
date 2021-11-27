from django.contrib import admin

from .models import Prato,Receita,Atividade

@admin.register(Prato)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome','ingrediente','preco', 'ativo', 'modificado', 'imagem')

@admin.register(Receita)
class PratoAdmin(admin.ModelAdmin):
    list_display = ('nome','ingrediente','preparo', 'ativo', 'modificado')


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('descricao','fazer', 'fazendo', 'feito', 'ativo', 'modificado')

