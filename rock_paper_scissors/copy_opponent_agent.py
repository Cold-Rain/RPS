## %%writefile copy_opponent_agent.py

import random

class copy_opponent():
    '''
игровой агент стратегия которого заключается в том чтобы копировать последнее\
значение, выставленное опонентом
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
            return observation.lastOpponentAction

agent =  copy_opponent()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
