from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def criar_relatorio_pdf(filename="relatorio_ado3_colisoes.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    styles = getSampleStyleSheet()

    # Estilos customizados
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=16, leading=20, alignment=1, textColor=colors.HexColor('#1A365D'))
    subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=14, alignment=1, textColor=colors.HexColor('#4A5568'))
    h1_style = ParagraphStyle('H1Style', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=15, textColor=colors.HexColor('#1A365D'), spaceBefore=10, spaceAfter=6)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#2D3748'), spaceBefore=3, spaceAfter=3)

    elements = []

    # Cabeçalho
    elements.append(Paragraph("Relatório Acadêmico - ADO 3: Física Práticas Extensivas", title_style))
    elements.append(Paragraph("Curso: Ciência da Computação | Opção Escolhida: A (Colisões Elásticas)", subtitle_style))
    elements.append(Spacer(1, 15))

    # Q1. Cálculos à mão para a Situação Padrão (Caso 1)
    elements.append(Paragraph("Q1. Cálculos Manuais das Velocidades (Caso 1)", h1_style))
    p1 = (
        "Parâmetros iniciais: m1 = 1.0 kg, m2 = 1.0 kg, v1 = 4.0 m/s e v2 = 0 m/s.<br/>"
        "Aplicando a equação fechada de colisão elástica para u1:<br/>"
        "u1 = [(1 - 1)*4.0 + 2*1*0] / (1 + 1) = 0 / 2 = <b>0 m/s</b>.<br/>"
        "Aplicando a equação para u2:<br/>"
        "u2 = [(1 - 1)*0 + 2*1*4.0] / (1 + 1) = 8.0 / 2 = <b>4.0 m/s</b>.<br/>"
        "Esses valores batem exatamente com o painel em tempo real da aplicação construída."
    )
    elements.append(Paragraph(p1, body_style))

    # Q2. Conservação do Momento
    elements.append(Paragraph("Q2. Conservação do Momento Linear", h1_style))
    p2 = (
        "Momento antes (p_antes) = 1.0 * 4.0 + 1.0 * 0 = <b>4.0 kg.m/s</b>.<br/>"
        "Momento depois (p_depois) = 1.0 * 0 + 1.0 * 4.0 = <b>4.0 kg.m/s</b>.<br/>"
        "Portanto, p_antes = p_depois. O momento se conserva mesmo em colisões inelásticas porque o sistema formado pelos dois blocos é <b>isolado na direção horizontal</b>. "
        "Como não há forças externas atuantes (apenas as forças internas de contato, que se anulam pela 3ª Lei de Newton), a variação do momento total é nula."
    )
    elements.append(Paragraph(p2, body_style))

    # Q3. Energia Cinética
    elements.append(Paragraph("Q3. Variação da Energia Cinética e Redistribuição", h1_style))
    p3 = (
        "K_antes = 0.5 * 1.0 * (4.0)² = <b>8.0 J</b>. | K_depois = 0.5 * 1.0 * (4.0)² = <b>8.0 J</b>. Logo, ΔK = 0 J (perfeitamente elástica).<br/><br/>"
        "<b>Redistribuição de energia:</b><br/>"
        "• <b>Caso 1 (Massas iguais):</b> O bloco m1 para totalmente (u1=0) e transfere 100% de sua energia cinética para m2, que arranca com a velocidade original do projétil.<br/>"
        "• <b>Caso 2 (Alvo pesado):</b> O projétil m1 bate em uma parede de massa (m2=4kg). Ele volta (recua) retendo parte da energia, enquanto o alvo pesado avança lentamente com a energia restante.<br/>"
        "• <b>Caso 3 (Projétil pesado):</b> O projétil m1 (4kg) funciona como um 'trator'. Ele amassa a pequena massa m2, seguindo em frente sem perder muito embalo, enquanto m2 ganha mais energia e é disparado violentamente para a frente."
    )
    elements.append(Paragraph(p3, body_style))

    # Q4. Impulso e Força Média
    elements.append(Paragraph("Q4. Impulso e Análise da Força Média", h1_style))
    p4 = (
        "Usando o Teorema do Impulso (Caso 1):<br/>"
        "J1 = m1*(u1 - v1) = 1.0*(0 - 4.0) = <b>-4.0 N.s</b>.<br/>"
        "J2 = m2*(u2 - v2) = 1.0*(4.0 - 0) = <b>4.0 N.s</b>.<br/>"
        "Verifica-se perfeitamente que J1 = -J2, respeitando a ação e reação.<br/>"
        "Para Δt = 10 ms (0.01 s): <b>F_med = |J1| / Δt = 4.0 / 0.01 = 400 N</b>.<br/>"
        "Se o tempo de contato for 10x maior (100 ms ou 0.1 s): <b>F_med = 4.0 / 0.1 = 40 N</b>. "
        "A Força Média diminui dez vezes. Isso explica o princípio de funcionamento dos <i>airbags</i> automotivos e materiais de amortecimento: ao se prolongar o tempo (Δt) da transferência de momento durante uma colisão, o pico de Força Média destrutiva cai drasticamente."
    )
    elements.append(Paragraph(p4, body_style))

    # Q5. Análise do Sinal da Velocidade
    elements.append(Paragraph("Q5. Explicação do Sinal da Velocidade (Termo m1 - m2)", h1_style))
    p5 = (
        "Na equação da colisão elástica com o alvo em repouso (v2 = 0), a velocidade final do projétil se reduz à fração: <b>u1 = v1 * (m1 - m2) / (m1 + m2)</b>.<br/>"
        "• <b>No Caso 2 (m1 < m2):</b> O termo (m1 - m2) resulta num valor negativo (1 - 4 = -3). O numerador inteiro fica negativo, forçando u1 a ser menor que zero (u1 < 0). Por isso o projétil recua (volta).<br/>"
        "• <b>No Caso 3 (m1 > m2):</b> O termo (m1 - m2) resulta num valor positivo (4 - 1 = 3). O numerador é positivo, forçando u1 a ser maior que zero (u1 > 0). Por isso o projétil massivo supera a inércia do alvo leve e segue em frente."
    )
    elements.append(Paragraph(p5, body_style))

    doc.build(elements)
    print("Relatório ADO 3 gerado com sucesso!")

if __name__ == "__main__":
    criar_relatorio_pdf()
