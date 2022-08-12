'''Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. Depois, desenvolva três ou mais objetos para testar o código.'''

class aluno:
    cont=0
    def __init__(self, nome, idade, serie):
        self.nome=nome
        self.idade=idade
        self.serie=serie
        aluno.cont+=1

    def muda_idade(self, nova_idade):
        self.idade=nova_idade

    def muda_serie(self, nova_serie):
        self.serie=nova_serie

aluno1=aluno("Renato", "12", "sexta")
aluno2=aluno("Bruna", "14", "oitava")
aluno3=aluno("Bruna", "10", "quinta")
aluno2.muda_idade("15")
aluno3.muda_serie("quarta")
print(f'Aluno: {aluno1.nome}\nIdade: {aluno1.idade}\nSérie: {aluno1.serie}\n'
      f'Aluno: {aluno2.nome}\nIdade: {aluno2.idade}\nSérie: {aluno2.serie}\n'
      f'Aluno: {aluno3.nome}\nIdade: {aluno3.idade}\nSérie: {aluno3.serie}\n'
      f'Total de alunos cadastrados: {aluno.cont}')
