# Casa do Conhecimento: Quiz Educativo Multicultural

Bem-vindo(a) à Casa do Conhecimento, um quiz interativo e educativo sobre culturas, idiomas e sistemas educacionais ao redor do mundo!

## Sobre o Jogo

Este jogo tem como objetivo promover o aprendizado ativo e a internacionalização da educação através de perguntas e respostas sobre diversos tópicos globais.

## Requisitos

Para rodar este jogo, você precisa ter o Python 3 instalado em seu computador.

## Como Jogar

1.  **Crie a estrutura de pastas:**
    Certifique-se de que a estrutura de pastas esteja organizada como mostrado abaixo. Crie a pasta `casa_do_conhecimento` e, dentro dela, as subpastas e os arquivos:

    ```
    casa_do_conhecimento/
    ├── src/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── game_logic.py
    │   ├── data_manager.py
    │   ├── mini_games.py
    │   ├── locales.py
    ├── data/
    │   ├── questions_pt.json
    │   ├── questions_en.json
    │   ├── questions_es.json
    │   ├── scores.json
    ├── README.md
    ```

2.  **Preencha os arquivos:**
    Copie o código fornecido para cada um dos arquivos `.py` e o conteúdo JSON para `questions_pt.json`, `questions_en.json`, `questions_es.json`.
    Crie um arquivo `scores.json` vazio (com `[]` dentro) na pasta `data/`.

3.  **Execute o jogo:**
    Abra seu terminal ou prompt de comando.
    Navegue **até a pasta raiz** do projeto (`casa_do_conhecimento/`). **É CRUCIAL estar nesta pasta.**

    ```bash
    cd C:\Users\SEU_USUARIO\Desktop\casa_do_conhecimento
    ```
    (Substitua `SEU_USUARIO` pelo seu nome de usuário no Windows)

    Em seguida, execute o arquivo principal usando o módulo Python:

    ```bash
    python -m src.main
    ```

4.  **Siga as instruções:**
    O jogo irá primeiro pedir para você escolher o idioma. Depois, apresentará o menu principal. Digite as opções para iniciar um novo jogo, ver o ranking ou sair.

## Funcionalidades

* **Perguntas de Múltipla Escolha:** Questões sobre cultura, idiomas e sistemas educacionais.
* **Multilinguismo:** Suporte para Português, Inglês e Espanhol na interface e nas perguntas.
* **Feedback Imediato:** Explicação detalhada após cada resposta, correta ou incorreta.
* **Pontuação Dinâmica:** Pontos variam de acordo com a dificuldade da pergunta.
* **Desafios:** Bônus de pontos por sequências de respostas corretas.
* **Mini Jogos:** Desafios extras para ganhar pontos bônus.
* **Ranking:** Salva e exibe as pontuações dos jogadores.

## Próximas Melhorias (Ideias)

* **Interface Gráfica (GUI):** Implementar uma interface visual usando bibliotecas como Tkinter, Pygame ou PyQt para uma experiência mais rica.
* **Mais Mini Jogos:** Expandir a variedade de mini-jogos e torná-los mais complexos.
* **Sons e Música:** Adicionar efeitos sonoros e trilha sonora.
* **Mais Categorias/Tópicos:** Expandir o banco de perguntas com novas áreas do conhecimento global.