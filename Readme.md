# 🎙️ VoiceAssist RPA — Assistente de Voz Desktop para Acessibilidade

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Category](https://img.shields.io/badge/category-RPA%20%26%20Accessibility-orange.svg)

O **VoiceAssist RPA** é uma solução de automação desktop focada em **acessibilidade digital**, projetada para permitir que pessoas com restrições motoras, tremores ou lesões por esforço repetitivo (LER/DORT) operem o sistema operacional através de comandos de voz simples e intencionais.

O sistema intercepta comandos falados em português, traduz em ações de automação no sistema operacional e devolve um feedback sonoro (*Text-to-Speech*), dispensando a necessidade do uso constante de mouse e teclado.

---

## 🎯 Impacto e Acessibilidade

Este projeto foi desenhado sob as diretrizes do **WCAG 2.1 (Web Content Accessibility Guidelines)**, com foco nos princípios:

* **Operável:** Oferece uma alternativa 100% acionável por voz para atalhos de teclado e cliques de mouse.
* **Compreensível:** Fornece respostas em áudio claras para cada ação realizada ou erro detectado, garantindo previsibilidade para pessoas com deficiência visual ou baixa visão.
* **Redução de Carga Cognitiva:** Permite agrupar rotinas complexas (ex: abrir ambiente de trabalho) em um único comando audível.

---

## 🚀 Funcionalidades

- [x] **Reconhecimento de Voz em PT-BR:** Captura áudio via microfone e converte em texto.
- [x] **Síntese de Voz Offline (TTS):** Respostas ágeis em áudio sem dependência de conexão com a internet.
- [x] **Automação de Tarefas Desktop:**
  - Abertura e fechamento de aplicações.
  - Execução de atalhos globais de sistema (`Alt+Tab`, `Win+D`, etc.).
  - Leitura de métricas do sistema (uso de CPU e memória RAM).
- [x] **Mapeamento Flexível por JSON:** Permite adicionar novos comandos sem modificar o código-fonte principal.
- [x] **Logs de Auditoria:** Registro detalhado de execuções e exceções no arquivo `app.log`.

---

## 🏗️ Arquitetura do Projeto

```text
voiceassist-rpa/
├── config/
│   └── commands.json      # Mapeamento de frases de voz -> funções/ações
├── modules/
│   ├── listener.py        # Captura e conversão de áudio em texto
│   ├── speaker.py         # Módulo de resposta por áudio (pyttsx3)
│   ├── executor.py        # Automação de eventos de SO (PyAutoGUI/Keyboard)
│   └── logger.py          # Gerenciamento de logs da aplicação
├── logs/
│   └── app.log            # Histórico de eventos do sistema
├── .env.example           # Modelo de variáveis de ambiente
├── main.py                # Ponto de entrada do script
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Reconhecimento de Voz:** `SpeechRecognition`
* **Síntese de Voz:** `pyttsx3`
* **Automação Desktop:** `PyAutoGUI`, `keyboard`
* **Monitoramento do Sistema:** `psutil`
* **Gerenciamento de Logs:** `logging` (nativo)

---

## 📦 Configuração e Instalação

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Microfone operacional configurado no sistema.
* Windows OS (suporte nativo para os atalhos de automação configurados).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/voiceassist-rpa.git
   cd voiceassist-rpa
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instalação do PyAudio (se necessário no Windows):**
   Caso ocorra erro na instalação da biblioteca de áudio:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```

---

## 🎮 Como Usar

1. Execute o script principal:
   ```bash
   python main.py
   ```
2. Aguarde a mensagem sonora *"Assistente iniciado e pronto para ouvir"*.
3. Diga um dos comandos configurados em `config/commands.json`, por exemplo:
   * *"Abrir navegador"*
   * *"Verificar memória"*
   * *"Modo trabalho"*

---

## 📋 Comandos Disponíveis (Exemplos)

| Comando de Voz | Ação Executada |
| :--- | :--- |
| **"Abrir navegador"** | Inicia o navegador padrão configurado no sistema. |
| **"Status do sistema"** | Retorna por voz o uso atual de CPU e RAM do PC. |
| **"Minimizar tudo"** | Pressiona a combinação de teclas `Win + D`. |
| **"Modo trabalho"** | Abre o ambiente de desenvolvimento e utilitários de anotações. |

---

## 🤝 Como Contribuir

Contribuições são super bem-vindas! Se você deseja adicionar suporte a novos comandos, melhorar a sensibilidade do áudio ou adicionar recursos de IA:

1. Faça um Fork do projeto.
2. Crie uma branch para sua funcionalidade (`git checkout -b feature/NovaFuncionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona NovaFuncionalidade'`).
4. Faça o Push para a branch (`git push origin feature/NovaFuncionalidade`).
5. Abra um Pull Request.

---

## 📄 Licença

Este projeto está sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.