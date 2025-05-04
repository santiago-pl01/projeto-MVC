#  EStrutura do projeto-MVC

Estrutura do projeto:<br>
meu_projeto/<br>
|-- app/<br>
| |-- static/ (arquivos CSS, JS, imagens)<br>
| |-- templates/ (arquivos HTML)<br>
| |-- models.py (definição das classes do banco de dados)<br>
| |-- views.py (definição das rotas e lógica da aplicação)<br>
| |-- controllers.py (funções que tratam os dados)<br>
|-- main.py (ponto de entrada da aplicação)<br>
|-- requirements.txt (dependências do projeto)<br>
|-- README.md (documentação sobre o projeto)<br>

##
🧠 Resumo prático:

| Parte       | Responsabilidade              | Local comum         |
|-------------|-------------------------------|---------------------|
| Model       | Dados, regras de negócio      | models.py           |
| View        | Interface visual (HTML/CSS)   | Pasta templates/    |
| Controller  | Lógica das rotas e respostas  | app.py ou routes.py |



# 📚 Projeto Acadêmico - API com Flask (Padrão MVC)

Este projeto foi desenvolvido com fins acadêmicos, com o objetivo de compreender na prática as funcionalidades do framework **Flask**, aplicando o padrão de arquitetura **MVC (Model-View-Controller)**.

A aplicação simula um pequeno sistema de cadastro de **usuários** e **produtos**, no qual um **gerente** pode adicionar, editar ou excluir registros de ambos os tipos. A estrutura dividida em camadas permite um melhor entendimento, organização do código e facilita futuras manutenções.

---

## 🧩 Estrutura do Projeto

O projeto está dividido em três camadas principais:

### 📦 Model (Banco de Dados)
Responsável pela modelagem e estrutura dos dados. Nesta camada estão definidos os modelos de:

- **Usuário**: com atributos como `nome`, `e-mail` e `senha`.
- **Produto**: com atributos como `nome`, `tipo`, `preço` e `id`.

Todos os dados são armazenados em um banco de dados SQLite simples, ideal para projetos de pequeno porte e testes locais.

---

### 🌐 View (Rotas e Templates)

A camada de **View** é responsável por:

- Definir as **rotas** da aplicação;
- Renderizar os **templates HTML** com auxílio de CSS para o estilo visual;
- Exibir as páginas aos usuários.

Os principais templates utilizados são:

- `index.html`: Página inicial onde o usuário escolhe o que deseja cadastrar (usuário ou produto);
- `cadastrar.html`: Página de cadastro de usuários;
- `produto.html`: Página de cadastro de produtos.

---

### 🧠 Controller (Regras de Negócio)

O **controller** faz a interligação entre a *view* e o *model*. É aqui que estão implementadas as principais **regras de negócio**, como:

- Validação de dados de entrada;
- Comunicação com o banco de dados;
- Redirecionamentos após ações como cadastro, edição ou exclusão.

Essa separação torna o sistema mais organizado, facilitando futuras atualizações e o trabalho em equipe.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLite
- HTML5
- CSS3

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git



