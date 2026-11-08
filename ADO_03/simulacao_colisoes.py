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

