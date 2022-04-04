import json

f = open('./config.json')

data = json.load(f)
P = data['P']
file = data['file']
mutation_prob = data['mutation_prob']
selection_name = data['selection']['method']
truncated_k = data['selection']['truncated_k']
crossover_points = data['crossover']['points']
unchanged_gens = data['stop']['unchanged_generations']
max_gens = data['stop']['max_generations']
boltzman_k = data['selection']['boltzman_k']
Tc = data['selection']['Tc']
T0 = data['selection']['T0']

f.close()