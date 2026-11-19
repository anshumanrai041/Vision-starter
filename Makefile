install:
        poetry install

link:
    poetry run ruff check

test:
     poetry run pytest

run:
   poetry run python src/vision_starter/main.pytest