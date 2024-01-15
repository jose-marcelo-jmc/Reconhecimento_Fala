# Reconhecimento de Fala

Projeto de reconhecimento de fala dividido em funções: identificação da fala, leitura de arquivos de áudio e criação de arquivos de áudio.

## Descrição dos arquivos de código e suas funções

### main:
Código base para a estrutura de captação, leitura e transcrição dos áudios.
  * Processo de execução:
    1. Avalia o som do ambiente.
    2. Envia a mensagem "Comece a falar:", indicando para o usuário iniciar sua fala.
    3. Para encerrar sua fala, basta permanecer em silêncio por um momento.
    4. Caso o usuário não fale após a mensagem "comece a falar" ou ocorra qualquer erro, a mensagem "Não captei nenhum áudio" será enviada.

### audios_longos:
Código que permite falas mais longas do usuário, mostra gradativamente sua fala e só se encerra após receber uma ordem específica.
  * Processo de execução:
    1. Avalia o som do ambiente.
    2. Envia a mensagem "Comece a falar:", indicando para o usuário iniciar sua fala.
    3. Permite liberdade para pausas na fala; a cada pausa, sua última frase será mostrada.
    4. Para encerrar sua fala, durante sua frase, diga "encerrar gravação".

### criar_audio:
Código que cria um arquivo de áudio a partir da fala do usuário.
  * Processo de execução:
    1. Avalia o som do ambiente.
    2. Envia a mensagem "Comece a falar:", indicando para o usuário iniciar sua fala.
    3. Para encerrar sua fala, basta permanecer em silêncio por um momento.
    4. Um arquivo de áudio é criado na mesma pasta do código, contendo a sua fala.

### ler_audio:
O código lê um arquivo de áudio enviado e o transcreve.
  * Processo de execução:
    1. Envie o arquivo de áudio (Certifique-se de que o arquivo está na mesma pasta e faça as alterações necessárias conforme o local, nome e tipo).

## Bibliotecas Necessárias:

* speech_recognition
* time
