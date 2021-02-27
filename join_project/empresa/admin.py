from django.contrib import admin
from empresa.models import *


# Register your models here.
class CargosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_cargo', ]
    search_fields = ['id', 'nome_cargo', ]


class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'admissao', 'cargo', ]
    search_fields = ['id', 'nome', ]
    list_filter = ['cargo', ]
    filter_horizontal = ['permissoes', ]


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['id', 'rua', 'bairro', 'numero', ]
    search_fields = ['id', 'rua', 'bairro', 'numero', 'cidade', 'pais', ]


class SolicitacoesAdmin(admin.ModelAdmin):
    list_display = ['id', 'funcionario', 'data_solicitacao', 'resolvido', ]
    search_fields = ['id', 'funcionario', ]

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ('data_solicitacao', )


class PermissoesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_permissao', ]
    search_fields = ['id', 'nome_permissao', ]


class AlvosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', ]
    search_fields = ['id', 'nome', ]


admin.site.register(Cargos, CargosAdmin)
admin.site.register(Funcionarios, FuncionariosAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Solicitacoes, SolicitacoesAdmin)
admin.site.register(Permissoes, PermissoesAdmin)
admin.site.register(Alvos, AlvosAdmin)