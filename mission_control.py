nome_missao = "Aurora-1"
nome_equipe = "Equipe Horizonte"

dados_missao = [
    [22, 94, 91, 98, 93],
    [29, 82, 75, 94, 87],
    [33, 68, 54, 90, 72],
    [36, 51, 42, 86, 61],
    [38, 27, 17, 79, 37],
    [31, 63, 46, 84, 58]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional"
]


def analisar_temperatura(temperatura):
    if temperatura < 18:
        return ["ATENCAO", 1, "Temperatura abaixo do ideal"]
    elif temperatura <= 30:
        return ["NORMAL", 0, "Temperatura estavel"]
    elif temperatura <= 35:
        return ["ATENCAO", 1, "Temperatura elevada"]
    else:
        return ["CRITICO", 2, "Risco de superaquecimento"]


def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return ["CRITICO", 2, "Comunicacao com a base em nivel critico"]
    elif comunicacao < 60:
        return ["ATENCAO", 1, "Comunicacao instavel"]
    else:
        return ["NORMAL", 0, "Comunicacao estavel"]


def analisar_bateria(bateria):
    if bateria < 20:
        return ["CRITICO", 2, "Bateria em nivel critico"]
    elif bateria < 50:
        return ["ATENCAO", 1, "Bateria abaixo do recomendado"]
    else:
        return ["NORMAL", 0, "Energia estavel"]


def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return ["CRITICO", 2, "Oxigenio em nivel critico"]
    elif oxigenio < 90:
        return ["ATENCAO", 1, "Oxigenio abaixo do ideal"]
    else:
        return ["NORMAL", 0, "Oxigenio adequado"]


def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return ["CRITICO", 2, "Estabilidade operacional critica"]
    elif estabilidade < 70:
        return ["ATENCAO", 1, "Estabilidade operacional reduzida"]
    else:
        return ["NORMAL", 0, "Estabilidade operacional adequada"]


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"


def gerar_recomendacao(resultados, pontuacao):
    if pontuacao == 0:
        return "Manter operacao normal e continuar monitoramento."
    elif pontuacao >= 8:
        return "Ativar modo de seguranca e priorizar energia, oxigenio e comunicacao."
    elif resultados[0][0] == "CRITICO":
        return "Verificar controle termico da missao."
    elif resultados[1][0] == "CRITICO":
        return "Tentar restabelecer contato com a base."
    elif resultados[2][0] == "CRITICO":
        return "Ativar modo de economia de energia."
    elif resultados[3][0] == "CRITICO":
        return "Acionar protocolo de suporte a vida."
    elif resultados[4][0] == "CRITICO":
        return "Reduzir operacoes nao essenciais."
    else:
        return "Monitorar sistemas em atencao e preparar plano de contingencia."


def analisar_tendencia(riscos):
    primeiro = riscos[0]
    ultimo = riscos[len(riscos) - 1]

    if ultimo > primeiro:
        return "A missao apresentou tendencia de piora."
    elif ultimo < primeiro:
        return "A missao apresentou tendencia de melhora."
    else:
        return "A missao permaneceu estavel em relacao ao inicio."


def identificar_area_mais_afetada(pontuacao_areas, areas):
    maior_pontuacao = pontuacao_areas[0]
    posicao_maior = 0

    for i in range(1, len(pontuacao_areas)):
        if pontuacao_areas[i] > maior_pontuacao:
            maior_pontuacao = pontuacao_areas[i]
            posicao_maior = i

    return areas[posicao_maior]


def mostrar_linha(nome, valor, unidade, resultado):
    print(nome + ": " + str(valor) + unidade + " | " + resultado[0] + " | " + resultado[2])


print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missao: " + nome_missao)
print("Equipe: " + nome_equipe)
print("Quantidade de ciclos analisados: " + str(len(dados_missao)))
print("=" * 60)

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]
soma_temperatura = 0
soma_comunicacao = 0
soma_bateria = 0
soma_oxigenio = 0
soma_estabilidade = 0
quantidade_ciclos_criticos = 0
maior_risco = -1
ciclo_mais_critico = 0

