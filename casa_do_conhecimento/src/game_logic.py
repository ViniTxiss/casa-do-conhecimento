import random
import time
from . import data_manager
from . import mini_games
from . import locales # Importa o nosso 'tradutor'

def run_quiz(player_name, questions_data):
    """
    Executa uma sessão do quiz para um jogador.
    É a nossa 'partida' na sala de jogos.
    """
    score = 0
    correct_answers_in_a_row = 0
    questions_for_this_round = list(questions_data) # Copia a lista para embaralhar
    random.shuffle(questions_for_this_round)

    print(locales.get_string('welcome_message', player_name=player_name))
    print(locales.get_string('quiz_instructions'))
    time.sleep(1) # Pausa para efeito de "transição"

    # Monitor de pontos para o mini-jogo
    next_mini_game_score_threshold = 150 # O primeiro mini-jogo será ativado ao atingir 150 pontos

    for i, q in enumerate(questions_for_this_round):
        print(locales.get_string('question_number', num=(i + 1), category=q['category']))
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input(locales.get_string('your_answer')).strip().upper()

        if user_answer == q["answer"]:
            points = data_manager.DIFFICULTY_POINTS.get(q['difficulty'], 10)
            print(locales.get_string('correct', points=points))
            score += points
            correct_answers_in_a_row += 1
            if correct_answers_in_a_row >= 3: # Desafio: 3 respostas corretas seguidas
                print(locales.get_string('challenge_completed', count=3))
                print(locales.get_string('bonus_awarded', points=50))
                score += 50
                correct_answers_in_a_row = 0 # Reseta o contador do desafio
        else:
            print(locales.get_string('incorrect', answer=q['answer']))
            correct_answers_in_a_row = 0 # Reseta o contador se errar

        print(locales.get_string('explanation', explanation=q['explanation'])) # Feedback imediato
        time.sleep(2) # Pausa para o jogador ler a explicação

        # Lógica para ativar o mini-jogo bônus
        if score >= next_mini_game_score_threshold:
           print(locales.get_string('mini_game_intro'))
           bonus_points = mini_games.mini_game_flag_colors() # Chamando o mini-jogo da 'sala de bônus'
           score += bonus_points
           print(locales.get_string('mini_game_points', points=bonus_points))
           next_mini_game_score_threshold += 200 # Aumenta o limiar para o próximo mini-jogo
           time.sleep(2)


    print(locales.get_string('quiz_finished', player_name=player_name))
    print(locales.get_string('final_score', score=score))
    return score

def display_ranking(player_scores):
    """
    Exibe o ranking dos jogadores.
    É como mostrar o 'quadro de honra' na sala de jogos.
    """
    if not player_scores:
        print(locales.get_string('ranking_title'))
        print(locales.get_string('no_players'))
        return

    # Ordena as pontuações em ordem decrescente
    sorted_scores = sorted(player_scores, key=lambda x: x["score"], reverse=True)

    print(locales.get_string('ranking_title'))
    for i, player in enumerate(sorted_scores):
        print(locales.get_string('ranking_entry', num=(i + 1), name=player['name'], score=player['score']))