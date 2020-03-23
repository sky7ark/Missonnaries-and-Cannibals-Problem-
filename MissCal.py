LEFT = 0
INITIAL_STATE = {"people" : [[3,0],[3,0]], "boat" :LEFT}

MC_combinations = [(1,0),(2,0),(3,0),(1,1),(2,1)]

OPERRATORS = [(
    "Cross the river with "+str(m)+" missionaries and "+str(c)+" cannibals",
    lambda s, m1 = m, c1 = c: can_move(s,m1,c1),
    lambda s, m1 = m, c1 = c: move(s,m1,c1))
    for (m,c) in MC_combinations]

M = 0
C = 1
LEFT = 0
RIGHT = 1

def copy_state(s):
    news = {}
    news["people"] = [[0,0], [0,0]]
    for i in range(2):
        news["people"][i] = s["people"][i][:]
    news["boat"] = s["boat"]
    return news
def can_move(s,m,c):
    side = s["boat"]
    p = s["people"]
    if m<1:
        return False
    m_available = p[M][side]
    if m_available < m:
        return False
    c_available = p[C][side]
    if c_available < c:
        return False
    m_remaining = m_available - m
    c_remaining = c_available - c
    if m_remaining > 0 and m_remaining < c_remaining:
        return False
    m_at_arrival = p[M][1-side]+m
    c_at_arrival = p[C][1-side]+c
    if m_at_arrival > 0 and m_at_arrival < c_at_arrival:
        return False
    return True

def move(olds,m,c):
    s = copy_state(olds)
    side = s["boat"]
    p = s["people"]

    p[M][side] = p[M][side] - m
    p[C][side] = p[C][side] - c
    p[M][1 - side] = p[M][1 - side] - m
    p[C][1 - side] = p[C][1 - side] - c
    s["boat"] = 1-side
    return s

def goal_test(s):
    p = s["people"]
    return (p[M][RIGHT] == 3 and p[C][RIGHT] == 3)

    
    

