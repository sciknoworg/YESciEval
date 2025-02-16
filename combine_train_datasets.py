from sciqaeval import config, utils

paths = config.datasets_train_path['orkg-synthesis']

datasets = []
for path in paths:
    datasets += utils.read_json(path)

print("Dataset size is:", len(datasets))

print("Dataset keys:", datasets[0].keys())

utils.save_json(data=datasets, file_path='dataset/ORKG-Synthesis/llm4syn_train_combined_refactored_dataset.json')

paths = config.datasets_train_path['bioasq']

datasets = []
for path in paths:
    datasets += utils.read_json(path)

print("Dataset size is:", len(datasets))

print("Dataset keys:", datasets[0].keys())
utils.save_json(data=datasets, file_path='dataset/BioASQ/BioASQ_train_combined_refactored_dataset.json')