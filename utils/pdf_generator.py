from fpdf import FPDF

def create_question_paper_pdf(data, question_paper, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add header
    pdf.cell(200, 10, txt=f"{data['school_name']} - {data['exam_name']}", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Subject: {data['subject_name']} | Class: {data['class']} | Marks: {data['marks']}", ln=True, align='C')
    pdf.ln(10)

    # Add question paper content
    pdf.multi_cell(0, 10, txt=question_paper)

    # Save PDF
    pdf.output(output_path)
