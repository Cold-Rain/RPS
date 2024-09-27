## %%writefile contr_opponent_agent.py

import random
import common as cmn

class contr_opponent():
     '''
игровой агент стратегия которого заключается в том чтобы \
возвращать контрзначение для последнего значения выставленного опонентом

    '''
     
     def __call__(self, observation, configuration):        
        # в случае первой итерации, когда нет информации о последнем 
        # значении выставленном оппонентом, выбирается случайное значение 
        # из списка допустимых
        if observation.step == 0:
            return random.randrange(0, configuration.signs)
        # в случае когда есть информация о последнем значении 
        # выставленном оппонентом
        else:
            return cmn.COUNTER_VALUES[observation.lastOpponentAction]

            
agent =  contr_opponent()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
