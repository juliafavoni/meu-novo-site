import random

# 1. Código Base do Jogo
# Definindo as posições das escadas e serpentes

# Escadas: base -> topo
escadas = {
    3: 16,
    5: 7,
    15: 25,
    18: 20,
    21: 23
}

# Serpentes: cabeça -> cauda
serpentes = {
    12: 2,
    14: 11,
    17: 4,
    31: 19,
    35: 22
}

def jogar_dado():
    return random.randint(1, 6)

def simular_jogo(prob_sobe_escada=1.0, registrar_quedas=False, contar_lancamentos=False, pos_inicial_bruno=1, imunidade_primeira_serpente=False):
    #Simula uma partida entre Ana (inicia) e Bruno
    pos_ana = 1
    pos_bruno = pos_inicial_bruno
    turno = 0 # 0 para Ana, 1 para Bruno
    quedas_serpentes = 0
    total_lancamentos = 0
    imunidade_bruno = imunidade_primeira_serpente # True se Bruno tem uma cobra de imunidade

    while True:
        jogador = "Ana" if turno % 2 == 0 else "Bruno"
        if jogador == "Ana":
            pos_ana += jogar_dado()
            total_lancamentos += 1
            if pos_ana in escadas and random.random() < prob_sobe_escada:
                pos_ana = escadas[pos_ana]
            elif pos_ana in serpentes:
                pos_ana = serpentes[pos_ana]
                if registrar_quedas:
                    quedas_serpentes += 1
            if pos_ana >= 36:
                return ("Ana", quedas_serpentes, total_lancamentos)
        else:
            pos_bruno += jogar_dado()
            total_lancamentos += 1
            if pos_bruno in escadas and random.random() < prob_sobe_escada:
                pos_bruno = escadas[pos_bruno]
            elif pos_bruno in serpentes:
                if imunidade_bruno:
                    imunidade_bruno = False
                else:
                    pos_bruno = serpentes[pos_bruno]
                    if registrar_quedas:
                        quedas_serpentes += 1
            if pos_bruno >= 36:
                return ("Bruno", quedas_serpentes, total_lancamentos)

        turno += 1

# Pergunta 1: Probabilidade de vitória de quem começa

total_jogos = 10000
vitorias = {"Ana": 0, "Bruno": 0}

for _ in range(total_jogos):
    vencedor, _, _ = simular_jogo()
    vitorias[vencedor] += 1

prob_ana = vitorias["Ana"] / total_jogos
prob_bruno = vitorias["Bruno"] / total_jogos

print("----- Pergunta 1 -----")
print(f"Probabilidade de vitória de quem começa (Ana):")
print(f"Ana venceu {vitorias['Ana']} vezes. ({prob_ana:.2%})")
print(f"Bruno venceu {vitorias['Bruno']} vezes. ({prob_bruno:.2%})")

# Pergunta 2: Média de quedas em serpentes por jogo

quedas_total = 0

for _ in range(total_jogos):
    _, quedas, _ = simular_jogo(registrar_quedas=True)
    quedas_total += quedas

media_quedas = quedas_total / total_jogos

print("\n----- Pergunta 2 -----")
print(f"Média de quedas em serpentes por jogo: {media_quedas:.2f}")

# Pergunta 3: Escadas com 50% de chance de subir

lancamentos_total_100 = 0
lancamentos_total_50 = 0

for _ in range(total_jogos):
    _, _, lancamentos_100 = simular_jogo(prob_sobe_escada=1.0, contar_lancamentos=True)
    lancamentos_total_100 += lancamentos_100

    _, _, lancamentos_50 = simular_jogo(prob_sobe_escada=0.5, contar_lancamentos=True)
    lancamentos_total_50 += lancamentos_50

media_lancamentos_100 = lancamentos_total_100 / total_jogos
media_lancamentos_50 = lancamentos_total_50 / total_jogos

print("\n----- Pergunta 3 -----")
print(f"Média de lançamentos para vencer com 50% de chance de subir escadas: {media_lancamentos_50:.2f}")
print(f"Comparação com 100% de chance de subir escadas:")
print(f"Média de lançamentos para vencer com 100% de chance de subir escadas: {media_lancamentos_100:.2f}")

# Pergunta 4: Probabilidade de vitória de Bruno começando em outra casa
print("\n----- Pergunta 4 -----")
print(f"{'Posição Bruno':>14} | {'Vitórias Ana (%)':>16} | {'Vitórias Bruno (%)':>18} | {'Diferença (%)':>15}")
print("-" * 70)

melhor_posicao = 1
menor_diferenca = float("inf")

for pos in range(1, 36):  # Testar posições iniciais de Bruno de 1 a 35
    vitorias_temp = {"Ana": 0, "Bruno": 0}

    for _ in range(10000):
        vencedor, _, _ = simular_jogo(prob_sobe_escada=1.0, pos_inicial_bruno=pos)
        vitorias_temp[vencedor] += 1

    prob_ana = vitorias_temp["Ana"] / 10000
    prob_bruno = vitorias_temp["Bruno"] / 10000
    diferenca = abs(prob_ana - prob_bruno)

    print(f"{pos:>14} | {prob_ana * 100:>16.2f} | {prob_bruno * 100:>18.2f} | {diferenca * 100:>15.2f}")

    if diferenca < menor_diferenca:
        menor_diferenca = diferenca
        melhor_posicao = pos

print(f"\n➡️  A posição inicial mais justa para Bruno é: {melhor_posicao} (diferença de {menor_diferenca * 100:.2f}% nas vitórias)")

# Pergunta 5: Probabilidade de vitória com imunidade na primeira cobra do Bruno

total_jogos = 10000
vitorias = {"Ana": 0, "Bruno": 0}

for _ in range(total_jogos):
    vencedor, _, _ = simular_jogo(prob_sobe_escada=1.0, imunidade_primeira_serpente=True)
    vitorias[vencedor] += 1

prob_ana = vitorias["Ana"] / total_jogos
prob_bruno = vitorias["Bruno"] / total_jogos

print("\n----- Pergunta 5 -----")
print(f"Com imunidade para Bruno na primeira cobra:")
print(f"Ana venceu {vitorias['Ana']} vezes. ({prob_ana:.2%})")
print(f"Bruno venceu {vitorias['Bruno']} vezes. ({prob_bruno:.2%})")