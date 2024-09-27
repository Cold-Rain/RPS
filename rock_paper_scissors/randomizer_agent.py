## %%writefile randomizer_agent.py

import random

class randomizer():
    '''
игровой агент стратегия которого заключается в том \
чтобы всегда возвращать случайное значение
    '''

    def __call__(self, observation, configuration):
        # возвращаем случайное значение
        return random.randrange(0, configuration.signs)

agent = randomizer()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
