from flask import Flask, render_template

app = Flask(__name__)

# Informações globais para os templates
config = {
    "nome_advogado": "Lúcio Roger",
    "nome_escritorio": "Lúcio Roger Advogados Associados",
    "whatsapp_numero": "5511999999999",
    "email_contato": "contato@lucioroger.com.br",
    "endereco": "Av. Paulista, 1000 - Bela Vista, São Paulo - SP",
    "instagram": "https://instagram.com/luciorogeradv",
    "linkedin": "https://linkedin.com/in/lucioroger"
}

@app.context_processor
def inject_config():
    return dict(config=config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/campanha')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
