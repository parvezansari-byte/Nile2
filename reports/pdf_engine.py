from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import A4


def generate_stock_report(
    symbol,
    price,
    signal,
    score,
    conviction,
    rsi
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    elements = []

    # Title
    title = Paragraph(
        f"<b>{symbol} Institutional Report</b>",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # Summary Table
    data = [
        ["Metric", "Value"],
        ["Current Price", str(price)],
        ["AI Signal", signal],
        ["Institutional Score", f"{score}/100"],
        ["Conviction", conviction],
        ["RSI", str(round(rsi, 2))]
    ]

    table = Table(data)

    table.setStyle(
        TableStyle([

            ("BACKGROUND", (0,0), (-1,0), colors.black),

            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("GRID", (0,0), (-1,-1), 1, colors.grey),

            ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke)

        ])
    )

    elements.append(table)

    elements.append(Spacer(1, 20))

    # Analyst Commentary
    commentary = f"""
    The stock currently has an institutional score of
    {score}/100 with a {signal} recommendation.

    Current conviction level is classified as
    {conviction}.

    RSI indicates current momentum condition at
    {round(rsi, 2)}.
    """

    para = Paragraph(
        commentary,
        styles["BodyText"]
    )

    elements.append(para)

    # Build PDF
    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
