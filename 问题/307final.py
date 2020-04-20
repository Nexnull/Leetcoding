

class V:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def q2helper(v1,v2,v3):

    ve0 = (v1.x - v2.x, v1.y - v2.y, v1.z - v2.z)
    ve1 = (v1.x - v3.x, v1.y - v3.y, v1.z - v3.z)

    c =    (ve0[1]*ve1[2] - ve0[2]*ve1[1],
             ve0[2]*ve1[0] - ve0[0]*ve1[2],
             ve0[0]*ve1[1] - ve0[1]*ve1[0])

    lv1 = (c[0] ** 2 + c[1] ** 2 + c[2] ** 2) ** 0.5
    normal = ( round(c[0]/lv1,2) , round(c[1]/lv1,2) , round(c[2]/lv1,2) )

    coefficent = normal[0]*(-v3.x) + normal[1]*(-v3.y) + normal[2]*(-v3.z)
    coefficent = str(coefficent) if coefficent < 0 else "+" + str(coefficent)


    x = "+ " +str(normal[0])+"x" if normal[0] > 0 else  "- "+str(normal[0])[1:]+"x"
    y = "+ " +str(normal[1])+"y" if normal[1] > 0 else  "- "+str(normal[1])[1:]+"y"
    z = "+ " +str(normal[2])+"z" if normal[2] > 0 else  "- "+str(normal[2])[1:]+"z"

    print(x + " " + y + " " + z + " " + coefficent  + " = 0")


# v1 = V(3,2,5)
# v2 = V(1,3,3)
# v3 = V(1,1,2)

v1 = V(3,3,0)
v2 = V(5,3,1)
v3 = V(2,2,2)
v4 = V(1,4,3)
v5 = V(2,5,4)
v6 = V(4,5,5)
v7 = V(6,4,6)
v8 = V(7,3,7)
v9 = V(4,1,8)
#
# v11 = V(4,3,2)
# v12 = V(2,3,4)
# v13 = V(9,5,6)
#
# q2helper(v11,v12,v13)

q2helper(v1,v2,v6)
q2helper(v1,v2,v9)
q2helper(v1,v3,v9)
q2helper(v1,v3,v4)
q2helper(v1,v4,v5)
q2helper(v1,v5,v6)
q2helper(v2,v6,v7)
q2helper(v2,v7,v8)
q2helper(v2,v8,v9)




