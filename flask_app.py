from flask import Flask, render_template, request, session, redirect, url_for
import random
from questions import questions
import arabic_reshaper
from bidi.algorithm import get_display

app = Flask(__name__)
app.secret_key = 'your_secret_key_here_change_this'

def reshape_text(text):
    """Correct Arabic text display"""
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/start_quiz')
def start_quiz():
    """Start a new quiz"""
    session['current_question'] = 0
    session['score'] = 0
    session['questions'] = random.sample(questions, len(questions))
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    """Display current question"""
    if 'current_question' not in session:
        return redirect(url_for('index'))
    
    current_q = session['current_question']
    if current_q >= len(session['questions']):
        return redirect(url_for('results'))
    
    question_data = session['questions'][current_q]
    
    # Reshape Arabic text
    question_text = reshape_text(question_data['question'])
    choices = [reshape_text(choice) for choice in question_data['choices']]
    
    return render_template('quiz.html', 
                         question=question_text,
                         choices=choices,
                         question_num=current_q + 1,
                         total_questions=len(session['questions']))

@app.route('/answer', methods=['POST'])
def answer():
    """Process answer"""
    if 'current_question' not in session:
        return redirect(url_for('index'))
    
    user_answer = request.form.get('answer')
    current_q = session['current_question']
    correct_answer = session['questions'][current_q]['answer']
    
    is_correct = user_answer == correct_answer
    if is_correct:
        session['score'] += 1
    
    session['current_question'] += 1
    
    return render_template('answer_feedback.html',
                         is_correct=is_correct,
                         correct_answer=correct_answer,
                         user_answer=user_answer,
                         score=session['score'])

@app.route('/results')
def results():
    """Show final results"""
    if 'score' not in session:
        return redirect(url_for('index'))
    
    score = session['score']
    total = len(questions)
    percentage = (score / total) * 100
    
    return render_template('results.html',
                         score=score,
                         total=total,
                         percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)