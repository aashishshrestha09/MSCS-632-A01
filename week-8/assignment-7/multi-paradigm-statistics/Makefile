.PHONY: all c ocaml python clean

all: c ocaml python

c:
	@echo "Building C program..."
	$(MAKE) -C C
	@echo "Running C program..."
	./C/statistics

ocaml:
	@echo "Initializing opam and setting up OCaml environment..."
	@if ! opam switch show >/dev/null 2>&1; then \
		opam init --no-setup --disable-sandboxing; \
	fi
	@echo "Compiling OCaml program..."
	@bash -c 'eval "$$(opam env)" && ocamlc -o OCaml/statistics OCaml/statistics.ml'
	@echo "Running OCaml program..."
	./OCaml/statistics

python:
	@echo "Setting up Python virtual environment if not present..."
	@if [ ! -d "venv" ]; then python3 -m venv venv; fi
	@echo "Activating virtual environment and running program..."
	. venv/bin/activate && python3 Python/statistics_calculator.py

clean:
	@echo "Cleaning C build artifacts..."
	$(MAKE) -C C clean
	@echo "Cleaning OCaml build artifacts..."
	rm -f OCaml/statistics OCaml/*.cmi OCaml/*.cmo
	@echo "Removing Python virtual environment..."
	rm -rf venv

