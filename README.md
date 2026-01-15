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

## ⚙️ Configuração

### Variáveis de Ambiente
1. Copie o arquivo `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```

2. Configure sua chave da API OpenAI no arquivo `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

**Nota:** A aplicação funciona em modo simulado se a `OPENAI_API_KEY` não estiver configurada, permitindo testes sem necessidade de uma chave válida.

## 📈 Como Executar
1. Clone este repositório.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente (opcional para modo simulado).
4. Abra o `index.html` em qualquer navegador para ver o Dashboard.
5. Execute `python main.py` para simular o motor de IA.
6. Ou execute `python api/index.py` para iniciar a API Flask.
