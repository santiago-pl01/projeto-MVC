# projeto-MVC

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


