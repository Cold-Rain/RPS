## %%writefile loop_agent.py

import common as cmn

class loop():
    '''
игровой агент стратегия которого заключается в том \
чтобы возвращать RPS значения по кругу
    '''
    def __init__(self):
        self.loop_idx = None

    def __call__(self, observation, configuration):
        if observation.step == 0:
            # первоначальная инициализация 
            # для первой итерации сравнения агентов
            self.loop_idx = 0
        else:
            # изменяем индекс массива
            self.loop_idx += 1
            if self.loop_idx >= len(cmn.RPS_VALUES):
                self.loop_idx = 0
        # возвращаем значение для текущей итерации
        return cmn.RPS_VALUES[self.loop_idx]

agent = loop()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
