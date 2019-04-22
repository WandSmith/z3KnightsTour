Requirements: Build z3 SMT solver for python3 language.(see https://github.com/Z3Prover/z3)

This is a simple knight's tour puzzle solver bases on z3 SMT solver. A knight's tour puzzle is to find the possible path of a knight in a $m\times n$ board, with each step of the knight follows the chess rule, and the knight visiting every square of the board exactly once.

Run the program:

```shell
python3 KnightTour.py <num_row> <num_col>
```

num_row and num_col should all be nonzero natural numbers, otherwise, the program will throw an error about your input.

If the result is unsat, it simply output the sad result in your shell.

If the result is sat, it will automatically open the result demo with your default browser, like this:

![example](https://github.com/WandSmith/z3KnightsTour/blob/master/example.png)

Have funs!