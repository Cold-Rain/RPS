## %%writefile paper_agent.py

import common as cmn

class paper():
    '''
игровой агент стратегия которого заключается в том \
чтобы всегда возвращать бумагу
   '''
    
    def __call__(self, observation, configuration):
       # всегда возвращаем бумагу
       return cmn.PAPER

agent = paper()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
