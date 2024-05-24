.PHONY: node_run python_run run

node_run:
	@node md5.js >/dev/null &

python_run:
	@. .venv/bin/activate; trap 'pid=$$(lsof -t -i :8000); if [ -n "$$pid" ]; then kill -9 $$pid; fi' EXIT; python connect.py  

run: node_run python_run
	@echo "Bye.."
