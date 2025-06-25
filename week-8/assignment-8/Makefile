.PHONY: run test clean

# Run the interactive Prolog shell loading main program
run:
	swipl -s family_tree.pl

# Run the unit tests and exit
test:
	swipl -s tests/family_tree_tests.pl -g run_tests -g halt

# Clean any temporary or backup files (optional)
clean:
	rm -f *~ tests/*~
