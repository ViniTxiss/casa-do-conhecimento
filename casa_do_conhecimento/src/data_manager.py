import json
import os

# Importa o módulo de traduções para obter strings da interface, se necessário
from . import locales # Importa o nosso 'tradutor'

# O "caminho" para nossos arquivos de dados
# __file__ é o caminho do arquivo atual (data_manager.py)
# os.path.dirname(__file__) nos dá o diretório de 'src'
# os.path.join navega para fora de 'src' e para dentro de 'data'
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
SCORES_FILE = os.path.join(DATA_DIR, 'scores.json')

# Mapeia códigos de idioma para nomes de arquivos de perguntas
QUESTION_FILES = {
    'pt': 'questions_pt.json',
    'en': 'questions_en.json',
    'es': 'questions_es.json' # Adicionado o arquivo de perguntas em espanhol
}

def load_questions(language_code='pt'):
    """
    Carrega as perguntas da nossa 'estante de livros' específica para o idioma.
    """
    filename = QUESTION_FILES.get(language_code, QUESTION_FILES['pt']) # Pega o arquivo do idioma ou padrão PT
    filepath = os.path.join(DATA_DIR, filename)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(locales.get_string('questions_load_error')) # Usa string traduzida
        print(f"Detalhes: Arquivo '{filepath}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(locales.get_string('questions_load_error')) # Usa string traduzida
        print(f"Detalhes: Arquivo '{filepath}' está corrompido.")
        return []

def load_scores():
    """
    Carrega as pontuações do nosso 'quadro de honra' (scores.json).
    Se o quadro estiver vazio ou não existir, devolve uma lista vazia.
    """
    try:
        with open(SCORES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # print(locales.get_string('scores_file_not_found_warning')) # Poderíamos ter uma string para isso também
        return []
    except json.JSONDecodeError:
        # print(locales.get_string('scores_file_corrupted_warning'))
        return []

def save_scores(scores):
    """
    Salva as pontuações no nosso 'quadro de honra' (scores.json).
    É como registrar os novos recordes no quadro.
    """
    # Garante que a pasta 'data' exista antes de tentar salvar
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(SCORES_FILE, 'w', encoding='utf-8') as f:
        json.dump(scores, f, indent=4, ensure_ascii=False)

# Pontuação baseada na dificuldade - permanece aqui por ser um dado de configuração
DIFFICULTY_POINTS = {
    "easy": 10,
    "medium": 20,
    "hard": 30
}