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

# 4. ELEMENTOS VISUAIS E LÓGICA DE ANIMAÇÃO

bloco1 = patches.Rectangle((0, 0), 1, 1, fc='blue', alpha=0.8)
bloco2 = patches.Rectangle((0, 0), 1, 1, fc='red', alpha=0.8)
ax_anim.add_patch(bloco1)
ax_anim.add_patch(bloco2)

tempo_texto = ax_anim.text(0.02, 0.85, '', transform=ax_anim.transAxes, fontsize=12)

estado = {"t_anim": 0.0, "pausado": False, "t_colisao": 0.0, "fisica": {}}

def atualizar_fisica(val=None):
    m1, m2 = sl_m1.val, sl_m2.val
    v1, v2 = sl_v1.val, sl_v2.val
    dt_ms = sl_dt.val
    
    estado["fisica"] = calcular_fisica(m1, m2, v1, v2, dt_ms)
    estado["t_anim"] = 0.0
    
    # Tamanho visual dinâmico proporcional à raiz da massa
    w1, w2 = np.sqrt(m1), np.sqrt(m2)
    bloco1.set_width(w1); bloco1.set_height(w1)
    bloco2.set_width(w2); bloco2.set_height(w2)
    
    # Posições iniciais fixas
    x1_0, x2_0 = 0.0, 8.0 
    
    # R5. Verifica se haverá colisão
    if not estado["fisica"]["colisao"]:
        texto_resultados.set_text("NÃO HÁ COLISÃO (v1 <= v2).\nO projétil nunca alcançará o alvo.")
        texto_resultados.set_color("red")
        ax_bar_p.clear(); ax_bar_k.clear()
        estado["t_colisao"] = float('inf')
        return

    # Instante da colisão (distância entre centros = soma das meias larguras)
    distancia_choque = (w1 + w2) / 2.0
    v_relativa = v1 - v2
    # Compensando os centros geométricos dos retângulos (x é o canto inferior esquerdo)
    estado["t_colisao"] = (x2_0 - x1_0 - w1) / v_relativa 

    f = estado["fisica"]
    
    # R3. Painel de Resultados
    res = (
        f"--- RESULTADOS EM TEMPO REAL ---\n\n"
        f"VELOCIDADES:\n"
        f"  Antes: v1 = {v1:.2f} m/s | v2 = {v2:.2f} m/s\n"
        f"  Depois: u1 = {f['u1']:.2f} m/s | u2 = {f['u2']:.2f} m/s\n\n"
        f"MOMENTO LINEAR (kg.m/s):\n"
        f"  Antes = {f['p_antes']:.2f} | Depois = {f['p_depois']:.2f}\n\n"
        f"ENERGIA CINÉTICA (J):\n"
        f"  Antes = {f['k_antes']:.2f} | Depois = {f['k_depois']:.2f}\n"
        f"  Variação (ΔK) = {f['delta_k']:.2f} J\n\n"
        f"DINÂMICA DE IMPACTO:\n"
        f"  Impulso J1 = {f['j1']:.2f} N.s\n"
        f"  Impulso J2 = {f['j2']:.2f} N.s\n"
        f"  Força Média (F_med) = {f['f_med']:.2f} N\n"
    )
    texto_resultados.set_text(res)
    texto_resultados.set_color("black")
    
    # R4. Gráficos de Barras
    ax_bar_p.clear()
    ax_bar_p.bar(['Antes', 'Depois'], [f['p_antes'], f['p_depois']], color='orange')
    ax_bar_p.set_title("Momento (p)")
    
    ax_bar_k.clear()
    ax_bar_k.bar(['Antes', 'Depois'], [f['k_antes'], f['k_depois']], color='green')
    ax_bar_k.set_title("Energia (K)")

# Vincula o evento dos sliders à função de atualização
for sl in [sl_m1, sl_m2, sl_v1, sl_v2, sl_dt]:
    sl.on_changed(atualizar_fisica)

def ao_selecionar_caso(label):
    if label == 'Caso 1: Massas Iguais':
        sl_m1.set_val(1.0); sl_m2.set_val(1.0); sl_v1.set_val(4.0)
    elif label == 'Caso 2: Alvo Pesado':
        sl_m1.set_val(1.0); sl_m2.set_val(4.0); sl_v1.set_val(5.0)
    elif label == 'Caso 3: Projétil Pesado':
        sl_m1.set_val(4.0); sl_m2.set_val(1.0); sl_v1.set_val(5.0)
    sl_v2.set_val(0.0) # O roteiro fixa v2 = 0 para os 3 casos
radio.on_clicked(ao_selecionar_caso)

def pausar(event):
    estado["pausado"] = not estado["pausado"]
    btn_pause.label.set_text('Continuar' if estado["pausado"] else 'Pausar')
btn_pause.on_clicked(pausar)

def reiniciar(event):
    estado["t_anim"] = 0.0
btn_reset.on_clicked(reiniciar)

# Loop de Animação (R1)
def animar(frame):
    if estado["pausado"] or not estado["fisica"].get("colisao", False):
        return bloco1, bloco2, tempo_texto

    t = estado["t_anim"]
    tc = estado["t_colisao"]
    x1_0, x2_0 = 0.0, 8.0
    v1, v2 = sl_v1.val, sl_v2.val
    
    if t < tc:
        x1 = x1_0 + v1 * t
        x2 = x2_0 + v2 * t
    else:
        u1, u2 = estado["fisica"]["u1"], estado["fisica"]["u2"]
        x1_tc = x1_0 + v1 * tc
        x2_tc = x2_0 + v2 * tc
        x1 = x1_tc + u1 * (t - tc)
        x2 = x2_tc + u2 * (t - tc)
        
    bloco1.set_xy((x1, 0))
    bloco2.set_xy((x2, 0))
    tempo_texto.set_text(f'Tempo: {t:.2f} s')
    
    estado["t_anim"] += 0.05
    if x1 > 20 or x2 > 20: # Reinicia o ciclo se sair da tela
        estado["t_anim"] = 0.0

    return bloco1, bloco2, tempo_texto

# Inicializa o sistema
atualizar_fisica()
anim = FuncAnimation(fig, animar, interval=30, blit=True)

plt.show()
