import csv
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors


def read_and_analyze_data(file_path):
    data = []
    total_units = 0
    total_revenue = 0

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data.append(header)

        for row in reader:
            units = int(row[2])
            revenue = float(row[3])

            total_units += units
            total_revenue += revenue
            data.append(row)

    return data, total_units, total_revenue


def generate_pdf_report(data, total_units, total_revenue, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Sales Analysis Report", styles['Title']))

    # Summary
    elements.append(Paragraph(
        f"<b>Total Units Sold:</b> {total_units}<br/>"
        f"<b>Total Revenue:</b> ${total_revenue:,.2f}",
        styles['Normal']
    ))

    elements.append(Paragraph("<br/>Detailed Sales Data:", styles['Heading2']))

    # Table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (2, 1), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
    ]))

    elements.append(table)

    doc.build(elements)


if __name__ == "__main__":
    input_file = "sales_data.csv"
    output_file = "sales_report.pdf"

    data, total_units, total_revenue = read_and_analyze_data(input_file)
    generate_pdf_report(data, total_units, total_revenue, output_file)

    print("PDF report generated successfully!")
