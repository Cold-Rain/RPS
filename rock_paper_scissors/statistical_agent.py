## %%writefile statistical_agent.py

import random

class statistical():
    '''
игровой агент стратегия которого заключается в том чтобы \
найти среди статистики наиболее часто встречающееся значение опонента, \
и вернуть противоположное по значимости значение
    '''

    def __init__(self):
        self.action_histogram = {}

    def __call__(self, observation, configuration):
        if observation.step == 0:
            # в случае начального раунда возвращаем 
            # инициализируем словарь исторических данных
            self.action_histogram = {}
            # возвращаем случаное значение
            return random.randrange(0, configuration.signs)
        # берем последнее значение оппонента и инкрементируем его счетчик
        action = observation.lastOpponentAction
        if action not in self.action_histogram:
            self.action_histogram[action] = 0
        self.action_histogram[action] += 1
        # находим наиболее часто встречающеемя значение
        mode_action = None
        mode_action_count = None
        for k, v in self.action_histogram.items():
            if mode_action_count is None or v > mode_action_count:
                mode_action = k
                mode_action_count = v
                continue
        # возвращаем его противозначение
        return  (mode_action + 1) % configuration.signs

agent = statistical()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
