'''
общий модуль содержащий общие переменные функции и классы
'''

ROCK = 0
'''
Переменная хранящая значение для сущности камень. Значение равно 0
'''

PAPER = 1
'''
Переменная хранящая значение для сущности бумага. Значение равно 1
'''

SCISSORS = 2
'''
Переменная хранящая значение для сущности ножнецы. Значение равно 2
'''

RPS_VALUES = (ROCK, PAPER, SCISSORS)
'''
Все используемые значения в игре
'''

COUNTER_VALUES = {ROCK:PAPER, PAPER:SCISSORS, SCISSORS:ROCK}
'''
Словарь содержащий пары значение/противозначение, где \
противозначение всегда имеет преоритет в сравнении с значением.
Например:
камень/бумага, где бумага побеждает камень
'''

AGENTS = {
    'paper':'paper_agent.py',
    'rock':'rock_agent.py',
    'scissors':'scissors_agent.py',
    'copy_opponent':'copy_opponent_agent.py',
    'reactionary':'reactionary_agent.py',
    'counter_reactionar':'counter_reactionary_agent.py',
    'statistical':'statistical_agent.py',
    'randomizer':'randomizer_agent.py',
    'loop':'loop_agent.py',
    'LinearRegression':'lreg_agent.py',
    'spline_interp':'spline_interp_agent.py',
    'linear_interp':'linear_interp_agent.py',
    'contr_opponent':'contr_opponent_agent.py',
}
'''
словарь содержащий информацию о игровых агентах 
в виде название:файл
'''
