all: website

notebooks:
	python build.py notebooks

docs:
	python build.py docs

website: docs notebooks
	python build.py pelican
