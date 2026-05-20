# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TbApadrinhamentoCrianca(models.Model):
    idtb_apadrinhamento = models.IntegerField(primary_key=True)
    id_mad_pad = models.ForeignKey('TbMadrinhaPadrinho', models.DO_NOTHING, db_column='id_mad_pad')
    id_crianca = models.ForeignKey('TbFilhosResponsavel', models.DO_NOTHING, db_column='id_crianca')
    data_cadastro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_apadrinhamento_crianca'


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
    pk = models.CompositePrimaryKey('id_filho', 'id_responsavel')
    id_filho = models.AutoField()
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


class TbFuncionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    id_tipo = models.ForeignKey('TbTipoFuncionario', models.DO_NOTHING, db_column='id_tipo')
    pnome = models.CharField(max_length=255)
    snome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    flag_ativo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_funcionario'


class TbMadrinhaPadrinho(models.Model):
    id_mad_pad = models.AutoField(primary_key=True)
    id_usuario_cad = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario_cad', blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
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


class TbOficios(models.Model):
    id_oficio = models.AutoField(primary_key=True)
    data_criacao = models.DateTimeField(blank=True, null=True)
    id_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario')
    destinatario = models.CharField(max_length=255, blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_oficios'


class TbTipoFuncionario(models.Model):
    id_tipo = models.AutoField(primary_key=True)
    descricao = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'tb_tipo_funcionario'
