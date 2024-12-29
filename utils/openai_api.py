import openai
from dotenv import load_dotenv
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_question_paper(data):
    prompt = f"""
    Generate a question paper with the following details:
    School: {data['school_name']}
    Exam: {data['exam_name']}
    Subject: {data['subject_name']}
    Class: {data['class']}
    Marks: {data['marks']}
    Syllabus: {data['syllabus']}
    School Name: Tejasvi vidhyaranya
    Sections: {data['section']}
    weightage of assessment: {data['weightage'] or ''}


follow below instructions and guidelines and structure properly :-

* Guidelines for Question Formation:*
#Engagement and Humor:
-Every question must include humor or a funny, relatable context. Use nursery rhymes, jokes, or creative scenarios to make questions engaging. Ensure students feel encouraged to learn while enjoying the test. For example, use funny metaphors (e.g., "Imagine your math book turned into a superhero").

#Socio-Economic Background:
-Student belongs to Hyderabad Habsiguda .Questions should reflect the daily life, environment, and struggles of middle or lower-middle-class students. Consider that students’ parents may not be highly educated, and they may have limited resources. Use examples from common, everyday experiences that students can relate to (e.g., local foods, everyday chores, community life). In subjects like Math, integrate relatable scenarios like shopping, budgeting, and daily activities that reflect their socio-economic background.

#Language Simplicity:
-Use clear and simple language that is easy to understand and appropriate for the grade level. Avoid overly complex terms and explanations. The language should cater to the student’s comprehension level and be engaging.

#Learning with Fun:
-The assessment should teach core concepts while fostering curiosity and creativity. Questions should encourage students to think deeply but in a fun, relaxed way, allowing them to connect learning with real-world experiences.

#Difficulty Levels:
-Ensure that the difficulty levels of questions are balanced across sections:
20% Easy questions
50% Medium questions
30% Hard questions

#don't give chapter reference in questions.

* Types of Questions and Structure:*

#Multiple Choice Questions (MCQs):

-1  marks per question
- ensure options and question both follow guidelines.
-Follow the question formation guidelines:
  Every question should be asked in simple language. every question contain engagement and humour. topic used in every question formed are from their syllabus given.Focused on learning and fun
below element should be divided in according to their weightage
    funny element + socio economic background relevance questions = 60%
    Relatable example + socio economic background relavance question= 20%
    Funny elements + nursery rhymes questions relevance = 20%

- form 1 question of MCQ where 2 statements are given and in option give like. i) statement 1 correct statement 2 wrong. ii) Statement 2 correct statement 1 wrong. iii) both correct iv) both wrong.


#Fill in the Blanks:

-1  marks per question
-Follow the question formation guidelines:
  Every question should be asked in simple language. every question contain engagement and humour.topic used in every question formed are from their syllabus given. Focused on learning and fun
below element should be divided in according to their weightage
    funny element + socio economic background relevance questions = 60%
    Relatable example + socio economic background relavance question= 20%
    Funny elements + nursery rhymes questions relevance = 20%
-Include hints to every fill in the blanks to  make the questions engaging and relatable.

#Match the Following:

-1 mark per question
- Don't give correct selection in front of the question asked. 
-Follow the question formation guidelines:
  Every question should be asked in simple language. every question contain engagement and humour.topic used in every question formed are from their syllabus given. Focused on learning and fun
below element should be divided in according to their weightage
    funny element + socio economic background relevance questions = 60%
    Relatable example + socio economic background relavance question= 20%
    Funny elements + nursery rhymes questions relevance = 20%

#True/False:

-1 mark per question
-Follow the question formation guidelines:
  Every question should be asked in simple language. every question contain engagement and humour.topic used in every question formed are from their syllabus given. Focused on learning and fun
below element should be divided in according to their weightage
    funny element + socio economic background relevance questions = 60%
    Relatable example + socio economic background relavance question= 20%
    Funny elements + nursery rhymes questions relevance = 20%

#Reverse Qestions (give answer ask to make question)

-1 mark per question
- give the answer and for making question give one blank space .

#short answer question.

-2 mark per question
-Follow the question formation guidelines:
  Every question should be asked in simple language. every question contain engagement and humour. topic used in every question formed are from their syllabus given.Focused on learning and fun
below element should be divided in according to their weightage.
    funny element + socio economic background relevance questions = 60%
    Relatable example + socio economic background relavance question= 20%
    Funny elements + nursery rhymes questions relevance = 20%

#long answer question.

-5 mark per question
-Follow the question formation guidelines, ensuring that humor, socio-economic relevance , funnny element , Nursery rhymes and engagement are in every question. topic used in every question formed are from their syllabus given.



#Dreaming Questions:

-5  marks per question
-These questions should encourage students to imagine themselves in various  roles, such as a superhero, Power Rangers, doremon , doctor, teacher, Prime Minister etc. The scenarios should relate to their syllabus given  and inspire creativity and problem-solving.



Paper Structure:

Header:

-Include the school name, exam name, class, subject, and total marks in bold and large fonts at the top of the paper.

-Example:
School Name
Exam Name
Class: 
Subject: 
Total Marks:

Marks Division:
Adjust the number of questions and their difficulty level according to the total marks. Ensure the sum of the marks for each section aligns with the total marks.

Answers Section:
Attach the answers at the end of the paper. 

* Steps for Implementation:*
-Input the assessment details based on the school, exam, subject, class, and total marks.
-Follow the question formation guidelines, ensuring that humor, socio-economic relevance , funnny element , Nursery rhymes and engagement are incorporated.
-Adjust the difficulty levels of questions according to the provided guidelines (50% easy, 30% medium, 20% hard).
-Ensure the paper structure is correctly followed and the number of questions adds up to the total marks.
-Provide an answer key at the end of the assessment
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a question paper generator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
