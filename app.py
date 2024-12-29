from flask import Flask, render_template, request, redirect, url_for, send_file
from dotenv import load_dotenv
import os
from utils.pdf_processor import extract_pdf_content
from utils.openai_api import generate_question_paper
from utils.pdf_generator import create_question_paper_pdf

app = Flask(__name__)

# Configure file upload folder
UPLOAD_FOLDER = 'uploads/'
OUTPUT_FOLDER = 'outputs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure upload/output folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Handle uploaded file
    uploaded_file = request.files['syllabus_pdf']
    if uploaded_file.filename != '':
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        # Extract syllabus content
        syllabus_content = extract_pdf_content(file_path)

        # Get other form data
        school_name = request.form['school_name']
        exam_name = request.form['exam_name']
        subject_name = request.form['subject_name']
        class_name = request.form['class']
        marks = request.form['marks']
        section=request.form['section']
        weightage=request.form['weightage']
        # Generate question paper using ChatGPT
        structured_data = {
            "school_name": school_name,
            "exam_name": exam_name,
            "subject_name": subject_name,
            "class": class_name,
            "marks": marks,
            "syllabus": syllabus_content,
            "section": section,
            "weightage": weightage or ''
        }
        question_paper = generate_question_paper(structured_data)

        # Generate a PDF for the question paper
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], "question_paper.pdf")
        create_question_paper_pdf(structured_data, question_paper, output_path)
        
        # Serve the generated PDF
        return send_file(output_path, as_attachment=True)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

