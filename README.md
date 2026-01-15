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
- **Backend:** Python (Flask, OpenAI, Gemini Pro, Creatomate).
- **APIs:** OpenAI GPT-3.5/GPT-4 para geração de conteúdo inteligente.
- **Pipeline:** Automação de postagem via Make.com.

## ⚙️ Configuração da API OpenAI

### 1. Obter Chave de API
1. Acesse [OpenAI Platform](https://platform.openai.com/api-keys)
2. Faça login ou crie uma conta
3. Gere uma nova chave de API

### 2. Configurar Variáveis de Ambiente

**Opção A: Desenvolvimento Local**
1. Copie o arquivo de exemplo:
   ```bash
   cp .env.example .env
   ```
2. Edite o arquivo `.env` e adicione sua chave:
   ```
   OPENAI_API_KEY=sk-sua-chave-aqui
   ```

**Opção B: Deploy no Vercel**
1. Acesse o dashboard do seu projeto no Vercel
2. Vá em Settings → Environment Variables
3. Adicione a variável:
   - Name: `OPENAI_API_KEY`
   - Value: `sk-sua-chave-aqui`
   - Environment: Production, Preview, Development

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

## 📈 Como Executar

### Interface Web (Dashboard)
1. Abra o `index.htm` em qualquer navegador para ver o Dashboard.

### Exemplo OpenAI (Standalone)
Execute o exemplo de integração com OpenAI:
```bash
python openai_example.py
```

Este script demonstra:
- Uso básico da API OpenAI (Completion e Chat)
- Geração de roteiro personalizado baseado em perfil
- Tratamento de erros e verificação de configuração

### API Flask (Backend)
Execute o servidor Flask localmente:
```bash
python api/index.py
```

Ou execute o script standalone:
```bash
python main.py
```

### Endpoints da API

**GET /** - Status da API
```bash
curl http://localhost:5000/
```

**POST /api/processar-dna** - Processar DNA do influencer
```bash
curl -X POST http://localhost:5000/api/processar-dna \
  -H "Content-Type: application/json" \
  -d '{"videos": ["estetica.mp4", "voz.mp4", "ritmo.mp4"]}'
```

**POST /api/gerar-conteudo** - Gerar conteúdo com OpenAI
```bash
curl -X POST http://localhost:5000/api/gerar-conteudo \
  -H "Content-Type: application/json" \
  -d '{
    "tema": "Tendências de Moda IA 2026",
    "perfil": {
      "estilo": "High-Energy / Futurista",
      "voz": "Frequência média, sotaque neutro",
      "ritmo_corte": "1.2 segundos por transição"
    }
  }'
```

## 🔒 Segurança
- **Nunca** commite o arquivo `.env` no repositório
- Use variáveis de ambiente para armazenar credenciais
- O arquivo `.env` já está incluído no `.gitignore`
- Para produção, configure as variáveis diretamente no Vercel

## 📝 Notas
- A API OpenAI requer créditos (trial ou paid account)
- Modelos recomendados: `gpt-3.5-turbo` ou `gpt-4`
- O sistema funciona em modo simulação se a chave não estiver configurada
