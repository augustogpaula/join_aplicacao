from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Permissoes(models.Model):
    nome_permissao = models.CharField(u'Nome da permissão', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome_permissao

    class Meta:
        verbose_name = u'permissão'
        verbose_name_plural = u'5. Permissões'


class Endereco(models.Model):
    rua = models.CharField(max_length=120, null=False, blank=False)
    bairro = models.CharField(max_length=80, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    complemento = models.CharField(max_length=120, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    pais = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return f"{self.rua} - {self.bairro} - {self.numero}"

    class Meta:
        verbose_name = u'endereço'
        verbose_name_plural = u'1. Endereços'


class Cargos(models.Model):
    nome_cargo = models.CharField('Nome', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.nome_cargo

    class Meta:
        verbose_name = u'cargo'
        verbose_name_plural = u'2. Cargos'


class Funcionarios(models.Model):
    nome = models.CharField('Nome', max_length=80, blank=False, null=False)
    admissao = models.DateField(u'Data de admissão', blank=False, null=False)
    cargo = models.ForeignKey(Cargos, verbose_name=u'Cargo associado',
                              related_name='Cargos',
                              on_delete=models.CASCADE,
                              blank=False, null=False)
    endereco = models.OneToOneField(Endereco, verbose_name=u'Endereço',
                                    on_delete=models.SET_NULL,
                                    blank=True, null=True)
    permissoes = models.ManyToManyField(Permissoes, verbose_name=u'Permissões',
                                        blank=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'

    class Meta:
        verbose_name = u'funcionário'
        verbose_name_plural = u'3. Funcionários'


class Solicitacoes(models.Model):
    funcionario = models.ForeignKey(Funcionarios, verbose_name=u'Funcionário',
                                    on_delete=models.CASCADE,
                                    related_name='funcionarios')
    solicitacao = models.CharField(u'Solicitação', max_length=250, null=False, blank=False)
    data_solicitacao = models.DateTimeField(u'Data da solicitação', default=datetime.now)
    resolvido = models.BooleanField(u'Solicitação resolvida ?', default=False)

    def __str__(self):
        return self.funcionario.nome

    class Meta:
        verbose_name = u'solicitação'
        verbose_name_plural = u'4. Solicitações'


class Alvos(models.Model):
    nome = models.CharField('Nome', max_length=80, blank=False, null=False)
    latitude_localizacao = models.FloatField(u'Latitude da localização',
                                             validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
                                             blank=False, null=False,
                                             help_text=u'Latitude da localização do alvo registrado')
    longitude_localizacao = models.FloatField(u'Longitude da localização',
                                              validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],
                                              blank=False, null=False,
                                              help_text=u'Longitude da localização do alvo registrado')
    data_expiracao = models.DateField(u'Data de expiração', blank=False, null=False)
    deletado = models.BooleanField(u'Deletado ?', default=False)

    def __str__(self):
        return f'{self.id} - {self.nome}'

    class Meta:
        verbose_name = u'alvo'
        verbose_name_plural = u'6. Alvos'


