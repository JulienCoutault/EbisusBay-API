.PHONY: build tests upload_pip

build:
	python3 -m build --wheel
	twine check dist/*

test:tests

tests:
	pytest

upload_pip: build
	twine upload dist/*
	rm dist/*
