import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# 1. Configuração da Mesa, Bolas e Caçapas
LARGURA_MESA, ALTURA_MESA = 10.0, 5.0
RAIO = 0.2
RAIO_CACAPA = 0.35
DT = 0.02

cacapas = np.array([
    [0, 0], [LARGURA_MESA/2, 0], [LARGURA_MESA, 0],
    [0, ALTURA_MESA], [LARGURA_MESA/2, ALTURA_MESA], [LARGURA_MESA, ALTURA_MESA]
])

pos = np.zeros((16, 2))
vel = np.zeros((16, 2))
ativa = np.ones(16, dtype=bool)

# Posicionamento Inicial
pos[0] = [2.5, 2.5] # Bola Branca
start_x, start_y = 7.0, 2.5
idx = 1
for linha in range(5):
    for coluna in range(linha + 1):
        x = start_x + linha * (RAIO * np.sqrt(3))
        y = start_y + (coluna - linha/2) * (RAIO * 2.05)
        pos[idx] = [x, y]
        idx += 1

# Variaveís de Controle do Jogo
estado_jogo = "ESPERANDO" # Pode ser "ESPERANDO" ou "ROLANDO"

# 2. Motor Físico 2D
def resolver_colisoes():
    global pos, vel, ativa, estado_jogo
    
    vel[ativa] *= 0.992 # Atrito da mesa
    pos[ativa] += vel[ativa] * DT
    
    # Verifica se todas as bolas pararam para liberar o taco novamente
    velocidade_maxima = np.max(np.linalg.norm(vel[ativa], axis=1)) if np.any(ativa) else 0
    if velocidade_maxima < 0.2 and estado_jogo == "ROLANDO":
        vel[ativa] = 0 # Zera completamente para evitar micro-movimentos
        if ativa[0]:   # Se a branca não caiu na caçapa
            estado_jogo = "ESPERANDO"
    
    # Regras das Caçapas e Bordas
    for i in range(16):
        if not ativa[i]: continue
            
        for c in cacapas:
            if np.linalg.norm(pos[i] - c) < RAIO_CACAPA:
                ativa[i] = False
                vel[i] = [0, 0]
                pos[i] = [-10, -10]
                
                # Regra básica: Se a branca cair, ela volta para a posição inicial
                if i == 0:
                    pos[0] = [2.5, 2.5]
                    ativa[0] = True
                break
                
        if not ativa[i]: continue

        if pos[i, 0] - RAIO < 0:
            pos[i, 0] = RAIO; vel[i, 0] *= -1
        elif pos[i, 0] + RAIO > LARGURA_MESA:
            pos[i, 0] = LARGURA_MESA - RAIO; vel[i, 0] *= -1
            
        if pos[i, 1] - RAIO < 0:
            pos[i, 1] = RAIO; vel[i, 1] *= -1
        elif pos[i, 1] + RAIO > ALTURA_MESA:
            pos[i, 1] = ALTURA_MESA - RAIO; vel[i, 1] *= -1

    # Colisão entre Bolas
    for i in range(16):
        if not ativa[i]: continue
        for j in range(i + 1, 16):
            if not ativa[j]: continue
                
            vetor_dist = pos[i] - pos[j]
            dist = np.linalg.norm(vetor_dist)
            
            if dist < 2 * RAIO:
                n = vetor_dist / dist
                sobreposicao = 2 * RAIO - dist
                pos[i] += n * (sobreposicao / 2)
                pos[j] -= n * (sobreposicao / 2)
                
                v_relativa = vel[i] - vel[j]
                v_norm = np.dot(v_relativa, n)
                
                if v_norm < 0:
                    impulso = v_norm * n
                    vel[i] -= impulso
                    vel[j] += impulso
