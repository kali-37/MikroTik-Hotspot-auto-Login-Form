.PHONY: setup node_run python_run run


	
run: node_run python_run
	@echo "Bye.."

setup:
	@npm install express
	@if [ ! -d ".venv" ]; then \
		python -m venv .venv; \
	fi
	@source .venv/bin/activate && pip install -r requirements.txt

node_run:
	@pid=$$(lsof -t -i :8002); \
	if [ -n "$$pid" ]; then \
		kill -9 $$pid; \
	fi
	@node md5.js >/dev/null &

python_run:
	@source .venv/bin/activate && \
	python connect.py || { echo "ERR in connection"; }
	@trap 'pid=$$(lsof -t -i :8002); \
	if [ -n "$$pid" ]; then kill -9 $$pid; fi' EXIT
