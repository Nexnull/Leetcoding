

class V:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def coeff_helper(v1,v2,v3):
    ve0 = (v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
    ve1 = (v1.x - v3.x, v1.y - v3.y, v1.z - v3.z)

    c =    (ve0[1]*ve1[2] - ve0[2]*ve1[1],
             ve0[2]*ve1[0] - ve0[0]*ve1[2],
             ve0[0]*ve1[1] - ve0[1]*ve1[0])

    lv1 = (c[0] ** 2 + c[1] ** 2 + c[2] ** 2) ** 0.5
    normal = ( round(c[0]/lv1,2) , round(c[1]/lv1,2) , round(c[2]/lv1,2) )

    coefficent = normal[0]*(-v3.x) + normal[1]*(-v3.y) + normal[2]*(-v3.z)

    return normal[0],normal[1],normal[2],coefficent


def q2helper(v1,v2,v3,name):

    # ve0 = (v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
    # ve1 = (v1.x - v3.x, v1.y - v3.y, v1.z - v3.z)
    #
    # c =    (ve0[1]*ve1[2] - ve0[2]*ve1[1],
    #          ve0[2]*ve1[0] - ve0[0]*ve1[2],
    #          ve0[0]*ve1[1] - ve0[1]*ve1[0])
    #
    # lv1 = (c[0] ** 2 + c[1] ** 2 + c[2] ** 2) ** 0.5
    # normal = ( round(c[0]/lv1,2) , round(c[1]/lv1,2) , round(c[2]/lv1,2) )
    #
    # coefficent = normal[0]*(-v3.x) + normal[1]*(-v3.y) + normal[2]*(-v3.z)

    normal = [0,0,0]
    normal[0],normal[1],normal[2],coefficent = coeff_helper(v1,v2,v3)
    coefficent = str(coefficent) if coefficent < 0 else "+" + str(coefficent)


    x = "+ " +str(normal[0])+"x" if normal[0] > 0 else  "- "+str(normal[0])[1:]+"x"
    y = "+ " +str(normal[1])+"y" if normal[1] > 0 else  "- "+str(normal[1])[1:]+"y"
    z = "+ " +str(normal[2])+"z" if normal[2] > 0 else  "- "+str(normal[2])[1:]+"z"

    print(name + ": " + x + " " + y + " " + z + " " + coefficent  + " = 0")


def q3helper(v1,v2,v3):
    a,b,c,d = coeff_helper(v1,v2,v3)
    print(a,b,c,d)

    matrix = [[round(a**2,2 ), a*b, a*c, a*d],
              [a*b, b**2, b*c, b*d],
              [a*c, b*c, c*c, c*d],
              [a*d, b*d, c*d, d*d]]

    return matrix

def total(sets):

    total = [[0 for j in range(4)]for i in range(4)]

    for set in sets:
        matrix = q3helper(set[0],set[1],set[2])

        for i in range(4):
            for j in range(4):
                total[i][j] += matrix[i][j]

    for _ in range(4):
        print(total[_])
    # print(total)



v1 = V(3,3,0)
v2 = V(5,3,1)
v3 = V(2,2,2)
v4 = V(1,4,3)
v5 = V(2,5,4)
v6 = V(4,5,5)
v7 = V(6,4,6)
v8 = V(7,3,7)
v9 = V(4,1,8)


q2helper(v1,v2,v6,"126")
q2helper(v1,v2,v9,"129")
q2helper(v1,v3,v9,"139")
q2helper(v1,v3,v4,"134")
q2helper(v1,v4,v5,"145")
q2helper(v1,v5,v6,"156")
q2helper(v2,v6,v7,"267")
q2helper(v2,v7,v8,"278")
q2helper(v2,v8,v9,"289")

# v1connection = [[v1,v2,v6],[v1,v2,v9],[v1,v3,v9],[v1,v3,v4],[v1,v4,v5],[v1,v5,v6]]
test = [[v1,v2,v6],[v1,v2,v9]]
total(test)
#
# q3helper(v1,v2,v6)
# q3helper(v1,v2,v9)
