import time

# src/locales.py

# Dicionário que armazena todas as traduções das strings da interface
TRANSLATIONS = {
    'pt': {
        'language_selection_title': "\n--- Seleção de Idioma / Language Selection / Selección de Idioma ---",
        'lang_option_en': "1. English",
        'lang_option_pt': "2. Português",
        'lang_option_es': "3. Español",
        'choose_lang_prompt': "Escolha seu idioma (1, 2 ou 3): ",
        'invalid_lang_option': "Opção inválida. Por favor, escolha 1, 2 ou 3.",
        'welcome_message': "\n--- Bem-vindo(a) ao Quiz Multicultural, {player_name}! ---",
        'quiz_instructions': "Responda às perguntas para testar seus conhecimentos globais.",
        'question_number': "Questão {num} ({category}):",
        'your_answer': "Sua resposta (A, B, C ou D): ",
        'correct': "Correto! Você ganhou {points} pontos.",
        'incorrect': "Incorreto. A resposta correta era {answer}.",
        'explanation': "Explicação: {explanation}",
        'quiz_finished': "\n--- Quiz Concluído, {player_name}! ---",
        'final_score': "Sua pontuação final: {score} pontos!",
        'challenge_completed': "\n🎉 Desafio Concluído! Você respondeu {count} perguntas corretamente em sequência! 🎉",
        'bonus_awarded': "Você ganhou um bônus de {points} pontos!",
        'mini_game_intro': "\nParabéns! Você atingiu uma pontuação alta. Hora de um desafio bônus!",
        'mini_game_points': "Você ganhou {points} pontos extras no mini-jogo!",
        'main_menu_title': "\n--- Menu Principal do Quiz Multicultural ---",
        'menu_option_1': "1. Iniciar Novo Jogo",
        'menu_option_2': "2. Ver Ranking",
        'menu_option_3': "3. Sair",
        'choose_option': "Escolha uma opção: ",
        'invalid_option': "Opção inválida. Por favor, escolha 1, 2 ou 3.",
        'player_name_prompt': "Digite seu nome: ",
        'player_name_empty': "Nome não pode ser vazio. Tente novamente.",
        'thank_you': "Obrigado por visitar a Casa do Conhecimento! Até a próxima!",
        'ranking_title': "\n--- Ranking ---",
        'no_players': "Nenhum jogador ainda. Seja o primeiro a jogar!",
        'ranking_entry': "{num}. {name}: {score} pontos",
        'questions_load_error': "Erro: Não foi possível carregar as perguntas do quiz. Verifique os arquivos de perguntas.",
        'mini_game_flag_title': "\n--- MINI JOGO BÔNUS: Cores da Bandeira! ---",
        'mini_game_flag_question': "Qual a ordem correta das cores (da esquerda para a direita) na bandeira da Itália?",
        'mini_game_flag_options': "Opções: A. Verde, Branco, Vermelho | B. Vermelho, Branco, Verde | C. Branco, Verde, Vermelho",
        'mini_game_flag_correct': "Correto! A bandeira da Itália é Verde, Branco e Vermelho.",
        'mini_game_flag_incorrect': "Incorreto. A ordem correta é Verde, Branco, Vermelho."
    },
    'en': {
        'language_selection_title': "\n--- Language Selection / Selección de Idioma / Seleção de Idioma ---",
        'lang_option_en': "1. English",
        'lang_option_pt': "2. Português",
        'lang_option_es': "3. Español",
        'choose_lang_prompt': "Choose your language (1, 2 or 3): ",
        'invalid_lang_option': "Invalid option. Please choose 1, 2 or 3.",
        'welcome_message': "\n--- Welcome to the Multicultural Quiz, {player_name}! ---",
        'quiz_instructions': "Answer the questions to test your global knowledge.",
        'question_number': "Question {num} ({category}):",
        'your_answer': "Your answer (A, B, C or D): ",
        'correct': "Correct! You earned {points} points.",
        'incorrect': "Incorrect. The correct answer was {answer}.",
        'explanation': "Explanation: {explanation}",
        'quiz_finished': "\n--- Quiz Finished, {player_name}! ---",
        'final_score': "Your final score: {score} points!",
        'challenge_completed': "\n🎉 Challenge Completed! You answered {count} questions correctly in a row! 🎉",
        'bonus_awarded': "You earned a bonus of {points} points!",
        'mini_game_intro': "\nCongratulations! You've reached a high score. Time for a bonus challenge!",
        'mini_game_points': "You earned {points} extra points in the mini-game!",
        'main_menu_title': "\n--- Multicultural Quiz Main Menu ---",
        'menu_option_1': "1. Start New Game",
        'menu_option_2': "2. View Ranking",
        'menu_option_3': "3. Exit",
        'choose_option': "Choose an option: ",
        'invalid_option': "Invalid option. Please choose 1, 2 or 3.",
        'player_name_prompt': "Enter your name: ",
        'player_name_empty': "Player name cannot be empty. Please try again.",
        'thank_you': "Thank you for visiting the Knowledge House! See you next time!",
        'ranking_title': "\n--- Ranking ---",
        'no_players': "No players yet. Be the first to play!",
        'ranking_entry': "{num}. {name}: {score} points",
        'questions_load_error': "Error: Could not load quiz questions. Check the question files.",
        'mini_game_flag_title': "\n--- BONUS MINI-GAME: Flag Colors! ---",
        'mini_game_flag_question': "What is the correct order of colors (from left to right) on the Italian flag?",
        'mini_game_flag_options': "Options: A. Green, White, Red | B. Red, White, Green | C. White, Green, Red",
        'mini_game_flag_correct': "Correct! The Italian flag is Green, White, Red.",
        'mini_game_flag_incorrect': "Incorrect. The correct order is Green, White, Red."
    },
    'es': {
        'language_selection_title': "\n--- Selección de Idioma / Language Selection / Seleção de Idioma ---",
        'lang_option_en': "1. English",
        'lang_option_pt': "2. Português",
        'lang_option_es': "3. Español",
        'choose_lang_prompt': "Elige tu idioma (1, 2 o 3): ",
        'invalid_lang_option': "Opción inválida. Por favor, elige 1, 2 o 3.",
        'welcome_message': "\n--- ¡Bienvenido(a) al Quiz Multicultural, {player_name}! ---",
        'quiz_instructions': "Responde las preguntas para poner a prueba tus conocimientos globales.",
        'question_number': "Pregunta {num} ({category}):",
        'your_answer': "Tu respuesta (A, B, C o D): ",
        'correct': "¡Correcto! Ganaste {points} puntos.",
        'incorrect': "Incorrecto. La respuesta correcta era {answer}.",
        'explanation': "Explicación: {explanation}",
        'quiz_finished': "\n--- ¡Quiz Completado, {player_name}! ---",
        'final_score': "Tu puntuación final: ¡{score} puntos!",
        'challenge_completed': "\n🎉 ¡Desafío Completado! ¡Respondiste {count} preguntas correctamente seguidas! 🎉",
        'bonus_awarded': "¡Ganaste un bono de {points} puntos!",
        'mini_game_intro': "\n¡Felicidades! Alcanzaste una puntuación alta. ¡Es hora de un desafío extra!",
        'mini_game_points': "¡Ganaste {points} puntos extra en el mini-juego!",
        'main_menu_title': "\n--- Menú Principal del Quiz Multicultural ---",
        'menu_option_1': "1. Iniciar Nuevo Juego",
        'menu_option_2': "2. Ver Clasificación",
        'menu_option_3': "3. Salir",
        'choose_option': "Elige una opción: ",
        'invalid_option': "Opción inválida. Por favor, elige 1, 2 o 3.",
        'player_name_prompt': "Ingresa tu nombre: ",
        'player_name_empty': "El nombre no puede estar vacío. Intenta de nuevo.",
        'thank_you': "¡Gracias por visitar la Casa del Conocimiento! ¡Hasta la próxima!",
        'ranking_title': "\n--- Clasificación ---",
        'no_players': "Todavía no hay jugadores. ¡Sé el primero en jugar!",
        'ranking_entry': "{num}. {name}: {score} puntos",
        'questions_load_error': "Error: No se pudieron cargar las preguntas del quiz. Verifica los archivos de preguntas.",
        'mini_game_flag_title': "\n--- MINI JUEGO BONO: ¡Colores de Bandera! ---",
        'mini_game_flag_question': "¿Cuál es el orden correcto de los colores (de izquierda a derecha) en la bandera de Italia?",
        'mini_game_flag_options': "Opciones: A. Verde, Blanco, Rojo | B. Rojo, Blanco, Verde | C. Blanco, Verde, Rojo",
        'mini_game_flag_correct': "¡Correcto! La bandera de Italia es Verde, Blanco, Rojo.",
        'mini_game_flag_incorrect': "Incorrecto. El orden correcto es Verde, Blanco, Rojo."
    }
}

CURRENT_LANGUAGE = 'pt' # Idioma padrão inicial

def set_language(lang_code):
    """Define o idioma atual do jogo."""
    global CURRENT_LANGUAGE
    if lang_code in TRANSLATIONS:
        CURRENT_LANGUAGE = lang_code
        return True
    return False

def get_string(key, **kwargs):
    """
    Obtém uma string traduzida pela sua 'key' (chave).
    Permite formatação com argumentos nomeados (kwargs).
    """
    # Se o idioma atual não existe, ou a chave não existe nesse idioma, volta para PT
    text = TRANSLATIONS.get(CURRENT_LANGUAGE, TRANSLATIONS['pt']).get(key, f"MISSING_TRANSLATION_FOR_{key}")
    return text.format(**kwargs)