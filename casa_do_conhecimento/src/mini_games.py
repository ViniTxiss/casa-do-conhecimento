import time
from . import locales # Importa o nosso 'tradutor'

def mini_game_flag_colors():
    """Um mini-jogo simples de identificação de cores de bandeira."""
    print(locales.get_string('mini_game_flag_title'))
    print(locales.get_string('mini_game_flag_question'))
    print(locales.get_string('mini_game_flag_options'))
    user_choice = input(locales.get_string('your_answer')).strip().upper() # Reutiliza a string de 'your_answer'

    time.sleep(0.5)

    if user_choice == 'A':
        print(locales.get_string('mini_game_flag_correct'))
        return 100 # Pontos de bônus
    else:
        print(locales.get_string('mini_game_flag_incorrect'))
        return 0

# Futuramente, podemos adicionar mais mini-jogos aqui:
# def mini_game_country_capital():
#     pass