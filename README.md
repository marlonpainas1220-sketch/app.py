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
- **Backend:** Python (OpenAI, Gemini Pro, Creatomate).
- **Pipeline:** Automação de postagem via Make.com.

## 📈 Como Executar

### Execução Local
1. Clone este repositório.
2. Abra o `index.htm` em qualquer navegador para ver o Dashboard.
3. Execute `python api/index.py` para simular o motor de IA.

### Deployment no Vercel
1. Instale o Vercel CLI: `npm i -g vercel`
2. Execute `vercel` na raiz do projeto para fazer deploy.
3. A estrutura está organizada para Vercel Serverless:
   - `/api/index.py` - Função serverless principal
   - `requirements.txt` - Dependências Python
   - `vercel.json` - Configuração de deployment
