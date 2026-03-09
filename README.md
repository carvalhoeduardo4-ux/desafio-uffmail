# Sistema de Criação de UFFMail - Desafio Técnico 🎓

Este projeto é uma solução para o desafio de implementação da criação de contas de e-mail (UFFMail) para alunos da Universidade Federal Fluminense. O sistema processa dados de um arquivo CSV, valida o status do aluno e gera opções personalizadas de e-mail.

##  Funcionalidades

- **Leitura de Dados:** Consumo de base de dados via arquivo `.csv`.
- **Validação de Regras de Negócio:**
  - Apenas alunos com status **Ativo** podem criar e-mails.
  - Alunos que já possuem um UFFMail cadastrado são impedidos de criar um novo.
- **Gerador de Opções:** Algoritmo que gera 4 variações de e-mail baseadas no nome do aluno.
- **Persistência de Dados:** O sistema atualiza o arquivo CSV automaticamente após a escolha do usuário.
- **Simulação de Notificações:** Exibição de confirmação de criação de conta e envio de SMS com senha.

##  Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 
- **Orientação a Objetos (OO):** Utilização de classes (`Aluno`, `SistemaUFF`, `GeradorUffMail`) para garantir baixo acoplamento e alta coesão.
- **Manipulação de Arquivos:** Uso das bibliotecas nativas `csv` para leitura e escrita (`DictReader` e `DictWriter`).
- **Tratamento de Exceções:** Robustez no código para lidar com erros de entrada de dados ou arquivos ausentes.

##  Estrutura do Código

- **Aluno:** Classe modelo que representa a entidade aluno.
- **GeradorUffMail:** Classe utilitária com métodos estáticos para lógica de strings.
- **SistemaUFF:** Classe controladora responsável pelo fluxo principal e interação com o arquivo CSV.