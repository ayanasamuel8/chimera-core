.PHONY: setup test docker-build

setup:
	uv sync

test:
	uv run pytest tests/

docker-build:
	docker build -t chimera-core .

docker-test:
	docker run chimera-core