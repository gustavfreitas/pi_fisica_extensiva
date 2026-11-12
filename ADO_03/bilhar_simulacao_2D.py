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

# 3. Interface, Renderização, Controle
fig, ax = plt.subplots(figsize=(10, 7))
fig.canvas.manager.set_window_title("Jogo de Sinuca em Python")
ax.set(xlim=(0, LARGURA_MESA), ylim=(0, ALTURA_MESA))
ax.set_aspect('equal')
ax.set_facecolor('#0f5e1e')
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.25) # Abre espaço para os controles

# Criação do Widget (Taco)
ax_ang = plt.axes([0.1, 0.12, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_forca = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_btn = plt.axes([0.8, 0.05, 0.15, 0.1])

slider_ang = Slider(ax_ang, 'Ângulo (°)', 0, 360, valinit=0, valstep=1)
slider_forca = Slider(ax_forca, 'Força', 5, 40, valinit=20)
btn_tacada = Button(ax_btn, 'Dar Tacada!', color='lightblue', hovercolor='0.975')

# Desenho dos Elementos Gráficos -
for c in cacapas: ax.add_patch(plt.Circle(c, RAIO_CACAPA, color='black', zorder=2))

cores = ['white', 'yellow', 'blue', 'red', 'purple', 'orange', 'green', 'maroon', 
         'black', 'yellow', 'blue', 'red', 'purple', 'orange', 'green', 'maroon']
bolas_graficas, textos = [], []

for i in range(16):
    b = plt.Circle(pos[i], RAIO, color=cores[i], zorder=5)
    if i > 8: b.set_edgecolor('white'); b.set_linewidth(3)
    ax.add_patch(b); bolas_graficas.append(b)
    
    num = "" if i == 0 else str(i)
    cor_texto = 'white' if i in [2, 3, 4, 7, 8] else 'black'
    txt = ax.text(pos[i,0], pos[i,1], num, color=cor_texto, ha='center', va='center', fontsize=8, fontweight='bold', zorder=6)
    textos.append(txt)

# Linhas visuais do Taco e da Mira
linha_taco, = ax.plot([], [], color='#8b4513', lw=5, zorder=6, solid_capstyle='round') # Marrom
linha_mira, = ax.plot([], [], color='white', lw=1, ls='--', zorder=4)
