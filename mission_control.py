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
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

def analisar_temperatura(temperatura):
    if temperatura < 18:
        return ["ATENÇÃO", 1, "Temperatura abaixo do ideal"]
    elif temperatura <= 30:
        return ["NORMAL", 0, "Temperatura estável"]
    elif temperatura <= 35:
        return ["ATENÇÃO", 1, "Temperatura elevada"]
    else:
        return ["CRÍTICO", 2, "Risco de superaquecimento"]

def analisar_comunicacao(comunicacao):
    if comunicacao < 30:
        return ["CRÍTICO", 2, "Comunicação com a base em nível crítico"]
    elif comunicacao < 60:
        return ["ATENÇÃO", 1, "Comunicação instável"]
    else:
        return ["NORMAL", 0, "Comunicação estável"]

def analisar_bateria(bateria):
    if bateria < 20:
        return ["CRÍTICO", 2, "Bateria em nível crítico"]
    elif bateria < 50:
        return ["ATENÇÃO", 1, "Bateria abaixo do recomendado"]
    else:
        return ["NORMAL", 0, "Energia estável"]

def analisar_oxigenio(oxigenio):
    if oxigenio < 80:
        return ["CRÍTICO", 2, "Oxigênio em nível crítico"]
    elif oxigenio < 90:
        return ["ATENÇÃO", 1, "Oxigênio abaixo do ideal"]
    else:
        return ["NORMAL", 0, "Oxigênio adequado"]

def analisar_estabilidade(estabilidade):
    if estabilidade < 40:
        return ["CRÍTICO", 2, "Estabilidade operacional crítica"]
    elif estabilidade < 70:
        return ["ATENÇÃO", 1, "Estabilidade operacional reduzida"]
    else:
        return ["NORMAL", 0, "Estabilidade operacional adequada"]

def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(resultados, pontuacao):
    if pontuacao == 0:
        return "Manter operação normal e continuar monitoramento."
    elif pontuacao >= 8:
        return "Ativar modo de segurança e priorizar energia, oxigênio e comunicação."
    elif resultados[0][0] == "CRÍTICO":
        return "Verificar controle térmico da missão."
    elif resultados[1][0] == "CRÍTICO":
        return "Tentar restabelecer contato com a base."
    elif resultados[2][0] == "CRÍTICO":
        return "Ativar modo de economia de energia."
    elif resultados[3][0] == "CRÍTICO":
        return "Acionar protocolo de suporte à vida."
    elif resultados[4][0] == "CRÍTICO":
        return "Reduzir operações não essenciais."
    else:
        return "Monitorar sistemas em atenção e preparar plano de contingência."

def analisar_tendencia(riscos):
    primeiro = riscos[0]
    ultimo = riscos[len(riscos) - 1]

    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."

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
print("Missão: " + nome_missao)
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

    if classificar_ciclo(risco_ciclo) == "MISSÃO CRÍTICA":
        quantidade_ciclos_criticos = quantidade_ciclos_criticos + 1

    print()
    print("CICLO " + str(i + 1))
    print("-" * 60)
    mostrar_linha("Temperatura", temperatura, " °C", resultado_temperatura)
    mostrar_linha("Comunicação", comunicacao, "%", resultado_comunicacao)
    mostrar_linha("Bateria", bateria, "%", resultado_bateria)
    mostrar_linha("Oxigênio", oxigenio, "%", resultado_oxigenio)
    mostrar_linha("Estabilidade", estabilidade, "%", resultado_estabilidade)
    print()
    print("Pontuação de risco do ciclo: " + str(risco_ciclo))
    print("Classificação do ciclo: " + classificar_ciclo(risco_ciclo))
    print("Recomendação: " + gerar_recomendacao(resultados, risco_ciclo))

quantidade_ciclos = len(dados_missao)
risco_total = 0

for i in range(len(riscos_ciclos)):
    risco_total = risco_total + riscos_ciclos[i]

risco_medio = risco_total / quantidade_ciclos
area_mais_afetada = identificar_area_mais_afetada(pontuacao_areas, areas_monitoradas)

print()
print("=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)
print("Missão: " + nome_missao)
print("Equipe: " + nome_equipe)

print()
print("Quantidade de ciclos analisados: " + str(quantidade_ciclos))
print()

print("Média de temperatura: " + format(soma_temperatura / quantidade_ciclos, ".2f") + " °C")
print("Média de comunicação: " + format(soma_comunicacao / quantidade_ciclos, ".2f") + "%")
print("Média de bateria: " + format(soma_bateria / quantidade_ciclos, ".2f") + "%")
print("Média de oxigênio: " + format(soma_oxigenio / quantidade_ciclos, ".2f") + "%")
print("Média de estabilidade: " + format(soma_estabilidade / quantidade_ciclos, ".2f") + "%")
print()

print("Ciclo mais crítico: Ciclo " + str(ciclo_mais_critico))
print("Maior pontuação de risco: " + str(maior_risco))
print("Risco médio da missão: " + format(risco_medio, ".2f"))
print("Quantidade de ciclos críticos: " + str(quantidade_ciclos_criticos))

print()
print("Tendência da missão:")
print(analisar_tendencia(riscos_ciclos))
print()

print("Pontuação acumulada por área:")
for i in range(len(areas_monitoradas)):
    print(areas_monitoradas[i] + ": " + str(pontuacao_areas[i]) + " pontos")

print()
print("Área mais afetada:")
print(area_mais_afetada)
print()

print("Classificação final da missão:")
print(classificar_ciclo(risco_medio))
print()

print("Conclusão:")
if risco_medio <= 2:
    print("A missão terminou com baixo nível de risco e pode continuar em operação normal.")
elif risco_medio <= 5:
    print("A missão apresentou instabilidade e deve continuar com monitoramento reforçado.")
else:
    print("A missão apresentou risco alto e deve entrar em protocolo de emergência.")
