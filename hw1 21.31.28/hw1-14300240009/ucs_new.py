# -*- coding: utf-8 -*-


# END
# Start A 2
# Start B 1
# A B 1
# A C 3
# A D 1
# B D 5
# B Goal 10
# C Goal 7
# D Goal 4
# END

def get_points_and_name ():
    points = []
    while True:
        s = raw_input("").strip()
        if 'END' in s:
            break
    for i in s:
        t = i.split(' ')
        points.append(new point(t[0],t[1],t[2]))
    name = set(point('Start','Start',0));
    for point in points:
        name.add(point.name)
    name = list(name)
    name.sort()
    return points, name

class point():
    name = ""
    father = ""
    settled = False
    totalcose = -1
    fathercost = -1
    def __init__(father, name, fathercost):
        this.name = name
        this.father = father
        this.fathercost = fathercost
        if father = 'Start':
            totalcose = fathercost
        if name = 'Start':
            settled = True

def set_up_matrix(points, name):
    matrix = [[False]*len(name) for i in range(len(name))]
    for point in points:
        matrix[name.index(point.father)][name.index(point.name)] = point.fathercost
    return matrix

def ucs(matrix, points, name):
    n = len(name)
    prev_name = [False]*len(name)
    cost_list = matrix[0]
    while True:
        min_pos = get_min(cost_list, points, name)
        prev_cost = cost_list[min_pos]
        next_line = matrix[min_pos]
        for i in range(1,n):
            if next_line[i]:                 
                if cost_list[i]:
                    if next_line[i] + cost_list[min_pos] < cost_list[i]:
                        cost_list[i] = next_line[i] + cost_list[min_pos]
                        prev_name[i] = min_pos
                else:
                    cost_list[i] = next_line[i] + cost_list[min_pos]
    return matrix, points, prev_name                   

def get_min(cost_list, points, name):
    min = cost_list(1)
    min_pos = 1
    min_point = point
    for i in range(1,len(cost_list)):
        if min < cost_list[i]:
            point = loc_name(points, name[i])
            if not point.settled:
                min_pos = i
                min = cost_list[i]
                min_point = point
    min_point.settled = True
    return min_pos

def loc_name(points, name_of_point):
    for i in points:
        if i.name = name_of_point:
            return i
    return False

def out_put(matrix, points, name, prev_name):
    result = ['Goal']
    for i in range(1, len(prev_name))[::-1]:
        result.append(name[prev_name[i]])
    print "Unreachable"
    print '->'.join(result[::-1])

points, name = get_points_and_name()
matrix = set_up_matrix(points, name)
matrix, points, prev_name = ucs(matrix, points, name)
out_put(matrix, points, name, prev_name)












# suppose you ve got a 