## Requisitos

- Python 3.10 ou superior
- pip

## Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o arquivo `.env` com a chave secreta (obrigatória, não versionado):

```bash
cp .env.example .env
sed -i "s/^SECRET_KEY=.*/SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')/" .env
```

Execute:

```bash
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

O banco `unidin.db` é criado e populado automaticamente na primeira execução.