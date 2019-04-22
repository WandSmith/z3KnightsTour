import z3
import sys
import os
import webbrowser

html = """
<html>
<head>
<title>RESULT</title>
<script type="text/javascript" src="./result.js"></script>
</head>
<body>

"""

html_tail = """
<p><button onclick="update()" id="nextStep">next step</button></p>
</body>
</html>
"""

def solve(m, n):
    v = [[z3.Int('v%d%d' % (i,j)) for j in range(n)] for i in range(m)]
    vs = [z3.Int('v%d%d' % (i,j)) for j in range(n) for i in range(m)]
    solver = z3.Solver()

    # the knight has m * n step
    for i in range(m):
        solver.add([z3.And(1 <= v[i][j], v[i][j] <= m * n) for j in range(n)])
    
    # every cell can be arrived at a unique step:
    solver.add(z3.Distinct(vs))

    # the nearby step must be a legal one:
    move = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
    for i in range(m):
        for j in range(n):
            step_c = z3.Or(v[i][j] == 1)
            step = [ (i+m[0],j+m[1]) for m in move]
            count = 0
            for s in step:
                if s[0] >= 0 and s[0] < m and s[1] >= 0 and s[1] < n:
                    #step is still in the board, add new constraint
                    step_c = z3.Or(step_c, v[i][j] - v[s[0]][s[1]] == 1)
                    count += 1
            if count != 0:
                solver.add(step_c)
    
    if solver.check() == z3.sat:
        model = solver.model()
        sol = [model[v[i][j]] for i in range(m) for j in range(n)]
        pos = [0] * len(sol)
        for i in range(m*n):
            pos[int(str(sol[i]))-1] = i
        f = open('result.html','w+')
        html_result = (html + "<canvas id=\"myCanvas\" width=\"" 
            + str(80*n) + "\" height=\"" + str(80*m) + "\" >\n</canvas>\n")
        html_result += "<script>draw(" +  str(m) + ','+ str(n) + ")</script>"
        html_result += "<script>pos=" + str(pos) + ";</script>"
        html_result += html_tail
        print(html_result, file = f)
        html_path = "file://"+os.getcwd()+"/result.html"
        webbrowser.open_new(html_path)
        f.close()
    else:
        print("unsat")
    return

def main(argv):
    try:
        (m, n) = (int(argv[0]), int(argv[1]))
        if m <= 0 or n <= 0:
            print("the numbers shouldn't be negative!")
        else:
            solve(m, n)
    except:
        print("the input should be 2 nonzero nats")
    return

if __name__ == "__main__":
    main(sys.argv[1:])