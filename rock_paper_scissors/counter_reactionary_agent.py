## %%writefile counter_reactionary_agent.py

import random
from  kaggle_environments.envs.rps.utils import get_score

class counter_reactionary():
    '''
игровой агент стратегия которого заключается в том чтобы \
менять следующую значение агента значение, противоположное \
предыдущему значению оппонента
    '''
    
    def __init__(self):
        self.last_counter_action = None
    
    def __call__(self, observation, configuration):
        if observation.step == 0:
            # инициируем случайным образом значение для первого раунда
            self.last_counter_action = random.randrange(0, configuration.signs)
        else:
            # оцениваем результат предыдущего раунда
            score = get_score(self.last_counter_action, observation.lastOpponentAction)
            if score == 1:
                # меняем значение на предыдущий результат оппонента
                self.last_counter_action = (self.last_counter_action + 2) % configuration.signs
            else:
                # меняем значение на противоположное по значимости предыдущему результату оппонента
                self.last_counter_action = (observation.lastOpponentAction + 1) % configuration.signs
        return self.last_counter_action


agent = counter_reactionary()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
