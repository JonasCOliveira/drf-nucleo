from pydoc import describe
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now

class Descargas(models.Model):
    latitude = models.DecimalField(max_digits=100, decimal_places=98)
    longitude = models.DecimalField(max_digits=100, decimal_places=98)
    intensidade = models.CharField(max_length=100)
    timestamp = models.DateTimeField()


class Imagem(models.Model):
    lat = models.DecimalField(max_digits=100, decimal_places=98)
    lng = models.DecimalField(max_digits=100, decimal_places=98)
    caminho = models.CharField(max_length=255)
    atualizacao = models.DateTimeField()
    captura = models.DateTimeField()
    


class Empresa(models.Model):
    cnpj = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=30, null=False)
    telefone = models.CharField(max_length=20, null=False)
    descricao = models.CharField(max_length=100)
    habilitado = models.BooleanField(default=True, null=False)

class Servico(models.Model):
    nome = models.CharField(max_length=40, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)

class Pagamento(models.Model):
    status = models.CharField(max_length=40, null=False)

class Plano(models.Model):
    nome = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=50, null=False)
    inicioContrato = models.DateField(null=False)
    fimContrato = models.DateField(null=False)
    inicioMonitoramento = models.TimeField(null=False)
    fimMonitoramento = models.TimeField(null=False)
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE, null=False)

class  Buffer(models.Model):
    tipoBuffer = models.CharField(max_length=40, null=False)

class Satelite(models.Model):
    nome = models.CharField(max_length=30, null=False)
    canal = models.IntegerField()

class Alvo(models.Model):
    # lat = models.DecimalField(max_digits=100, decimal_places=98)
    # lng = models.DecimalField(max_digits=100, decimal_places=98)
    nome = models.CharField(max_length=100, default='', blank=False, null=False)
    coordenadas = models.TextField(default='')
    buffer = models.ForeignKey(Buffer, on_delete=models.DO_NOTHING)
    satelite = models.ForeignKey(Satelite, on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)
    

class Permissao(models.Model):
    tipo = models.CharField(max_length=30, null=False)

class UsuarioEmpresa(models.Model):
    nome = models.CharField(max_length=50, null=False)
    cargo = models.CharField(max_length=30, null=False)
    diasTrabalhados = models.CharField(max_length=100, null=False)
    jornada = models.CharField(max_length=40, null=False)
    telefone = models.CharField(max_length=45, null=False)
    empresa = models.ForeignKey(Empresa, on_delete=CASCADE)

