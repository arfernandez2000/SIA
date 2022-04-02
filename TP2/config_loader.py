import json

f = open('./config.json')

data = json.load(f)
P = data['P']
file = data['file']
mutation_prob = data['mutation_prob']
selection_name = data['selection']['method']
tournament_k = data['selection']['k']
crossover_points = data['crossover']['points']
unchanged_gens = data['stop']['unchanged_generations']
max_gens = data['stop']['max_generations']

f.close()