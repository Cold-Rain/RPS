## %%writefile scissors_agent.py

import common as cmn

class scissors():
    '''
игровой агент стратегия которого заключается в том \
чтобы всегда возвращать ножницы
    '''

    def __call__(self, observation, configuration):
      # всегда возвращаем ножницы
      return cmn.SCISSORS

agent = scissors()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
