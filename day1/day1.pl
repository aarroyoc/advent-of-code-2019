file_to_lines(Path, Lines) :-
    open(Path, read, File),
    read_string(File, _, F),
    split_string(F, "\n", "\n", Lines).

string_to_number(S,N) :- atom_codes(S, C), number_codes(N, C).
map_to_numbers(XS, YS) :- maplist(string_to_number, XS, YS).

fuel(In, Out) :-
    X is div(In,3),
    Y is X-2,
    Y > 0,
    Out is Y.

fuel(_In, Out) :-
    Out is 0. 

fuel2(In, Out) :-
    fuel(In, X),
    X > 0,
    fuel2(X, Y),
    Out is X + Y.

fuel2(In, Out) :-
    fuel(In, X),
    X =< 0,
    Out is X.



main :-
    file_to_lines("input", Lines),
    map_to_numbers(Lines, Numbers),
    maplist(fuel2, Numbers, Out),
    sum_list(Out, Sum),
    write(Sum).


:- main.