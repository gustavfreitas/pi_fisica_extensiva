from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def criar_relatorio_pdf(filename="relatorio_fisica.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Estilos customizados
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=18, leading=22, alignment=1, textColor=colors.HexColor('#1A365D'))
    subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=14, alignment=1, textColor=colors.HexColor('#4A5568'))
    h1_style = ParagraphStyle('H1Style', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor('#1A365D'), spaceBefore=12, spaceAfter=6)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#2D3748'), spaceBefore=4, spaceAfter=4)

    elements = []

    # Cabeçalho
    elements.append(Paragraph("Relatório Acadêmico - ADO 2: Física Aplicada", title_style))
    elements.append(Paragraph("Curso: Ciência da Computação | Disciplina: Mecânica e Física Moderna", subtitle_style))
    elements.append(Spacer(1, 15))

    # 1. Equações e Derivação do Plano Inclinado
    elements.append(Paragraph("1. Equações Utilizadas e Lógica de Implementação (Sistema 3.1)", h1_style))
    p1_text = (
        "<b>Derivação da aceleração (a) do Plano Inclinado:</b><br/>"
        "Com base no algoritmo atualizado, a lógica foi condensada utilizando as variáveis dinâmicas <i>Massa_1</i>, <i>Massa_2</i> e <i>Angulo</i>. "
        "A Força Normal (N) e a Força Motriz foram definidas vetorialmente como:<br/>"
        "N = Massa_1 * G * cos(θ)<br/>"
        "F_motriz = Massa_2 * G - Massa_1 * G * sin(θ)<br/><br/>"
        "O script utiliza um operador ternário para definir o estado de movimento. A variável <i>Movimento_Uniforme</i> atua como o coeficiente de atrito (μ):<br/>"
        "<b>a = 0 se |F_motriz| <= Movimento_Uniforme * N, caso contrário:</b><br/>"
        "<b>a = [F_motriz - Movimento_Uniforme * N * sinal(F_motriz)] / (Massa_1 + Massa_2)</b><br/><br/>"
        "As grandezas cinemáticas seguem a integração direta no tempo do MRUV: Posição = 0.5 * a * t² e Velocidade = a * t."
    )
    elements.append(Paragraph(p1_text, body_style))
    elements.append(Spacer(1, 10))

    # Equações dos outros sistemas
    p_eq_outros = (
        "<b>Fórmulas Fechadas - Sistemas 3.2 e 3.3:</b><br/>"
        "• <b>Força Centrípeta (MCU):</b> ω = Velocidade / Raio | x(t) = Raio*cos(ωt) | y(t) = Raio*sin(ωt) | Fc = Massa * Velocidade² / Raio<br/>"
        "• <b>Arrasto Linear:</b> v_term = (Massa * G) / Coeficiente | v(t) = v_term * (1 - e^(-t / (Massa / Coeficiente)))<br/>"
        "• <b>Arrasto Quadrático:</b> v_term = √((Massa * G) / Coeficiente) | v(t) = v_term * tanh((G * t) / v_term)"
    )
    elements.append(Paragraph(p_eq_outros, body_style))
    elements.append(Spacer(1, 15))

    # 2. Análise do Coeficiente Crítico de Atrito
    elements.append(Paragraph("2. Determinação do Ponto Crítico de Atrito", h1_style))
    p2_text = (
        "Fixando os parâmetros padrão da simulação (Massa_1 = 5.0, Massa_2 = 7.0, Angulo = 30°):<br/>"
        "F_motriz = 7.0 * 9.81 - 5.0 * 9.81 * sin(30°) = 68.67 - 24.525 = 44.145 N.<br/>"
        "Força Normal (N) = 5.0 * 9.81 * cos(30°) = 42.48 N.<br/><br/>"
        "O sistema entra em repouso quando a condição do operador ternário é satisfeita (|F_motriz| <= Movimento_Uniforme * N). "
        "Logo, o valor crítico para o slider <i>Movimento_Uniforme</i> é calculado por:<br/>"
        "<b>Movimento_Uniforme_critico = 44.145 / 42.48 ≈ 1.039</b><br/><br/>"
        "Na interface gráfica da aplicação, ao deslizar <i>Movimento_Uniforme</i> para um valor maior que 1.04, a aceleração exibida na tela zera automaticamente, validando perfeitamente a lógica computacional implementada."
    )
    elements.append(Paragraph(p2_text, body_style))
    elements.append(Spacer(1, 15))

    # 3. Comparação Arrasto Linear vs Quadrático
    elements.append(Paragraph("3. Comparação da Velocidade Terminal no Arrasto", h1_style))
    p3_text = (
        "O algoritmo calcula a velocidade terminal de duas formas distintas, dependendo do seletor da interface:<br/>"
        "• <b>Linear:</b> O corpo sofre desaceleração estritamente proporcional à velocidade, utilizando a função exponencial do NumPy (np.exp). A curva apresenta uma transição mais suave desde o início do movimento.<br/>"
        "• <b>Quadrático:</b> A resistência escala com o quadrado da velocidade, modelada pela tangente hiperbólica (np.tanh). A queda inicial acompanha o comportamento de queda livre (G * t), mas sofre uma saturação muito mais abrupta ao se aproximar de v_term.<br/><br/>"
        "A renderização gráfica através do Matplotlib confirma visualmente que ambas as funções assintóticas estabilizam na linha tracejada (v_term), com distanciamento claro em relação à queda livre ideal."
    )
    elements.append(Paragraph(p3_text, body_style))
    elements.append(Spacer(1, 15))

    # 4. Discussão de Aplicação no Mundo Real
    elements.append(Paragraph("4. Aplicações Práticas e Modelagem Computacional", h1_style))
    p4_text = (
        "1. <b>Plano Inclinado:</b> A lógica do operador ternário emula sistemas automatizados de pontes rolantes e elevadores industriais, garantindo que os motores apenas atuem se a tração vencer a zona de atrito estático.<br/>"
        "2. <b>Força Centrípeta:</b> As equações de trajetória (x, y) aplicadas sobre o vetor de tempo simulam a dinâmica de satélites e são os mesmos cálculos vetoriais usados em motores de física (Game Engines) para estabilidade direcional.<br/>"
        "3. <b>Força de Arrasto:</b> O seletor linear/quadrático reflete a modelagem aerodinâmica, permitindo diferenciar fluidos densos e viscosos (comportamento linear) do impacto do ar em alta velocidade (comportamento quadrático)."
    )
    elements.append(Paragraph(p4_text, body_style))

    doc.build(elements)
    print("Relatório gerado com sucesso com base nas novas variáveis da simulação!")

if __name__ == "__main__":
    criar_relatorio_pdf()