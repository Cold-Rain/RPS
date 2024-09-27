## %%writefile linear_interp_agent.py

import random
import numpy as np
import common as cmn
from scipy.interpolate import interp1d

class linear_interp():
    '''
игровой агент стратегия которого заключается в том чтобы \
рассчитывать при помощи линейной интерполяции следующее значение оппонента \
и возвращать его противозначение
    '''

    def __init__(self):
        self.opponent_values = []

    def __call__(self, observation, configuration):
        if observation.step == 0:
            # в случае начальной итерации
            # инициализируем массив накопления данных
            self.opponent_values = []
            # возвращаем случайное значение
            return random.randrange(0, configuration.signs)
        else:
            # сохраняем последнее значение оппонента в массив
            self.opponent_values.append(observation.lastOpponentAction)
            # генерируем порследовательность входных значений интерполяции
            # по факту это порядковые номера выходных значений
            x_data = list(range(1, len(self.opponent_values) + 1))
            # определяем выходные значения (для наглядности)
            y_data = self.opponent_values
            # формируем приемлемые по типу аргументы для функции интерполяции
            x = np.array(x_data)
            y = np.array(y_data)
            # создаем интерполятор
            interp = interp1d(x, y, kind='linear', fill_value='extrapolate')
            # формируем значение аргумента, для которого нужно получить 
            # прогнозируемое значение
            next_x = max(x_data) + 1
            # формируем приемлемые по типу аргументы для функции интерполяции
            new_x = np.array([next_x])
            # вычисляем прогнозируемое значение стратегии оппонента
            y_pred = interp(new_x)
            predicted_val = y_pred[0] 
            # преобразуем полученное значение в область допустимых значений
            corrected_val = min(cmn.RPS_VALUES , key=lambda x: abs(x - predicted_val))
            # получаем и возвращаем контр-значение для спрогнозированного значения
            counter_val = cmn.COUNTER_VALUES[corrected_val]
            return counter_val

agent = linear_interp()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
