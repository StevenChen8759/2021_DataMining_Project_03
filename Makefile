init:
	pipenv --three
	pipenv install
	pipenv install --dev

hw03_preprocess:
	pipenv run python ./src/hw03_data_preprocess.py

ibm_preprocess:
	pipenv run python ./src/ibm_data_preprocess.py

preprocess: hw03_preprocess ibm_preprocess

run:
	pipenv run python ./src/main.py

graph_adjust:
	pipenv run python ./src/graph_adjust.py

commit:
	pipenv run cz commit

lint:
	pipenv run flake8
	pipenv run pylint