import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.patches as patches

# 1. NÚCLEO DE FÍSICA (FÓRMULAS FECHADAS)

def calcular_fisica(massa_1, massa_2, velocidade_1, velocidade_2, dt_ms):
    # R5. Tratamento de caso sem colisão
    if velocidade_1 <= velocidade_2:
        return {"colisao": False}
    
    # Colisão Elástica (Fórmulas da Seção 2 do roteiro)
    u1 = ((massa_1 - massa_2) * velocidade_1 + 2 * massa_2 * velocidade_2) / (massa_1 + massa_2)
    u2 = ((massa_2 - massa_1) * velocidade_2 + 2 * massa_1 * velocidade_1) / (massa_1 + massa_2)
    
    # Momento Linear
    p_antes = massa_1 * velocidade_1 + massa_2 * velocidade_2
    p_depois = massa_1 * u1 + massa_2 * u2
    
    # Energia Cinética
    k_antes = 0.5 * massa_1 * (velocidade_1**2) + 0.5 * massa_2 * (velocidade_2**2)
    k_depois = 0.5 * massa_1 * (u1**2) + 0.5 * massa_2 * (u2**2)
    delta_k = k_depois - k_antes
    
    # Impulso e Força Média
    j1 = massa_1 * (u1 - velocidade_1)
    j2 = massa_2 * (u2 - velocidade_2)
    dt_s = dt_ms / 1000.0
    f_med = abs(j1) / dt_s if dt_s > 0 else 0
    
    return {
        "colisao": True,
        "u1": u1, "u2": u2,
        "p_antes": p_antes, "p_depois": p_depois,
        "k_antes": k_antes, "k_depois": k_depois, "delta_k": delta_k,
        "j1": j1, "j2": j2, "f_med": f_med
    }

# 2. CONFIGURAÇÃO DA INTERFACE (MATPLOTLIB)

fig = plt.figure(figsize=(14, 8))
fig.canvas.manager.set_window_title("ADO 3 - Colisões Elásticas (Opção A)")

# Eixos da Animação
ax_anim = plt.axes([0.05, 0.7, 0.6, 0.25])
ax_anim.set_xlim(-2, 20)
ax_anim.set_ylim(-2, 2)
ax_anim.set_yticks([])
ax_anim.set_title("Animação da Colisão Unidimensional", fontweight='bold')
ax_anim.axhline(0, color='black', lw=2) # Chão

# Eixos dos Gráficos de Barras
ax_bar_p = plt.axes([0.75, 0.7, 0.08, 0.25])
ax_bar_k = plt.axes([0.88, 0.7, 0.08, 0.25])

# Eixo do Painel de Resultados
ax_text = plt.axes([0.45, 0.05, 0.5, 0.55])
ax_text.axis('off')
texto_resultados = ax_text.text(0.05, 0.9, "", fontsize=11, family='monospace', va='top')


# 3. WIDGETS (SLIDERS, RADIOBUTTONS E BOTÕES)

cor_slider = 'lightgoldenrodyellow'

ax_m1 = plt.axes([0.1, 0.55, 0.25, 0.03], facecolor=cor_slider)
ax_m2 = plt.axes([0.1, 0.50, 0.25, 0.03], facecolor=cor_slider)
ax_v1 = plt.axes([0.1, 0.45, 0.25, 0.03], facecolor=cor_slider)
ax_v2 = plt.axes([0.1, 0.40, 0.25, 0.03], facecolor=cor_slider)
ax_dt = plt.axes([0.1, 0.35, 0.25, 0.03], facecolor=cor_slider)

sl_m1 = Slider(ax_m1, 'm1 (kg)', 0.1, 10.0, valinit=1.0)
sl_m2 = Slider(ax_m2, 'm2 (kg)', 0.1, 10.0, valinit=1.0)
sl_v1 = Slider(ax_v1, 'v1 (m/s)', 0.0, 15.0, valinit=4.0)
sl_v2 = Slider(ax_v2, 'v2 (m/s)', 0.0, 10.0, valinit=0.0)
sl_dt = Slider(ax_dt, 'Δt (ms)', 1.0, 100.0, valinit=10.0)

ax_radio = plt.axes([0.1, 0.15, 0.25, 0.15], facecolor=cor_slider)
radio = RadioButtons(ax_radio, ('Caso 1: Massas Iguais', 'Caso 2: Alvo Pesado', 'Caso 3: Projétil Pesado'))

ax_btn_reset = plt.axes([0.1, 0.05, 0.1, 0.05])
ax_btn_pause = plt.axes([0.25, 0.05, 0.1, 0.05])
btn_reset = Button(ax_btn_reset, 'Reiniciar', hovercolor='0.975')
btn_pause = Button(ax_btn_pause, 'Pausar', hovercolor='0.975')
