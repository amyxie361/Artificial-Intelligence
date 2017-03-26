# -*- coding: utf-8 -*-

def get_points_and_name ():
    points = []
    s_total = []
    while True:
        s = raw_input("").strip()
        if 'END' in s:
            break
        else:
            s_total.append(s)
    t_0 = []
    for i in s_total:
        t = i.split(' ')
        t_0.append(t[0])
        if t[0] != "Goal":
            new_point = Point(t[0],t[1],t[2])
            points.append(new_point)
    name = set();
    for point in points:
        name.add(point.name)
    name = list(name)
    name.sort()
    if "Goal" in name == False or "Start" in t_0 == False or len(s_total) == 0:
        return False, False
    name.remove("Goal")
    name = ["Start"] + name + ["Goal"]
    return points, name
 
class Point:
    name = ""
    father = ""
    settled = False
    totalcose = -1
    fathercost = -1
    def __init__(self, father, name, fathercost):
        self.name = name
        self.father = father
        self.fathercost = fathercost
        if father == 'Start':
            totalcose = fathercost
        if name == 'Start':
            settled = True

            

def set_up_matrix(points, name):
    matrix = [[False]*len(name) for i in range(len(name))]
    for point in points:
        matrix[name.index(point.father)][name.index(point.name)] = int(point.fathercost)
    return matrix
    

def ucs(matrix, points, name):
    n = len(name)
    prev_name = [False]*len(name)
    i = 0
    for point in points:
        i += 1
        if point.father == "Start":
            prev_name[i] = 0
    cost_list = matrix[0]
    count = 0
    while count <= n:
        count += 1
        min_pos = get_min(cost_list, points, name)
        next_line = matrix[min_pos]
        for i in range(1,n):
            if next_line[i]:
                if cost_list[i]:
                    if next_line[i] + cost_list[min_pos] < cost_list[i]:
                        cost_list[i] = next_line[i] + cost_list[min_pos]
                        prev_name[i] = min_pos
                else:
                    cost_list[i] = next_line[i] + cost_list[min_pos]
                    prev_name[i] = min_pos
    return matrix, points, prev_name                   

def get_min(cost_list, points, name):
    base = 0
    n = len(name)
    for temp in range(1,n):
        base += 1
        base_point = loc_name(points, name[temp])
        if base_point:
            if not base_point[0].settled:
                break
    min = cost_list[base]
    min_pos = base
    min_point = base_point
    for i in range(base,len(cost_list)):
        if not cost_list[i]:
            continue
        elif min is False or min > cost_list[i]:
            point = loc_name(points, name[i])
            if not point[0].settled:
                min_pos = i
                min = cost_list[i]
                min_point = point
    for p in min_point:
        p.settled = True
    return min_pos

def loc_name(points, name_of_point):
    result = []
    for i in points:
        if i.name == name_of_point:
            result.append(i)
    return result



def out_put(matrix, points, name, prev_name):
    result = ['Goal']
    flag = prev_name[len(name)-1]
    n = len(name)
    count = 0
    while flag != 0 and count < n:
        count += 1
        result.append(name[flag])
        flag = prev_name[flag]
    result.append("Start")
    print '->'.join(result[::-1])


while True:
    try:
        points, name = get_points_and_name()
        if points == False:
            print "Unreachable"
        else:
            matrix = set_up_matrix(points,name)
            matrix,points,prev_name = ucs(matrix,points,name) 
            out_put(matrix, points, name, prev_name)
    except EOFError:
        break

