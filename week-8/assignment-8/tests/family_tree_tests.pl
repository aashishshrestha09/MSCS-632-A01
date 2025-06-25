% Load the family tree module to test
:- [ '../family_tree' ].

% Begin the PlUnit test suite named 'family_tree'
:- begin_tests(family_tree).

% Test that parent facts are correctly defined
test(parent_fact) :-
    parent(john, mary),
    parent(susan, michael).

% Test grandparent relationship correctness
test(grandparent_rule) :-
    grandparent(john, lisa),
    grandparent(susan, kevin).

% Test sibling relationship: positive case (should succeed)
test(sibling_rule_true) :-
    sibling(mary, michael).

% Test sibling relationship: negative case (should fail)
test(sibling_rule_false, [fail]) :-
    sibling(mary, lisa).

% Test cousin relationship: positive case (should succeed)
% Handles cousin symmetry (cousin can be in either order)
test(cousin_rule_true) :-
    ( cousin(lisa, anna)
    ; cousin(anna, lisa) ).

% Test cousin relationship: negative case (should fail)
test(cousin_rule_false, [fail]) :-
    cousin(mary, michael).

% Test child relationship correctness
test(child_rule) :-
    child(mary, john),
    child(kevin, paul).

% Test descendant relationship: direct descendant case (child)
test(descendant_direct) :-
    descendant(mary, john).

% Test descendant relationship: indirect descendant case (grandchild or beyond)
test(descendant_indirect) :-
    descendant(lisa, john).

% Test descendant relationship: negative case (should fail)
test(descendant_false, [fail]) :-
    descendant(john, mary).

% Test grandparent relationship: negative case (should fail)
test(grandparent_false, [fail]) :-
    grandparent(mary, john).

% Test sibling relationship: a person cannot be their own sibling (should fail)
test(sibling_self_false, [fail]) :-
    sibling(john, john).

% Test cousin relationship: a person cannot be their own cousin (should fail)
test(cousin_self_false, [fail]) :-
    cousin(lisa, lisa).

% Test cousin relationship symmetry (if X is cousin of Y, then Y is cousin of X)
test(cousin_symmetry) :-
    cousin(lisa, anna),
    cousin(anna, lisa).

% Test descendant relationship symmetry: should be asymmetric (should fail)
test(descendant_symmetry_false, [fail]) :-
    descendant(john, lisa).

% End the test suite
:- end_tests(family_tree).