for i in range(len(dados_missao)):
    ciclo = dados_missao[i]

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    resultado_temperatura = analisar_temperatura(temperatura)
    resultado_comunicacao = analisar_comunicacao(comunicacao)
    resultado_bateria = analisar_bateria(bateria)
    resultado_oxigenio = analisar_oxigenio(oxigenio)
    resultado_estabilidade = analisar_estabilidade(estabilidade)

    resultados = [
        resultado_temperatura,
        resultado_comunicacao,
        resultado_bateria,
        resultado_oxigenio,
        resultado_estabilidade
    ]

    risco_ciclo = 0

    for j in range(len(resultados)):
        risco_ciclo = risco_ciclo + resultados[j][1]
        pontuacao_areas[j] = pontuacao_areas[j] + resultados[j][1]

    riscos_ciclos.append(risco_ciclo)

    soma_temperatura = soma_temperatura + temperatura
    soma_comunicacao = soma_comunicacao + comunicacao
    soma_bateria = soma_bateria + bateria
    soma_oxigenio = soma_oxigenio + oxigenio
    soma_estabilidade = soma_estabilidade + estabilidade

    if risco_ciclo > maior_risco:
        maior_risco = risco_ciclo
        ciclo_mais_critico = i + 1

    if classificar_ciclo(risco_ciclo) == "MISSAO CRITICA":
        quantidade_ciclos_criticos = quantidade_ciclos_criticos + 1

    print()
    print("CICLO " + str(i + 1))
    print("-" * 60)
    mostrar_linha("Temperatura", temperatura, " C", resultado_temperatura)
    mostrar_linha("Comunicacao", comunicacao, "%", resultado_comunicacao)
    mostrar_linha("Bateria", bateria, "%", resultado_bateria)
    mostrar_linha("Oxigenio", oxigenio, "%", resultado_oxigenio)
    mostrar_linha("Estabilidade", estabilidade, "%", resultado_estabilidade)
    print()
    print("Pontuacao de risco do ciclo: " + str(risco_ciclo))
    print("Classificacao do ciclo: " + classificar_ciclo(risco_ciclo))
    print("Recomendacao: " + gerar_recomendacao(resultados, risco_ciclo))

quantidade_ciclos = len(dados_missao)
risco_total = 0

for i in range(len(riscos_ciclos)):
    risco_total = risco_total + riscos_ciclos[i]

risco_medio = risco_total / quantidade_ciclos
area_mais_afetada = identificar_area_mais_afetada(pontuacao_areas, areas_monitoradas)

print()
print("=" * 60)
print("RELATORIO FINAL DA MISSAO")
print("=" * 60)
print("Missao: " + nome_missao)
print("Equipe: " + nome_equipe)
print()
print("Quantidade de ciclos analisados: " + str(quantidade_ciclos))
print()
print("Media de temperatura: " + format(soma_temperatura / quantidade_ciclos, ".2f") + " C")
print("Media de comunicacao: " + format(soma_comunicacao / quantidade_ciclos, ".2f") + "%")
print("Media de bateria: " + format(soma_bateria / quantidade_ciclos, ".2f") + "%")
print("Media de oxigenio: " + format(soma_oxigenio / quantidade_ciclos, ".2f") + "%")
print("Media de estabilidade: " + format(soma_estabilidade / quantidade_ciclos, ".2f") + "%")
print()
print("Ciclo mais critico: Ciclo " + str(ciclo_mais_critico))
print("Maior pontuacao de risco: " + str(maior_risco))
print("Risco medio da missao: " + format(risco_medio, ".2f"))
print("Quantidade de ciclos criticos: " + str(quantidade_ciclos_criticos))
print()
print("Tendencia da missao:")
print(analisar_tendencia(riscos_ciclos))
print()
print("Pontuacao acumulada por area:")
for i in range(len(areas_monitoradas)):
    print(areas_monitoradas[i] + ": " + str(pontuacao_areas[i]) + " pontos")
print()
print("Area mais afetada:")
print(area_mais_afetada)
print()
print("Classificacao final da missao:")
print(classificar_ciclo(risco_medio))
print()
print("Conclusao:")
if risco_medio <= 2:
    print("A missao terminou com baixo nivel de risco e pode continuar em operacao normal.")
elif risco_medio <= 5:
    print("A missao apresentou instabilidade e deve continuar com monitoramento reforcado.")
else:
    print("A missao apresentou risco alto e deve entrar em protocolo de emergencia.")
