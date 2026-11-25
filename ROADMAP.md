# Roadmap do Projeto: Assistente de Voz (Wuai)

Este documento acompanha as etapas de desenvolvimento do assistente, desde a captura de áudio até a integração final com resposta por voz e interface.

## Legenda de Status
- [ ] Pendente
- [~] Em andamento
- [x] Concluído

---

## Etapa 1: Captura de Áudio
Objetivo: garantir a entrada de áudio estável e validada no ambiente de desenvolvimento.

- [ ] Resolver a instalação do **PyAudio**
  - [ ] Identificar o microfone disponível no sistema
  - [ ] Capturar áudio em tempo real
  - [ ] Gravar um pequeno arquivo `WAV`
  - [ ] Reproduzir e validar a gravação

## Etapa 2: Reconhecimento de Voz (STT)
Objetivo: converter a fala capturada em texto com boa precisão.

- [ ] Integrar **Whisper** ou outro modelo de *Speech-to-Text* (STT)
  - [ ] Converter voz em texto
  - [ ] Validar o reconhecimento em português
  - [ ] Testar comandos simples por voz

## Etapa 3: Inteligência Artificial (LLM)
Objetivo: processar o texto transcrito e gerar respostas coerentes e acionáveis.

- [ ] Integrar um **LLM** (*Large Language Model*)
  - [ ] Avaliar modelos disponíveis no **Hugging Face**
  - [ ] Comparar execução local versus uso via API
  - [ ] Interpretar intenções do usuário e gerar respostas estruturadas

## Etapa 4: Execução de Comandos
Objetivo: permitir que o assistente realize ações práticas no sistema e na web.

- [ ] Integrar **PyAutoGUI** (e demais automações necessárias)
  - [ ] Abrir programas
  - [ ] Pesquisar na internet
  - [ ] Executar comandos autorizados com segurança

## Etapa 5: Resposta por Voz e Integração
Objetivo: fechar o ciclo interativo do assistente com fala natural e interface de uso.

- [ ] Aprimorar o **TTS** (*Text-to-Speech*)
  - [ ] Integrar **Piper**, se necessário
  - [ ] Criar um ciclo contínuo de escuta e resposta
  - [ ] Desenvolver uma interface para o assistente