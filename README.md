# ⚽ Sistema de Visualização de Times de Futebol

Projeto desenvolvido com Django para visualizar times de futebol cadastrados em um banco de dados.

---

## 🚀 Tecnologias utilizadas

- Python 3
- Django
- HTML + CSS
- SQLite (banco padrão do Django)

---

## 🎯 Objetivo do projeto

O sistema permite:

- Cadastro de times via painel administrativo do Django
- Visualização dos times em uma interface web
- Organização das informações como:
  - Nome do time
  - Cidade
  - Estádio
  - Ano de fundação

---

## 🖥️ Funcionalidades

✔ Cadastro de times pelo admin  
✔ Listagem de times na página principal  
✔ Interface estilizada (tema preto e branco inspirado em clubes tradicionais)  
✔ Estrutura organizada em Django (Model, View, Template)

---

## 📂 Estrutura do projeto

```
Times_django/
│
├── futebol_project/
├── times/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Valmartinssantos/Times_django.git
2. Entrar na pasta
cd Times_django
3. Criar ambiente virtual
py -m venv venv
4. Ativar ambiente
venv\Scripts\activate
5. Instalar dependências
py -m pip install -r requirements.txt
6. Rodar o projeto
py manage.py runserver
```

🔐 Acesso ao admin

Após rodar o servidor, acesse:

http://127.0.0.1:8000/admin/

Crie um superusuário com:

py manage.py createsuperuser

📸 Demonstração

Sistema web exibindo lista de times cadastrados com layout moderno e responsivo.
