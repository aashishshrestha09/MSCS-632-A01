# Prolog Family Tree

## Overview

This project implements a family tree in Prolog, defining basic family relationships using facts and deriving relationships such as grandparents, siblings, cousins, children, and descendants using logical rules and recursion. The project demonstrates logical inference and recursive queries in Prolog.

## Project Details

- Family facts: `parent/2`, `male/1`, `female/1`
- Derived relationships: `grandparent/2`, `sibling/2`, `cousin/2`, `child/2`, `descendant/2`
- Logical inference queries: Find children, siblings, cousins, descendants lists
- Unit tests: Validate relationship rules and recursive logic correctness using plunit
- Demonstrates: Prolog’s recursion, pattern matching, and relational reasoning

## Project Structure

```bash
.
├── family_tree.pl
├── Makefile
├── README.md
└── tests
    └── family_tree_tests.pl
```

## Requirements

- [SWI-Prolog](https://www.swi-prolog.org/) (Recommended version 9.0.4 or later)

## Usage

### Running interactively

Start SWI-Prolog with the family tree loaded:

```bash
make run
```

Then at the Prolog prompt (`?-`), enter any of the sample queries below.

To exit Prolog:

```prolog
?- halt.
```

or press `Ctrl+D` (Linux/macOS) or `Ctrl+Z` then Enter (Windows).

### Running Unit Tests

Run the automated unit tests using the Makefile:

```bash
make test
```

Or directly via SWI-Prolog:

```bash
swipl -s tests/family_tree_tests.pl -g run_tests -g halt
```

Tests check correctness of all facts, derived relationships, and recursive logic.

## Sample Queries

Here are some example queries you can try after loading the family tree:

```prolog
% Find all children of a person
?- children(john, Children).

% List all siblings of a person
?- siblings_list(mary, Siblings).

% List all cousins of a person (fully symmetric, no duplicates)
?- cousins_list(anna, Cousins).

% List all descendants of a person
?- descendants_list(john, Descendants).

% Check if two people are siblings
?- sibling(mary, michael).

% Check if two people are cousins (relation is symmetric)
?- cousin(lisa, anna).
?- cousin(anna, lisa).

% Check if a person is a grandparent of another
?- grandparent(john, lisa).

% Verify child-parent relationship
?- child(mary, susan).

% Check direct descendant
?- descendant(mary, john).

% Check indirect descendant (like a grandchild or beyond)
?- descendant(lisa, john).
```

Each query returns bindings for variables on success. Use `;` to see alternative answers or press `Enter` to finish.
