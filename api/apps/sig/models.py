from django.db import models

from apps.sig.querysets import SigDiscente as SigDiscenteQS


class SigPessoa(models.Model):
    id_pessoa = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    cpf_cnpj = models.BigIntegerField()
    email = models.EmailField()

    class Meta:
        managed = False
        db_table = u'"comum\".\"pessoa"'
        default_permissions = ()


class SigUsuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=60)
    pessoa = models.ForeignKey(SigPessoa, on_delete=models.RESTRICT, db_column='id_pessoa')

    class Meta:
        managed = False
        db_table = u'"comum\".\"usuario"'
        default_permissions = ()


class SigCategoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = u'"rh\".\"categoria"'
        default_permissions = ()


class SigServidor(models.Model):
    id_servidor = models.IntegerField(primary_key=True)
    siape = models.IntegerField()
    id_ativo = models.IntegerField()
    pessoa = models.ForeignKey(SigPessoa, on_delete=models.RESTRICT, db_column='id_pessoa')
    categoria = models.ForeignKey(SigCategoria, on_delete=models.RESTRICT, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = u'"rh\".\"servidor"'
        default_permissions = ()


class SigStatusDiscente(models.Model):
    id_status = models.IntegerField(primary_key=True, db_column='status')
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'status_discente'
        default_permissions = ()


class SigTipoMovimentacaoAluno(models.Model):
    id_tipo_movimentacao_aluno = models.IntegerField(primary_key=True)
    descricao = models.TextField()
    grupo = models.CharField(max_length=2, null=True)
    ativo = models.BooleanField()
    status_discente = models.ForeignKey(SigStatusDiscente, on_delete=models.RESTRICT, db_column='statusdiscente')
    graduacao = models.BooleanField()
    stricto = models.BooleanField()
    todos = models.BooleanField()
    perda = models.BooleanField()
    medio = models.BooleanField()

    class Meta:
        managed = False
        db_table = u'"ensino\".\"tipo_movimentacao_aluno"'
        default_permissions = ()


class SigDiscente(models.Model):
    id_discente = models.IntegerField(primary_key=True)
    matricula = models.PositiveBigIntegerField()
    pessoa = models.ForeignKey(SigPessoa, on_delete=models.RESTRICT, db_column='id_pessoa')
    status_discente = models.ForeignKey(SigStatusDiscente, on_delete=models.RESTRICT, db_column='status')
    ano_ingresso = models.PositiveSmallIntegerField(db_column='ano_ingresso')
    periodo_ingresso = models.PositiveSmallIntegerField(db_column='periodo_ingresso')

    objects = SigDiscenteQS.as_manager()

    class Meta:
        managed = False
        db_table = 'discente'
        default_permissions = ()


class SigMovimentacaoAluno(models.Model):
    id_movimentacao_aluno = models.IntegerField(primary_key=True)
    discente = models.ForeignKey(SigDiscente, on_delete=models.RESTRICT, db_column='id_discente')
    tipo_movimentacao = models.ForeignKey(SigTipoMovimentacaoAluno, on_delete=models.RESTRICT,
                                          db_column='id_tipo_movimentacao_aluno')
    data_ocorrencia = models.DateTimeField()
    ativo = models.BooleanField()
    ano_referencia = models.PositiveSmallIntegerField()
    periodo_referencia = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = u'"ensino\".\"movimentacao_aluno"'
        default_permissions = ()


class SigEstornoMovimentacaoAluno(models.Model):
    id_estorno_movimentacao_aluno = models.IntegerField(primary_key=True)
    data_estorno = models.DateTimeField()
    movimentacao = models.ForeignKey(SigMovimentacaoAluno, on_delete=models.RESTRICT, db_column='id_movimentacao_aluno')

    class Meta:
        managed = False
        db_table = u'"ensino\".\"estorno_movimentacao_aluno"'
        default_permissions = ()


class SigCampus(models.Model):
    id_campus = models.IntegerField(primary_key=True, db_column='id_unidade')
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = u'"comum\".\"unidade"'
        default_permissions = ()


class SigCurso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200)
    nivel = models.CharField(max_length=1)
    campus = models.ForeignKey(SigCampus, on_delete=models.RESTRICT, db_column='id_unidade')

    class Meta:
        managed = False
        db_table = 'curso'
        default_permissions = ()

    def __str__(self):
        return self.nome


class SigDisciplinaDetalhes(models.Model):
    id_disciplina_detalhes = models.IntegerField(primary_key=True, db_column='id_componente_detalhes')
    nome = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"componente_curricular_detalhes"'
        default_permissions = ()


class SigGraduacaoCurriculo(models.Model):
    id_curriculo = models.IntegerField(primary_key=True, db_column='id_curriculo')
    curso = models.ForeignKey(SigCurso, on_delete=models.RESTRICT, db_column='id_curso')

    class Meta:
        managed = False
        db_table = u'"graduacao\".\"curriculo"'
        default_permissions = ()


