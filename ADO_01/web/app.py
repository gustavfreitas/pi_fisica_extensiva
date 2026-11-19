import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="ADO 01 - Lançamento de Projéteis", page_icon="🚀", layout="wide")


def mostrar_html(html, altura):
    """Mostra um trecho de HTML/JS (compatível com versões novas e antigas do Streamlit)."""
    if hasattr(st, "iframe"):
        st.iframe(html, height=altura)
    else:
        components.html(html, height=altura, scrolling=True)

X0 = 0.0  # posição x inicial fixa em zero


# ---------------------------------------------------------------------------
# NÚCLEO DE FÍSICA (fórmulas analíticas fechadas)
# ---------------------------------------------------------------------------
def calcular_resultados(v0, alpha, y0, g):
    theta = np.radians(alpha)
    # Equação (3): tempo de voo
    termo_raiz = (v0 * np.sin(theta)) ** 2 + 2 * g * y0
    tvoo = (v0 * np.sin(theta) + np.sqrt(termo_raiz)) / g
    # Equação (4): altura máxima
    ymax = y0 + ((v0 * np.sin(theta)) ** 2) / (2 * g)
    # Equação (5): alcance horizontal total
    R = X0 + v0 * np.cos(theta) * tvoo
    return tvoo, ymax, R


def calcular_trajetoria(v0, alpha, y0, g, tvoo):
    theta = np.radians(alpha)
    t = np.linspace(0, tvoo, 200)
    # Equações (1) e (2)
    x = X0 + v0 * np.cos(theta) * t
    y = y0 + v0 * np.sin(theta) * t - 0.5 * g * t**2
    return t, x, y


def rotulo(cfg):
    v0, alpha, y0, _ = cfg
    return rf"$v_0$={v0:.0f} | $\theta$={alpha:.0f}° | $y_0$={y0:.0f}"


# ---------------------------------------------------------------------------
# FIGURAS
# ---------------------------------------------------------------------------
def montar_figura(historico, atual=None, destaque=None):
    """Desenha as trajetórias salvas, a configuração atual (tracejada)
    e, opcionalmente, o ponto de destaque (projétil)."""
    fig, ax = plt.subplots(figsize=(9, 4.6), dpi=72)
    maxs_x, maxs_y = [10.0], [10.0]

    for cfg in historico:
        tv, ym, R = calcular_resultados(*cfg)
        _, x, y = calcular_trajetoria(*cfg, tv)
        ax.plot(x, y, lw=1.5, alpha=0.8, label=rotulo(cfg))
        maxs_x.append(R)
        maxs_y.append(ym)

    if atual is not None:
        tv, ym, R = calcular_resultados(*atual)
        _, x, y = calcular_trajetoria(*atual, tv)
        ax.plot(x, y, lw=2.5, color="blue", linestyle="--", label="Configuração atual")
        maxs_x.append(R)
        maxs_y.append(ym)

    ponto = None
    if destaque is not None:
        ponto, = ax.plot([], [], "ro", ms=8, zorder=5)

    ax.set_xlabel("Distância horizontal - X (m)")
    ax.set_ylabel("Altura - Y (m)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_xlim(0, max(maxs_x) * 1.1)
    ax.set_ylim(0, max(maxs_y) * 1.1)
    ax.set_aspect("equal", adjustable="datalim")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    return fig, ax, ponto


def gerar_animacao(historico, cfg):
    """Gera a animação do último lançamento como HTML (roda 100% no navegador)."""
    tv, _, _ = calcular_resultados(*cfg)
    _, x, y = calcular_trajetoria(*cfg, tv)
    idx = np.linspace(0, len(x) - 1, 48).astype(int)

    fig, ax, ponto = montar_figura(historico, destaque=True)
    ax.set_title(f"Último lançamento: {len(historico)} trajetória(s) no gráfico", fontsize=10)

    def atualizar(i):
        k = idx[i]
        ponto.set_data([x[k]], [y[k]])
        return (ponto,)

    anim = animation.FuncAnimation(fig, atualizar, frames=len(idx), interval=40, blit=False)
    html = anim.to_jshtml(fps=25, default_mode="once")
    plt.close(fig)
    return html


# ---------------------------------------------------------------------------
# ESTADO
# ---------------------------------------------------------------------------
if "historico" not in st.session_state:
    st.session_state.historico = []
if "anim_html" not in st.session_state:
    st.session_state.anim_html = None


def acao_lancar():
    cfg = (
        float(st.session_state.v0),
        float(st.session_state.alpha),
        float(st.session_state.y0),
        float(st.session_state.g),
    )
    st.session_state.historico.append(cfg)
    st.session_state.anim_html = gerar_animacao(st.session_state.historico, cfg)


def acao_limpar():
    st.session_state.historico = []
    st.session_state.anim_html = None


# ---------------------------------------------------------------------------
# INTERFACE
# ---------------------------------------------------------------------------
st.title("🚀 ADO 01 · Lançamento de Projéteis")
st.caption(
    "Movimento parabólico no caso ideal (sem resistência do ar), calculado por fórmulas "
    "analíticas fechadas. Ajuste os parâmetros e clique em **Lançar**."
)

with st.sidebar:
    st.header("Parâmetros")
    st.slider("v₀ — velocidade inicial (m/s)", 5.0, 150.0, 50.0, 1.0, key="v0")
    st.slider("θ — ângulo de lançamento (°)", 1.0, 89.0, 45.0, 1.0, key="alpha")
    st.slider("y₀ — altura inicial (m)", 0.0, 50.0, 10.0, 1.0, key="y0")
    st.slider("g — gravidade (m/s²)", 1.6, 24.8, 9.81, 0.01, key="g")
    c1, c2 = st.columns(2)
    c1.button("🚀 Lançar", on_click=acao_lancar, type="primary")
    c2.button("🧹 Limpar", on_click=acao_limpar)
    st.caption("Referências de g: Lua ≈ 1,6 · Terra ≈ 9,81 · Júpiter ≈ 24,8")

atual = (
    float(st.session_state.v0),
    float(st.session_state.alpha),
    float(st.session_state.y0),
    float(st.session_state.g),
)
tvoo, ymax, R = calcular_resultados(*atual)

m1, m2, m3 = st.columns(3)
m1.metric("Alcance R", f"{R:.2f} m")
m2.metric("Altura máxima y_max", f"{ymax:.2f} m")
m3.metric("Tempo de voo t_voo", f"{tvoo:.2f} s")

st.subheader("Pré-visualização")
fig, _, _ = montar_figura(st.session_state.historico, atual)
st.pyplot(fig)
plt.close(fig)

if st.session_state.anim_html:
    st.subheader("Animação do último lançamento")
    mostrar_html(st.session_state.anim_html, 560)

with st.expander("Equações utilizadas"):
    st.latex(r"x(t) = x_0 + v_0\cos\theta\,t")
    st.latex(r"y(t) = y_0 + v_0\sin\theta\,t - \tfrac{1}{2}g\,t^2")
    st.latex(r"t_{voo} = \dfrac{v_0\sin\theta + \sqrt{(v_0\sin\theta)^2 + 2gy_0}}{g}")
    st.latex(r"y_{max} = y_0 + \dfrac{(v_0\sin\theta)^2}{2g}")
    st.latex(r"R = x_0 + v_0\cos\theta\,t_{voo}")
