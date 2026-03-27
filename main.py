from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Context processor para disponibilizar a data atual em todos os templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Aqui você pode processar os dados
    print(f"📧 Email recebido: {email}")
    print(f"🔒 Senha recebida: {password}")
    
    # Redireciona para a página home após o submit
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)