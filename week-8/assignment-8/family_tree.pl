%-----------------------------------------------------------
% Basic Facts
%-----------------------------------------------------------

% parent(Parent, Child).
parent(john, mary).
parent(john, michael).
parent(susan, mary).
parent(susan, michael).

parent(mary, lisa).
parent(mary, kevin).
parent(paul, lisa).
parent(paul, kevin).

parent(michael, anna).
parent(michael, tom).
parent(linda, anna).
parent(linda, tom).

% male(Person).
male(john).
male(michael).
male(paul).
male(kevin).
male(tom).

% female(Person).
female(susan).
female(mary).
female(linda).
female(lisa).
female(anna).

%-----------------------------------------------------------
% Derived Relationship Rules
%-----------------------------------------------------------

% grandparent(Grandparent, Grandchild)
% True if Grandparent is a parent of a Parent who is the parent of Grandchild.
grandparent(X, Y) :- 
    parent(X, Z), 
    parent(Z, Y).

% sibling(Person1, Person2)
% True if Person1 and Person2 share at least one parent and are distinct individuals.
sibling(X, Y) :- 
    parent(P, X), 
    parent(P, Y), 
    X \= Y.

% cousin(Person1, Person2)
% True if Person1 and Person2 have parents who are siblings, excluding self-cousins.
cousin(X, Y) :-
    parent(PX, X),
    parent(PY, Y),
    sibling(PX, PY),
    X \= Y.

% child(Child, Parent)
% True if Child is a child of Parent.
child(X, Y) :- 
    parent(Y, X).

% descendant(Descendant, Ancestor)
% True if Descendant is a child of Ancestor or recursively a descendant of one of Ancestor's children.
descendant(X, Y) :- 
    parent(Y, X).
descendant(X, Y) :- 
    parent(Y, Z), 
    descendant(X, Z).

%-----------------------------------------------------------
% Logical Inference Queries with no duplicates
%-----------------------------------------------------------

% children(+Parent, -ChildrenList)
% Returns a list of all children of Parent, no duplicates.
children(Parent, Children) :-
    setof(Child, child(Child, Parent), Children).

% siblings_list(+Person, -SiblingsList)
% Returns all siblings of Person as a list without duplicates.
siblings_list(Person, Siblings) :-
    setof(Sib, sibling(Person, Sib), Siblings).

% cousins_list(+Person, -CousinsList)
% Returns all cousins of Person (in either direction) as a list without duplicates.
cousins_list(Person, Cousins) :-
    setof(Cousin, (cousin(Person, Cousin) ; cousin(Cousin, Person)), Cousins).

% descendants_list(+Ancestor, -DescendantsList)
% Returns a list of all descendants of Ancestor without duplicates.
descendants_list(Ancestor, Descendants) :-
    setof(Descendant, descendant(Descendant, Ancestor), Descendants).
