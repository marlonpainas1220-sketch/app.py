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
- **Backend:** Python Flask (OpenAI, Gemini Pro, Creatomate).
- **Deploy:** Vercel (Serverless Functions).
- **Pipeline:** Automação de postagem via Make.com.

## 📋 Pré-requisitos

Antes de realizar o deploy, certifique-se de ter:
- Conta no [Vercel](https://vercel.com) (gratuita)
- [Vercel CLI](https://vercel.com/docs/cli) instalado (opcional, para deploy via terminal)
- Python 3.9+ instalado (para testes locais)
- Git instalado

## 🚀 Deploy no Vercel

### Método 1: Deploy via Interface Web (Recomendado)

1. **Prepare o Repositório**
   - Certifique-se de que o código está no GitHub, GitLab ou Bitbucket
   - O repositório deve conter os arquivos `vercel.json` e `requirements.txt`

2. **Importar Projeto no Vercel**
   - Acesse [vercel.com](https://vercel.com) e faça login
   - Clique em **"Add New Project"** ou **"Import Project"**
   - Conecte sua conta do GitHub (ou outro provider)
   - Selecione o repositório `marlonpainas1220-sketch/app.py`

3. **Configurar o Projeto**
   - **Framework Preset:** Selecione "Other" (a configuração está no `vercel.json`)
   - **Root Directory:** Deixe como `.` (raiz do projeto)
   - **Build Command:** Deixe vazio (não necessário para Python serverless)
   - **Output Directory:** Deixe vazio

4. **Configurar Variáveis de Ambiente** (Opcional)
   - Clique em **"Environment Variables"**
   - Adicione as variáveis necessárias, se aplicável:
     - `OPENAI_API_KEY`: Sua chave da API OpenAI
     - `GEMINI_API_KEY`: Sua chave da API Gemini
     - Outras variáveis de ambiente necessárias

5. **Deploy**
   - Clique em **"Deploy"**
   - Aguarde o processo de build e deploy (geralmente 1-2 minutos)
   - Após conclusão, você receberá uma URL de produção (ex: `https://seu-projeto.vercel.app`)

### Método 2: Deploy via Vercel CLI

1. **Instalar Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Fazer Login**
   ```bash
   vercel login
   ```

3. **Navegar até o Diretório do Projeto**
   ```bash
   cd /caminho/para/app.py
   ```

4. **Iniciar Deploy**
   ```bash
   vercel
   ```
   - Siga as instruções interativas
   - Confirme o escopo do projeto
   - Confirme as configurações

5. **Deploy para Produção**
   ```bash
   vercel --prod
   ```

## 🧪 Testar Localmente

### Opção 1: Executar com Flask Localmente

1. **Criar Ambiente Virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar Dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Executar o Servidor**
   ```bash
   python api/index.py
   # Para habilitar modo debug, use:
   python api/index.py --debug
   ```
   - O servidor estará disponível em `http://localhost:5000`

4. **Testar Endpoints**
   ```bash
   # Testar endpoint principal
   curl http://localhost:5000/

   # Testar processamento de DNA
   curl -X POST http://localhost:5000/api/processar-dna \
     -H "Content-Type: application/json" \
     -d '{"videos": ["video1.mp4", "video2.mp4"]}'

   # Testar geração de conteúdo
   curl -X POST http://localhost:5000/api/gerar-conteudo \
     -H "Content-Type: application/json" \
     -d '{"tema": "Tendências 2026", "perfil": {"estilo": "Moderno"}}'
   ```

### Opção 2: Testar com Vercel CLI Localmente

1. **Instalar Vercel CLI** (se ainda não instalou)
   ```bash
   npm install -g vercel
   ```

2. **Executar em Modo de Desenvolvimento**
   ```bash
   vercel dev
   ```
   - O servidor local estará disponível em `http://localhost:3000`
   - Simula o ambiente serverless do Vercel

## 📡 Endpoints da API

### `GET /`
Retorna informações sobre o serviço e endpoints disponíveis.

**Resposta:**
```json
{
  "status": "active",
  "service": "AI.PRODUTORA - DNA CONTENT ENGINE",
  "description": "Uma plataforma de produção de conteúdo autónomo...",
  "version": "1.0.0",
  "endpoints": {
    "/": "Informações do serviço",
    "/api/processar-dna": "POST - Processar DNA do influencer",
    "/api/gerar-conteudo": "POST - Gerar conteúdo autônomo"
  }
}
```

### `POST /api/processar-dna`
Processa os vídeos de referência e extrai o DNA do influencer.

**Request Body:**
```json
{
  "videos": ["estetica.mp4", "voz.mp4", "ritmo.mp4"]
}
```

**Resposta:**
```json
{
  "status": "success",
  "perfil": {
    "estilo": "High-Energy / Futurista",
    "voz": "Frequência média, sotaque neutro",
    "ritmo_corte": "1.2 segundos por transição"
  }
}
```

### `POST /api/gerar-conteudo`
Gera conteúdo autônomo baseado no perfil e tema fornecidos.

**Request Body:**
```json
{
  "tema": "Tendências de Moda IA 2026",
  "perfil": {
    "estilo": "High-Energy / Futurista",
    "voz": "Frequência média, sotaque neutro",
    "ritmo_corte": "1.2 segundos por transição"
  }
}
```

**Resposta:**
```json
{
  "status": "success",
  "resultado": "Conteúdo Gerado com Sucesso! Pronto para publicação.",
  "tema": "Tendências de Moda IA 2026",
  "perfil": {...}
}
```

## 📁 Estrutura do Projeto

```
app.py/
├── api/
│   └── index.py          # Função serverless Flask para Vercel
├── main.py               # Script standalone para testes locais
├── requirements.txt      # Dependências Python
├── vercel.json          # Configuração do Vercel
├── README.md            # Documentação
└── index.htm            # Dashboard (opcional)
```

## 🔧 Configuração do Vercel

O arquivo `vercel.json` configura como o Vercel processa a aplicação:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "api/index.py"
    }
  ]
}
```

- **builds**: Define que `api/index.py` deve ser buildado como função Python
- **routes**: Redireciona todas as requisições para a função serverless

## 🔐 Variáveis de Ambiente

Para configurar variáveis de ambiente no Vercel:

1. Acesse seu projeto no dashboard do Vercel
2. Vá em **Settings** → **Environment Variables**
3. Adicione as variáveis necessárias:
   - `OPENAI_API_KEY`
   - `GEMINI_API_KEY`
   - Outras conforme necessário

Para testes locais, crie um arquivo `.env`:
```env
OPENAI_API_KEY=sua_chave_aqui
GEMINI_API_KEY=sua_chave_aqui
```

## 🔄 Atualizações Automáticas

O Vercel automaticamente:
- Faz redeploy quando você faz push para o branch principal
- Cria preview deployments para pull requests
- Mantém histórico de deployments

## 📞 Suporte e Troubleshooting

### Erro: "Serverless Function has timed out"
- Aumente o timeout nas configurações do Vercel (planos pagos)
- Otimize o processamento para ser mais rápido

### Erro: "Module not found"
- Verifique se todas as dependências estão no `requirements.txt`
- Certifique-se de usar versões compatíveis com Python 3.9+

### Logs do Vercel
- Acesse **Deployments** no dashboard do Vercel
- Clique no deployment específico
- Visualize logs em tempo real

## 📈 Como Executar (Legado)

**Modo Standalone:**
1. Clone este repositório.
2. Abra o `index.html` em qualquer navegador para ver o Dashboard.
3. Execute `python main.py` para simular o motor de IA.

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

Desenvolvido por Marlon Painas
