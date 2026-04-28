# Lúcio Roger - Advogados Associados 🏛️

Website institucional e Landing Page desenvolvidos em Flask para o escritório de advocacia fictício "Lúcio Roger".
O projeto possui um design *dark mode premium*, inspirado em referências modernas, projetado para transmitir autoridade e focar na alta conversão de clientes.

## 🚀 Funcionalidades
- **Site Institucional (`/`):** Página inicial completa com seções informativas sobre "O Escritório", "Áreas de Atuação" e perfil da "Nossa Equipe".
- **Landing Page de Campanha (`/campanha`):** Uma página agressiva para tráfego pago, sem distrações no cabeçalho e totalmente focada em levar o cliente ao WhatsApp.
- **Design Responsivo:** Layout flexível que se adapta perfeitamente a smartphones, tablets e desktops.
- **Botões Flutuantes e CTA:** Forte apelo à ação via integração nativa com o WhatsApp.

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, JavaScript Vanilla
- **Servidor Web:** Waitress (preparado para produção)
- **Design System:** Fontes do Google (Inter e Playfair Display) e paleta baseada em tons escuros e dourado.

## 📦 Como Executar o Projeto Localmente

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/UendelHenrique/law-firm-site.git
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd law-firm-site
   ```

3. **Instale as dependências necessárias:**
   ```bash
   py -m pip install -r requirements.txt
   ```
   *(Nota: Dependendo do sistema operacional, você pode precisar usar `python` em vez de `py`).*

4. **Inicie o servidor local:**
   ```bash
   py app.py
   ```

5. **Acesse no seu navegador:**
   - Site Principal: [http://localhost:5000/](http://localhost:5000/)
   - Landing Page: [http://localhost:5000/campanha](http://localhost:5000/campanha)
