def tower_builder(n_floors):
    tower1= []
    for i in range(n_floors):
        tower = [" "*(n_floors-1) + "*" * (2*i+1) +  " "*(n_floors-1)]
        n_floors -=1
        tower1 = tower1 + tower
    return tower1
