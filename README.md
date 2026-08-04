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

## 🔐 Segurança

Este repositório já teve uma `SECRET_KEY` exposta em versões antigas do `settings.py`. A chave foi **rotacionada** e o projeto agora lê toda a configuração sensível de **variáveis de ambiente**:

| Variável | Descrição |
|---|---|
| `DJANGO_SECRET_KEY` | Gere a sua com `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| `DJANGO_DEBUG` | `True` só em desenvolvimento · `False` em produção |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos, separados por vírgula |

Copie `.env.example` para `.env` e preencha os valores. O banco (`db.sqlite3`) e as configurações de IDE (`.idea/`) ficam fora do versionamento — veja o `.gitignore`.

## 👤 Autor

**Alexandre Ramos** — [github.com/Alexsantossp71](https://github.com/Alexsantossp71)

## 📄 Status

Material de estudo (junho/2025).
