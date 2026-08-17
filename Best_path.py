routes = {
    "Route1" : 10,
    "Route2":20,
    "Route3" :30
    
}
print("Available routes  and distance:")
for route ,distance in routes.items():
    print( routes,"+", distance, "km")

best_route = min(routes, key=routes.get)

print("Best route:",best_route)
print("Distance:" ,routes[best_route],"km")

print("i am learning from the experience")

pre_best = "Route B"
print(routes)
if routes.get(pre_best,0) > routes[best_route]:
    print(routes[pre_best])
else:
    print(routes[best_route])

