# Mission Control AI

Projeto da disciplina Pensamento Computacional e Automação com Python.

## Objetivo

O programa simula o monitoramento de uma missão espacial experimental. Ele analisa ciclos da missão, gera alertas, calcula o risco de cada ciclo, identifica tendência, mostra a área mais afetada e exibe um relatório final no terminal.

## Arquivos

- `mission_control.py`: código principal do projeto.
- `README.md`: explicação do projeto e das regras usadas.

## Dados usados

O programa usa uma matriz chamada `dados_missao`.

Cada linha representa um ciclo da missão.

Cada ciclo segue esta ordem:

```text
[temperatura, comunicação, bateria, oxigênio, estabilidade]
```

As áreas monitoradas são:

```text
Temperatura interna
Comunicação com a base
Sistema de energia
Suporte de oxigênio
Estabilidade operacional
```

## Regras de classificação

### Temperatura

- Menor que 18 °C: ATENÇÃO
- De 18 °C até 30 °C: NORMAL
- Maior que 30 °C até 35 °C: ATENÇÃO
- Maior que 35 °C: CRÍTICO

### Comunicação

- Menor que 30%: CRÍTICO
- De 30% até 59%: ATENÇÃO
- 60% ou mais: NORMAL

### Bateria

- Menor que 20%: CRÍTICO
- De 20% até 49%: ATENÇÃO
- 50% ou mais: NORMAL

### Oxigênio

- Menor que 80%: CRÍTICO
- De 80% até 89%: ATENÇÃO
- 90% ou mais: NORMAL

### Estabilidade

- Menor que 40%: CRÍTICO
- De 40% até 69%: ATENÇÃO
- 70% ou mais: NORMAL

## Pontuação de risco

- NORMAL: 0 ponto
- ATENÇÃO: 1 ponto
- CRÍTICO: 2 pontos

Cada ciclo possui 5 informações monitoradas. Por isso, a pontuação máxima de um ciclo é 10 pontos.

## Classificação do ciclo

- 0 a 2 pontos: MISSÃO ESTÁVEL
- 3 a 5 pontos: MISSÃO EM ATENÇÃO
- 6 a 10 pontos: MISSÃO CRÍTICA

## Funções criadas

O código possui mais de 5 funções, como exigido:

- `analisar_temperatura()`
- `analisar_comunicacao()`
- `analisar_bateria()`
- `analisar_oxigenio()`
- `analisar_estabilidade()`
- `classificar_ciclo()`
- `gerar_recomendacao()`
- `analisar_tendencia()`
- `identificar_area_mais_afetada()`
- `mostrar_linha()`

## Como executar

No terminal, dentro da pasta do projeto, execute:

```bash
python mission_control.py
```

## Informações do projeto

Nome da missão: Aurora-1

Nome da equipe: Equipe Horizonte

Integrantes:

- Gabriel Castilla Cavaloti

Link do repositório GitHub:

- https://github.com/GabrielCavaloti/mission-control-ai
