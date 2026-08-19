point=(3,4)

#we use set generally to store the places we have visited and we don't use list as they don't have uniqueness or they can be cahnged

visited=set()
visited.add((0,0))

grid={
    (0,0):"Start",
    (0,1):"End",
}