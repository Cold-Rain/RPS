'''
главный испольняемый файл
'''

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
import common as cmn
import itertools 
from kaggle_environments import make, evaluate

# создаем уникальные комбинации агентов для тестирования
agent_comb = list(itertools.combinations(cmn.AGENTS.keys(), 2))
# определяем словарь результатов
results ={}
# запускаем тестирование агентов
for a1,  a2 in agent_comb:
    # получаем названия файлов тестируемых агентов
    af1 = cmn.AGENTS[a1]
    af2 = cmn.AGENTS[a2]
    # выполняем тестирование и сохраняем результаты
    results[(a1, a2)] = evaluate(
        "rps", 
        [af1, af2], 
        configuration={"episodeSteps": 100} )[0]
#print("\n"*3, "{\n" + "\n".join("   {!r}: {!r},".format(k, v) for k, v in results.items()).strip(',') + "\n}", "\n"*3)
# определяем победителей
winners = [k[0] if v[0] > v[1] else k[1] if v[0] < v[1] else None for k, v in results.items()]
# формируем и сортируем статистику
stats  = { t[0]:t[1] for t in sorted([(k, winners.count(k)) for k in cmn.AGENTS.keys()], key=lambda t: t[1], reverse=True)}
# выводим результаты
print("\n" + "\n".join("{!r}: {!r},".format(k, v) for k, v in stats.items()).strip(','), "\n")
print(f"Total agents count: {len(cmn.AGENTS)}\n")