class SigModalidade(models.Model):
    id_modalidade_curso_tecnico = models.IntegerField(primary_key=True, db_column='id_modalidade_curso_tecnico')
    descricao = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = u'"tecnico"\".\"modalidade_curso_tecnico"'
        default_permissions = ()


class SigEstruturaCurricular(models.Model):
    id_estrutura_curricular = models.IntegerField(primary_key=True, db_column='id_estrutura_curricular')
    modalidade = models.ForeignKey(SigModalidade, on_delete=models.PROTECT, db_column='id_modalidade_curso_tecnico')

    class Meta:
        managed = False
        db_table = u'"tecnico\".\"estrutura_curricular_tecnica"'
        default_permissions = ()


class SigDisciplina(models.Model):
    id_disciplina = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=20)
    detalhe = models.ForeignKey(SigDisciplinaDetalhes, on_delete=models.RESTRICT, db_column='id_detalhe')
    curso = models.ForeignKey(SigCurso, on_delete=models.RESTRICT, db_column='id_curso', null=True)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"componente_curricular"'
        default_permissions = ()


class SigGraduacaoCurriculoComponente(models.Model):
    id_curriculo_componente = models.IntegerField(primary_key=True, db_column='id_curriculo_componente')
    disciplina = models.ForeignKey(SigDisciplina, on_delete=models.RESTRICT, db_column='id_disciplina')
    curriculo = models.ForeignKey(SigGraduacaoCurriculo, on_delete=models.RESTRICT, db_column='id_curriculo')

    class Meta:
        managed = False
        db_table = u'"graduacao\".\"curriculo_componente"'
        default_permissions = ()


class SigModuloDisciplina(models.Model):
    id_modulo = models.IntegerField(primary_key=True, db_column='id_modulo')
    disciplina = models.ForeignKey(SigDisciplina, on_delete=models.RESTRICT, db_column='id_disciplina')

    class Meta:
        managed = False
        db_table = u'"tecnico\".\"modulo_disciplina'
        default_permissions = ()


class SigModuloCurricular(models.Model):
    id_modulo_curricular = models.IntegerField(primary_key=True, db_column='id_modulo_curricular')
    modulo_disciplina = models.ForeignKey(SigModuloDisciplina, on_delete=models.PROTECT, db_column='id_modulo')
    estrutura_curricular = models.ForeignKey(
        SigEstruturaCurricular, on_delete=models.PROTECT,
        db_column='id_estrutura_curricular'
    )

    class Meta:
        managed = False
        db_table = u'"tecnico"\".\"modulo_curricular"'
        default_permissions = ()


class SigSituacaoTurma(models.Model):
    id_situacao = models.IntegerField(primary_key=True, db_column='id_situacao_turma')
    descricao = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"situacao_turma"'
        default_permissions = ()


class SigTurma(models.Model):
    id_turma = models.IntegerField(primary_key=True)
    ano = models.IntegerField()
    periodo = models.IntegerField()
    codigo = models.CharField(max_length=30)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    curso = models.ForeignKey(SigCurso, on_delete=models.RESTRICT, db_column='id_curso', null=True)
    disciplina = models.ForeignKey(SigDisciplina, on_delete=models.RESTRICT, db_column='id_disciplina')
    situacao = models.ForeignKey(SigSituacaoTurma, on_delete=models.RESTRICT, db_column='id_situacao_turma')

    class Meta:
        managed = False
        db_table = u'"ensino\".\"turma"'
        default_permissions = ()


class SigDocenteTurma(models.Model):
    id_docente_turma = models.IntegerField(primary_key=True, db_column='id_docente_turma')
    turma = models.ForeignKey(SigTurma, on_delete=models.RESTRICT, db_column='id_turma')
    docente = models.ForeignKey(SigServidor, on_delete=models.RESTRICT, db_column='id_docente',
                                related_name='docente_turma')
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = u'"ensino\".\"docente_turma"'
        default_permissions = ()


class SigSituacaoMatricula(models.Model):
    id_situacao_matricula = models.IntegerField(primary_key=True, db_column='id_situacao_matricula')
    descricao = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = u'"ensino\".\"situacao_matricula"'
        default_permissions = ()


class SigDiscenteTurma(models.Model):
    id_discente_turma = models.IntegerField(primary_key=True, db_column='id_matricula_componente')
    turma = models.ForeignKey(SigTurma, on_delete=models.RESTRICT, db_column='id_turma')
    discente = models.ForeignKey(SigDiscente, on_delete=models.RESTRICT, db_column='id_discente')
    situacao_matricula = models.ForeignKey(SigSituacaoMatricula, on_delete=models.RESTRICT,
                                           db_column='id_situacao_matricula')

    class Meta:
        managed = False
        db_table = u'"ensino\".\"matricula_componente"'
        default_permissions = ()
