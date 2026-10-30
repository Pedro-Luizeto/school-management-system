# 🎓 Sistema de Gerenciamento de Alunos

Aplicação de terminal em Python para cadastrar e consultar alunos, acompanhar suas notas e calcular a média geral da turma.

<p align="center">
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-como-executar">Como executar</a> •
  <a href="#-menu-do-sistema">Menu</a> •
  <a href="#-tecnologias">Tecnologias</a>
</p>

---

## 💻 Sobre o projeto

O **Sistema de Gerenciamento de Alunos** é um programa de linha de comando que organiza informações básicas de uma turma. Pelo menu interativo, é possível adicionar, buscar, remover e listar alunos, além de consultar a média das notas cadastradas.

Os dados são mantidos em memória enquanto o programa está aberto. Ao encerrar a execução, os cadastros são apagados.

## ⚙️ Funcionalidades

- Cadastrar aluno com nome, idade e nota.
- Buscar aluno pelo nome, sem diferenciar letras maiúsculas de minúsculas.
- Remover aluno pelo nome.
- Listar todos os alunos cadastrados.
- Calcular a média geral das notas da turma.
- Exibir mensagens quando não há alunos ou quando um nome não é encontrado.
- Limpar a tela do terminal ao navegar pelo menu.

## 🚀 Como executar

### Pré-requisitos

- Python **3.10 ou superior** (o programa utiliza `match/case`).
- Um terminal ou prompt de comando.

O sistema usa apenas módulos da biblioteca padrão do Python, então não é necessário instalar dependências adicionais.

### Passos

1. Salve o código do programa em um arquivo chamado `sistema_alunos.py`.
2. Abra o terminal na pasta onde salvou o arquivo.
3. Execute:

```bash
python sistema_alunos.py
```

No Windows, se o comando `python` não estiver disponível, tente:

```powershell
py sistema_alunos.py
```

Em alguns sistemas, o comando pode ser:

```bash
python3 sistema_alunos.py
```

## 🖥️ Menu do sistema

Ao iniciar, escolha uma opção digitando o número correspondente:

| Opção | Ação |
| --- | --- |
| `1` | Adicionar aluno |
| `2` | Remover aluno pelo nome |
| `3` | Buscar aluno pelo nome |
| `4` | Listar todos os alunos |
| `5` | Mostrar a média geral |
| `6` | Sair do programa |

Para cadastrar um aluno, informe o nome, a idade e a nota quando solicitado. Depois de cada operação, pressione **ENTER** para voltar ao menu.

## 🛠️ Tecnologias

- **Python 3.10+**
- `os` — limpeza da tela do terminal
- `time` — pequenas pausas entre mensagens
- Estruturas nativas do Python, como listas, dicionários e funções

## 📌 Observações

- Os dados não são gravados em arquivo ou banco de dados; eles existem apenas durante a execução atual.
- A nota é exibida com duas casas decimais.
- O programa espera receber idade como número inteiro e nota como número decimal.
