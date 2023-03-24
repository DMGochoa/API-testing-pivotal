static_code_analysis:
	@echo "Static Code analisys"
	pipenv run pylint main/
	pipenv run pylint tests/
	pipenv run flake8 main/ --benchmark
	pipenv run flake8 tests/ --benchmark
	pipenv run pycodestyle main/ --benchmark
	pipenv run pycodestyle tests/ --benchmark
