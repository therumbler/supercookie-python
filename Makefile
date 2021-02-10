start:
	pipenv run uvicorn app:app

start-dev:
	pipenv run uvicorn app:app --reload --log-level='debug'