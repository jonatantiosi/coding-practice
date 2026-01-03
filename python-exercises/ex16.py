class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    @property
    def matricular_curso(self):
        return self.cursos
    
    @matricular_curso.setter
    def matricular_curso(self, novos_curso):
        self.cursos.extend(novos_curso)

    def listar_cursos(self):
        if not self.cursos:
            print(f'O(a) aluno(a) {self.nome} não está matriculado em nenhum curso.')
            return
        print(f'O(a) aluno(a) {self.nome} está matriculado nos seguintes cursos:')
        cursos_formatados = ', '.join(self.cursos) + '.'
        print(cursos_formatados)

class Curso:
    def __init__(self, nome):
        self.nome = nome

curso_1 = Curso('Matemática Discreta')
curso_2 = Curso('Análise de Dados')
curso_3 = Curso('Literatura')
curso_4 = Curso('Banco de Dados')

aluno_1 = Aluno('Jonatan Tiosi') 
aluno_2 = Aluno('Nathalia Paes')
aluno_3 = Aluno('Maple')

# seria melhor associar tudo, pra nao ficar limitado a nome
aluno_1.matricular_curso = curso_1.nome, curso_2.nome, curso_4.nome
aluno_2.matricular_curso = curso_3.nome, curso_4.nome

aluno_1.listar_cursos()
print()
aluno_2.listar_cursos()
print()
aluno_3.listar_cursos()