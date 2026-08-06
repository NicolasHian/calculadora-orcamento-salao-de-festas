"""
Calculadora de Orçamento - Salão de Festas (Garden + Villa)
V1 - Terminal
"""

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
    "conjunto": 1000.00,   # 30 camas, valor por unidade / 24h
    "individual": 320.00,  # até 4 pessoas, valor por unidade / 24h
    "conjunto + individual": 1320.00
}

DESCONTO_ALOJAMENTO = 0.10  # 10% de desconto no alojamento se combinado com o espaço


# ---------------------------------------------------
# FUNÇÕES
# ---------------------------------------------------

def pegar_convidados():
    numero_de_convidados = int(input("Numeros de convidados (Limitado a 200)"))
    degraus = [100, 120, 150, 180, 200] 
    for degrau in degraus:
        if numero_de_convidados  <= degrau:
            return degrau
          
    print("O Limite e 200")  
    return 200      
   


def pegar_tipo_dia():
    Dias = {
        1: ("Segunda-feira","semana"),
        2: ("Terça-feira","semana"),
        3: ("Quarta-feira","semana"),
        4: ("Quinta-feira","semana"),
        5: ("Sexta-feira","semana"),
        6: ("Sabado","fds"),
        7: ("Domingo","fds"), 
    }
    for numero, (nome_dia, tipo) in Dias.items():
        print(f"{numero} - {nome_dia}")
    Dia = int(input("Selecione 1 a 7 conforme o dia desejado"))
    resultado = Dias[Dia][1]
    return resultado



def pegar_espacos():
    espacos = {
        1: ["Garden"],
        2: ["Villa"],
        3: ["Villa + Garden"]
    }
    for numero, nome in espacos.items():
        print(numero, "-", nome)
    
    escolha = int(input("selecione uma opçao"))
    
    if escolha == 1:
        resultado = ["garden"]
    elif escolha == 2:
        resultado = ["villa"]
    else:
        resultado = ["garden", "villa"]
    
    return resultado
   

def pegar_alojamentos():
    alojamentos = {
        1: ("Alojamento 30 camas "),
        2: ("alojamentos de 4 quartos"),
        3:("Combo dos dois alojamentos ")
    }
    for numero, nome in alojamentos.items():
        print(numero,"-", nome)
    escolha = int(input("selecione uma opçao de 1 a 3:"))
    if escolha == 1:
        resultado = {"conjunto": 1, "individual": 0}
    elif escolha == 2:
        resultado ={"conjunto": 0, "individual": 1}
    else:
        resultado ={"conjunto": 1, "individual": 1}

    return resultado    
     
def calcular_preco_espacos(espacos_escolhidos, convidados_tier, tipo_dia):
        total = 0
        for espaco in espacos_escolhidos:
            preco = PRECOS_ESPACO[espaco][convidados_tier][tipo_dia]
            total = total + preco
        return total



def calcular_preco_alojamento(alojamentos_escolhidos, houve_locacao_espaco):

    total = 0
    for tipo, quantidade in alojamentos_escolhidos.items():
        preco = PRECO_ALOJAMENTO[tipo] * quantidade
        total = total + preco
    if houve_locacao_espaco:
        total = total * (1 - DESCONTO_ALOJAMENTO)
    return total  



def exibir_orcamento(espacos_escolhidos, convidados_tier, tipo_dia,
                      alojamentos_escolhidos, total_espacos,
                      total_alojamento):
    print("==== ORÇAMENTO =====")
    print("Quantidade de convidados:",convidados_tier)
    print("Dias", tipo_dia)
    print("Espaços escolhidos", espacos_escolhidos)
    print("total dos espaços", total_espacos)
    print("alojamentos escolhidos", alojamentos_escolhidos)
    print("total dos alojamentos",total_alojamento)
    total = total_alojamento + total_espacos
    print("valor total=",total)
    #===== ORÇAMENTO =====
    #Convidados: até 150
    #Dia: Fim de semana/feriado
    #Espaço(s): Garden, Villa
      #Garden: R$ 5100.00
     # Villa: R$ 6500.00
    #Alojamento:
      #Conjunto x1: R$ 1000.00
      #Individual x2: R$ 640.00
     # (desconto de 10% aplicado)
    #----------------------
    #TOTAL: R$ ...
    

# ---------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------

def main():
    print("=== Calculadora de Orçamento - Garden e Villa ===\n")

    convidados_tier = pegar_convidados()
    tipo_dia = pegar_tipo_dia()
    espacos_escolhidos = pegar_espacos()
    alojamentos_escolhidos = pegar_alojamentos()

    total_espacos = calcular_preco_espacos(
        espacos_escolhidos, convidados_tier, tipo_dia
    )

    # houve locação de espaço = a lista de espaços não está vazia
    houve_locacao_espaco = len(espacos_escolhidos) > 0

    total_alojamento = calcular_preco_alojamento(
        alojamentos_escolhidos, houve_locacao_espaco
    )

    exibir_orcamento(
        espacos_escolhidos, convidados_tier, tipo_dia,
        alojamentos_escolhidos, total_espacos, total_alojamento
    )


if __name__ == "__main__":
    main()