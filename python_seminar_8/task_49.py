import math

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
ellipse_square=lambda a,b: math.pi*a*b 
# print(ellipse_square(7,2))
find_max_far_orbit=lambda lst_orbits: max([ellipse_square(*i) for i in lst_orbits if len(set(i))!=1])
find_farthest_orbit_params=lambda lst_orbits: lst_orbits[[ellipse_square(*i) for i in lst_orbits].index(find_max_far_orbit(lst_orbits))]
print(*find_farthest_orbit_params(orbits))


# Краткое решение: 
print(max(orbits,key=lambda x: x[0]*x[1]*(x[0]!=x[1])))