# 🤖 AI.PRODUTORA - DNA CONTENT ENGINE

Uma plataforma de produção de conteúdo autónomo para influenciadores gerados por Inteligência Artificial.

## 🧬 O Conceito "DNA Engine"
Diferente de geradores genéricos, este sistema utiliza **Análise Multimodal** para processar 3 vídeos de referência do cliente. O motor de IA extrai:
1. **Estética:** Cores, iluminação e enquadramento.
2. **Voz:** Oratória, tom e cadência da fala.
3. **Ritmo:** Estilo de edição e cortes.

## 🚀 Funcionalidades
- **Treinamento de Persona:** Clonagem de espírito criativo através de vídeo.
- **Produção Automática:** Geração de Reels, Stories e Posts de forma autónoma.
- **Painel de Controlo:** Dashboard moderno para gestão de planos e agendamentos.

## 🛠️ Tecnologias
- **Frontend:** HTML5, Tailwind CSS, JavaScript.
- **Backend:** Flask + Python (Google Generative AI, OpenAI, Gemini Pro).
- **Deployment:** Vercel (Serverless Functions).
- **Pipeline:** Automação de postagem via Make.com.

## 📈 Como Executar

### Configuração Local
1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure a variável de ambiente `GOOGLE_API_KEY`:
   ```bash
   cp .env.example .env
   # Edite .env e adicione sua Google API Key
   ```
4. Execute o servidor Flask:
   ```bash
   python api/index.py
   ```
5. Acesse http://localhost:5000 no navegador.

### Deployment na Vercel
1. Instale a Vercel CLI:
   ```bash
   npm i -g vercel
   ```
2. Configure as variáveis de ambiente no dashboard da Vercel:
   - `GOOGLE_API_KEY`: Sua chave da API do Google Generative AI
3. Deploy:
   ```bash
   vercel --prod
   ```

## 🔑 APIs Necessárias
- **Google Generative AI**: Obtenha sua chave em https://makersuite.google.com/app/apikey
