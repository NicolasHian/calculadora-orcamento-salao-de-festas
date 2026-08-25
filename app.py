"""
app.py - Servidor web da Calculadora de Orçamento
Espaço Bem Me Quer - Garden & Villa
"""

from flask import Flask, render_template, request

app = Flask(__name__)


def formatar_moeda(valor):
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return texto

app.jinja_env.filters["moeda"] = formatar_moeda


# ---------------------------------------------------
# TABELAS DE PREÇO
# ---------------------------------------------------

PRECOS_ESPACO = {
    "garden": {
        100: {"semana": 3200.00, "fds": 4200.00},
        120: {"semana": 3500.00, "fds": 4600.00},
        150: {"semana": 3900.00, "fds": 5100.00},
        180: {"semana": 4300.00, "fds": 5600.00},
        200: {"semana": 4600.00, "fds": 6000.00},
    },
    "villa": {
        100: {"semana": 4100.00, "fds": 5400.00},
        120: {"semana": 4500.00, "fds": 5900.00},
        150: {"semana": 5000.00, "fds": 6500.00},
        180: {"semana": 5500.00, "fds": 7200.00},
        200: {"semana": 5900.00, "fds": 7700.00},
    },
}

PRECO_ALOJAMENTO = {
    "conjunto": 1000.00,
    "individual": 320.00,
}

DESCONTO_ALOJAMENTO = 0.10

PRECO_ACAI = {
    (60, 100): 20.00,
    (101, 150): 17.00,
    (151, 200): 15.00,
}

PRECO_BUFFET_POR_PESSOA = 90.00
PRECO_DJ = 2400.00
PRECO_CABINE_FOTOGRAFICA = 1200.00

NOME_EXTRA = {
    "acai": "Carrinho de Açaí",
    "buffet": "Buffet",
    "dj": "DJ",
    "cabine": "Cabine Fotográfica",
}


# ---------------------------------------------------
# FUNÇÕES DE CÁLCULO
# ---------------------------------------------------

def arredondar_convidados(numero):
    degraus = [100, 120, 150, 180, 200]
    for degrau in degraus:
        if numero <= degrau:
            return degrau
    return 200


def calcular_preco_espacos(espacos_escolhidos, convidados_tier, tipo_dia):
    detalhe = {}
    for espaco in espacos_escolhidos:
        detalhe[espaco] = PRECOS_ESPACO[espaco][convidados_tier][tipo_dia]
    return detalhe


def calcular_preco_alojamento(alojamento_escolha, houve_locacao_espaco):
    mapa = {
        "nenhum": {"conjunto": 0, "individual": 0},
        "conjunto": {"conjunto": 1, "individual": 0},
        "individual": {"conjunto": 0, "individual": 1},
        "ambos": {"conjunto": 1, "individual": 1},
    }
    quantidades = mapa[alojamento_escolha]

    total = 0
    for tipo, quantidade in quantidades.items():
        total += PRECO_ALOJAMENTO[tipo] * quantidade

    desconto_aplicado = False
    if total > 0 and houve_locacao_espaco:
        total = total * (1 - DESCONTO_ALOJAMENTO)
        desconto_aplicado = True

    return total, desconto_aplicado


def calcular_preco_acai(convidados_exato):
    for (inicio, fim), preco_pessoa in PRECO_ACAI.items():
        if convidados_exato >= inicio and convidados_exato <= fim:
            return preco_pessoa * convidados_exato
    return 0  # fora das faixas atendidas


def calcular_preco_buffet(convidados_exato):
    return PRECO_BUFFET_POR_PESSOA * convidados_exato


def calcular_extras(extras_escolhidos, convidados_exato):
    """
    Recebe a lista de extras marcados (ex: ["acai", "dj"]) e devolve
    um dicionário {nome_exibicao: valor} pronto pro ticket.
    """
    detalhe = {}

    if "acai" in extras_escolhidos:
        detalhe[NOME_EXTRA["acai"]] = calcular_preco_acai(convidados_exato)

    if "buffet" in extras_escolhidos:
        detalhe[NOME_EXTRA["buffet"]] = calcular_preco_buffet(convidados_exato)

    if "dj" in extras_escolhidos:
        detalhe[NOME_EXTRA["dj"]] = PRECO_DJ

    if "cabine" in extras_escolhidos:
        detalhe[NOME_EXTRA["cabine"]] = PRECO_CABINE_FOTOGRAFICA

    return detalhe


# ---------------------------------------------------
# ROTAS
# ---------------------------------------------------

@app.route("/")
def pagina_inicial():
    return render_template("index.html", resultado=None, form_data=None, erro=None)


@app.route("/calcular", methods=["POST"])
def calcular():
    convidados_raw = request.form.get("convidados", "")
    dia = request.form.get("dia", "")
    espacos = request.form.getlist("espacos")
    alojamento_escolha = request.form.get("alojamento", "nenhum")
    extras = request.form.getlist("extras")

    form_data = {
        "convidados": convidados_raw,
        "dia": dia,
        "espacos": espacos,
        "alojamento": alojamento_escolha,
        "extras": extras,
    }

    if not convidados_raw or not dia or not espacos:
        return render_template(
            "index.html", resultado=None, form_data=form_data,
            erro="Preencha convidados, dia e ao menos um espaço."
        )

    convidados_exato = int(convidados_raw)
    convidados_tier = arredondar_convidados(convidados_exato)

    espacos_detalhe = calcular_preco_espacos(espacos, convidados_tier, dia)
    total_espacos = sum(espacos_detalhe.values())

    total_alojamento, desconto_aplicado = calcular_preco_alojamento(
        alojamento_escolha, houve_locacao_espaco=len(espacos) > 0
    )

    extras_detalhe = calcular_extras(extras, convidados_exato)
    total_extras = sum(extras_detalhe.values())

    resultado = {
        "convidados_tier": convidados_tier,
        "tipo_dia": dia,
        "espacos_detalhe": espacos_detalhe,
        "total_alojamento": total_alojamento,
        "desconto_aplicado": desconto_aplicado,
        "extras_detalhe": extras_detalhe,
        "total": total_espacos + total_alojamento + total_extras,
    }

    return render_template("index.html", resultado=resultado, form_data=form_data, erro=None)


if __name__ == "__main__":
    app.run(debug=True)
