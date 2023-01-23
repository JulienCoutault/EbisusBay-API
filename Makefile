.PHONY: build upload_pip

build:
	python3 -m build --wheel
	twine check dist/*

upload_pip: build
	twine upload dist/*
	rm dist/*
