init_dev_server:
	uvicorn src.main:app --host=127.0.0.1 --port=8080 --reload

create_db:
	alembic upgrade head

tests:
	pytest ./src/
