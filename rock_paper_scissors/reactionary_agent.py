## %%writefile reactionary_agent.py

import random
from  kaggle_environments.envs.rps.utils import get_score

class reactionary():
    '''
игровой агент стратегия которого заключается в том чтобы \
в случае проигрыша или ничьей менять значение на противоположное \
по значимости предыдущему результату оппонента
    '''

    def __init__(self):
        self.last_react_action = None

    def __call__(self, observation, configuration):
        if observation.step == 0:
            # инициируем случайным образом значение для первого раунда
            self.last_react_action = random.randrange(0, configuration.signs)
        else:
            # оцениваем результат предыдущего раунда
            score = get_score(self.last_react_action, observation.lastOpponentAction)
            # в случае проигрыша или ничьей 
            if score <= 1:
                # меняем значение на противоположное по значимости 
                # предыдущему результату оппонента
                self.last_react_action = \
                    (observation.lastOpponentAction + 1) % configuration.signs
        return self.last_react_action

agent = reactionary()

# метод вызываемый из kaggle_environments
def call_agent(obs, conf):
    return agent(obs, conf)
