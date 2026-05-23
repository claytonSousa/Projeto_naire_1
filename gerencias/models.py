from django.db import models
import mysql.connector

#Classe de conexao
class Conn(models.Model):
    def executa_query(consulta):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="bd_naire2"
        )
        mycursor = mydb.cursor()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(consulta)
        myresult = mycursor.fetchall()
        mydb.close()
        return myresult
    
    def executa_insert(consulta):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="bd_naire2"
        )
        mycursor = mydb.cursor()
        mycursor.execute(consulta)
        mydb.commit()
        mydb.close()
        return mycursor.lastrowid

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class TbFuncionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    id_tipo = models.ForeignKey('TbTipoFuncionario', models.DO_NOTHING, db_column='id_tipo')
    pnome = models.CharField(max_length=255)
    snome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    flag_ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_funcionario'


class TbTipoFuncionario(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    descricao = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'tb_tipo_funcionario'

class TbCadastroResponsavel(models.Model):
    id_responsavel = models.AutoField(primary_key=True)
    id_usuario_cad = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario_cad', blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(blank=True, null=True)
    pnome = models.CharField(max_length=100, blank=True, null=True)
    snome = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=11)
    titulo = models.CharField(max_length=45, blank=True, null=True)
    data_nascimento = models.CharField(max_length=10, blank=True, null=True)
    flag_responsavel_trabalha = models.CharField(max_length=1, blank=True, null=True)
    flag_conjuge = models.CharField(max_length=1, blank=True, null=True)
    flag_conjuge_trabalha = models.CharField(max_length=1, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    url_image_familia = models.CharField(max_length=255, blank=True, null=True)
    flag_validado = models.CharField(max_length=1, blank=True, null=True)
    flag_ativo = models.CharField(max_length=1, blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cadastro_responsavel'

class TbCadastroResponsavel(models.Model):
    id_responsavel = models.AutoField(primary_key=True)
    id_usuario_cad = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario_cad', blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(blank=True, null=True)
    pnome = models.CharField(max_length=100, blank=True, null=True)
    snome = models.CharField(max_length=255, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=11)
    titulo = models.CharField(max_length=45, blank=True, null=True)
    data_nascimento = models.CharField(max_length=10, blank=True, null=True)
    flag_responsavel_trabalha = models.CharField(max_length=1, blank=True, null=True)
    flag_conjuge = models.CharField(max_length=1, blank=True, null=True)
    flag_conjuge_trabalha = models.CharField(max_length=1, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    url_image_familia = models.CharField(max_length=255, blank=True, null=True)
    flag_validado = models.CharField(max_length=1, blank=True, null=True)
    flag_ativo = models.CharField(max_length=1, blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cadastro_responsavel'


class TbFilhosResponsavel(models.Model):
    #pk = models.CompositePrimaryKey('id_filho', 'id_responsavel')
    id_filho = models.AutoField(primary_key=True)
    id_responsavel = models.ForeignKey(TbCadastroResponsavel, models.DO_NOTHING, db_column='id_responsavel')
    id_usuario_cad = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario_cad', blank=True, null=True)
    pnome = models.CharField(max_length=100, blank=True, null=True)
    snome = models.CharField(max_length=255, blank=True, null=True)
    data_nascimento = models.CharField(max_length=10, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    sexo = models.CharField(max_length=2, blank=True, null=True)
    numero_roupa = models.CharField(max_length=15, blank=True, null=True)
    numero_sapato = models.IntegerField(blank=True, null=True)
    cadastro_outra_ong = models.CharField(max_length=1, blank=True, null=True)
    url_imagem = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_atualizacao = models.DateTimeField(blank=True, null=True)
    flag_ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_filhos_responsavel'

class TbOficios(models.Model):
    id_oficio = models.AutoField(primary_key=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    id_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario')
    destinatario = models.CharField(max_length=255, blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_oficios'

class TbMadrinhaPadrinho(models.Model):
    id_mad_pad = models.AutoField(primary_key=True)
    id_usuario_cad = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario_cad', blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=11, blank=True, null=True)
    flag_anonimo = models.CharField(max_length=1, blank=True, null=True)
    pnome = models.CharField(max_length=100, blank=True, null=True)
    snome = models.CharField(max_length=255, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    atualizacao_cad = models.DateTimeField(blank=True, null=True)
    flag_ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_madrinha_padrinho'

class TbApadrinhamentoCrianca(models.Model):
    id_apadrinhamento = models.IntegerField(primary_key=True)
    id_mad_pad = models.ForeignKey('TbMadrinhaPadrinho', models.DO_NOTHING, db_column='id_mad_pad')
    id_filho = models.ForeignKey('TbFilhosResponsavel', models.DO_NOTHING, db_column='id_filho')
    data_cadastro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apadrinhamento_crianca'

class TbEntrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_evento = models.IntegerField()
    id_mad_pad = models.IntegerField(blank=True, null=True)
    id_crianca = models.IntegerField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=255, blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_chegada = models.DateTimeField(blank=True, null=True)
    flag_finalizado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_entrega'

class TbEvento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    data_evento = models.CharField(max_length=10)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=225, blank=True, null=True)
    flag_finalizado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_evento'