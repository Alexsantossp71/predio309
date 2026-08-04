# 🏢 Prédio 309 — Estudo de Django

> Projeto base Django criado para estudar o framework (startproject).

## 📌 Sobre

Repositório de estudo: estrutura inicial gerada pelo `django-admin startproject` para aprender o funcionamento do **Django** (settings, URLs, rotas e ORM). Serve como base para os projetos Integradores da UNIVESP.

## 🚀 Como executar localmente

```bash
git clone https://github.com/Alexsantossp71/predio309.git
cd predio309/predio309

python -m venv .venv
source .venv/bin/activate
pip install django

python manage.py runserver
# acesse http://localhost:8000
```

## ⚠️ Atenção (segurança)

Este repositório foi criado em ambiente de estudo e contém a `SECRET_KEY` exposta e `DEBUG=True` no arquivo `settings.py`. **Ao reutilizar este projeto:**

1. Gere uma nova SECRET_KEY
2. Use variáveis de ambiente (`.env`) — não commite segredos
3. Configure `DEBUG=False` e `ALLOWED_HOSTS` em produção
4. Adicione `db.sqlite3` e `.env` ao `.gitignore`

## 👤 Autor

**Alexandre Ramos** — [github.com/Alexsantossp71](https://github.com/Alexsantossp71)

## 📄 Status

Material de estudo (junho/2025).
