install:
	brew install entr
	pip3 install -r requirements.txt

run:
	python3 main.py

rerun:
	ls main.py | entr python3 main.py

focus:
	ls main.py | entr python3 main.py g.png

.PHONY: install run rerun
