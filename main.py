import csv

class Aluno:
    def __init__(self,nome,matricula,telefone,email,uffmail,status):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.uffmail = uffmail
        self.status = status
        
    def is_ativo(self):
        return self.status.lower() == 'ativo'
    
    
class GeradorUffMail:
    @staticmethod
    def gerar_opcoes(nome_completo):
        partes = nome_completo.lower().split() 
        primeiro_nome = partes[0] 
        ultimo_nome = partes[-1] 
        
        opcoes = [
            f"{primeiro_nome}_{ultimo_nome}@id.uff.br",
            f"{primeiro_nome[0]}_{ultimo_nome}@id.uff.br",
            f"{primeiro_nome}_{ultimo_nome[0]}@id.uff.br",
            f"{primeiro_nome[0]}{primeiro_nome}{ultimo_nome[0]}{ultimo_nome}@id.uff.br"

        ]
        return opcoes


class SistemaUFF:
    def __init__(self,caminho_csv):
        self.caminhos_csv = caminho_csv
        self.alunos = {}
        self.carregar_dados(caminho_csv)
    
    def carregar_dados(self,caminho_csv):
        try:
            with open(caminho_csv,mode ='r',encoding='utf-8') as arquivo:
                leitor = csv.DictReader(arquivo) #lê o CSV e entrega cada linha como um dicionário
                for linha in leitor:
                    aluno = Aluno(
                        linha['nome'],
                        linha['matricula'],
                        linha['telefone'],
                        linha['email'],
                        linha['uffmail'],
                        linha['status']
                    )
                    self.alunos[aluno.matricula] = aluno
        except FileNotFoundError:
            print('ERRO: Arquivo csv não encontrado.')
    def atualiza_csv(self):
        colunas = ['nome','matricula','telefone','email','uffmail','status']
        try:
            with open(self.caminhos_csv,mode = 'w', encoding='utf-8') as arquivo:
                escritor = csv.DictWriter(arquivo, fieldnames=colunas) #recebe um dicionário e o transforma em uma linha de CSV, seguindo a ordem das fieldnames (colunas)
                escritor.writeheader() #escreve o cabeçalho
                for aluno in self.alunos.values():
                    escritor.writerow({
                        'nome' : aluno.nome,
                        'matricula' : aluno.matricula,
                        'telefone' : aluno.telefone,
                        'email' : aluno.uffmail,
                        'status' : aluno.status
                    })
        except Exception:
            print(f'Erro ao salvar arquivo {Exception}')
    
    def processar_solicitacao(self):
        matricula = input('Entre com a matricula: ')
        
        if not matricula in self.alunos:
            print('Matricula não encontrada')
            return
        aluno = self.alunos[matricula]
        
        #Regra 1: apenas alunos ativos podem ter um UFFmail
        if not aluno.is_ativo():
            print("Apenas alunos com status 'ativo' podem criar um UFFmail")
            return
        
        #Regra 2: um aluno só pode ter um UFFmail
        if aluno.uffmail:
            print('O aluno ja possui um UFFmail cadastrado')
            return
        
    
        print(f'\n{aluno.nome.split()[0]} por favor, escolha uma das opcoes abaixo:')
        opcoes = GeradorUffMail.gerar_opcoes(aluno.nome)
        
        for i,opcao in enumerate(opcoes,1):
            print(f'{i} - {opcao}')
        
        try:
            escolha = int(input('Digite o numero da opcao desejada: '))
            email_escolhido = opcoes[escolha - 1]
            
            aluno.uffmail = email_escolhido
            self.atualiza_csv()
            
            print(f"\nA criação de seu e-mail ({email_escolhido}) será feita nos próximos minutos.")
            print(f"Um SMS foi enviado para {aluno.telefone} com a sua senha de acesso.")
        
        except (ValueError, IndexError):
            print("Opção inválida.")
    
    
if __name__ == "__main__":
    sistema = SistemaUFF('alunos.csv')
    sistema.processar_solicitacao()

        
