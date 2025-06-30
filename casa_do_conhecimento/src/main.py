import sys
import os
import time # Importar time para as pausas

from src import data_manager # Importa o 'bibliotecário'
from src import game_logic   # Importa a 'sala de jogos'
from src import locales      # Importa o 'tradutor'

def select_language():
    """Permite que o usuário escolha o idioma do jogo."""
    lang_options = {'1': 'en', '2': 'pt', '3': 'es'}
    while True:
        print(locales.get_string('language_selection_title'))
        print(locales.get_string('lang_option_en'))
        print(locales.get_string('lang_option_pt'))
        print(locales.get_string('lang_option_es'))
        lang_choice = input(locales.get_string('choose_lang_prompt')).strip()

        # Tenta obter o código do idioma do dicionário
        if lang_code := lang_options.get(lang_choice):
            locales.set_language(lang_code)
            break
        else:
            print(locales.get_string('invalid_lang_option'))
            time.sleep(1)

def main_menu():
    """
    Exibe o menu principal do jogo.
    É a nossa 'recepção' na Casa do Conhecimento.
    """
    # Primeiro, permite que o usuário escolha o idioma
    while True:
        select_language()
        break

    # Agora que o idioma está definido, carrega as pontuações e perguntas
    player_scores = data_manager.load_scores()
    # Passa o código do idioma selecionado para carregar o arquivo de perguntas correto
    questions_data = data_manager.load_questions(locales.CURRENT_LANGUAGE)

    if not questions_data:
        print(locales.get_string('questions_load_error'))
        return # Sai do jogo se não houver perguntas

    while True:
        print(locales.get_string('main_menu_title'))
        print(locales.get_string('menu_option_1'))
        print(locales.get_string('menu_option_2'))
        print(locales.get_string('menu_option_3'))

        choice = input(locales.get_string('choose_option')).strip()

        if choice == '1':
            player_name = input(locales.get_string('player_name_prompt')).strip()
            if player_name:
                new_score = game_logic.run_quiz(player_name, questions_data)
                player_scores.append({"name": player_name, "score": new_score})
                data_manager.save_scores(player_scores) # O bibliotecário salva a nova pontuação
            else:
                print(locales.get_string('player_name_empty'))
                continue
        elif choice == '2':
            # A 'recepção' pede para a 'sala de jogos' mostrar o ranking
            game_logic.display_ranking(player_scores)
        elif choice == '3':
            print(locales.get_string('thank_you'))
            break
        else:
            print(locales.get_string('invalid_option'))
            time.sleep(1)

if __name__ == "__main__":
    # Para executar o jogo corretamente, navegue até a pasta raiz 'casa_do_conhecimento'
    # e use o comando no terminal:
    # python -m src.main
    # Isso garante que todos os imports de módulos funcionem como esperado.
    main_menu()