## %%writefile rock_agent.py

import common as cmn

class rock():
    '''
игровой агент стратегия которого заключается в том \
чтобы всегда возвращать камень
    '''

    def __call__(self, observation, configuration):
        # всегда возвращаем камень
        return cmn.ROCK

agent = rock()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
