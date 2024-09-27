## %%writefile lreg_agent.py

import random
import numpy as np
import common as cmn
from sklearn.linear_model import LinearRegression

class linear_regression():
    '''
игровой агент стратегия которого заключается в том чтобы \
рассчитывать по линейной регрессии следующее значение оппонента \
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
            x = np.array(x_data).reshape((-1, 1))
            y = np.array(y_data)
            # создаем модель регрессии и вычисляем оптимальные значение весов
            model = LinearRegression().fit(x, y)
            # вычисляем прогнозируемое значение стратегии оппонента
            y_pred = model.predict(x)
            predicted_val = y_pred[0] 
            # преобразуем полученное значение в область допустимых значений
            corrected_val = \
                min(cmn.RPS_VALUES , key=lambda x: abs(x - predicted_val))
            # получаем и возвращаем контр-значение 
            # для спрогнозированного значения
            counter_val = cmn.COUNTER_VALUES[corrected_val]
            return counter_val

agent = linear_regression()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
