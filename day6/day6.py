from collections import defaultdict
import networkx as nx

orbits = defaultdict(lambda: list())

def orbit_count(key):
    n_orbits = 0
    n_orbits += len(orbits[key])
    for subkey in orbits[key]:
        if subkey in orbits.keys():
            n_orbits += orbit_count(subkey)
    return n_orbits    

def main():
    
    with open("input") as f:
        lines = f.readlines()
    for line in lines:
        s = line.strip().split(")")
        a = s[0]
        b = s[1]
        orbits[b].append(a)
    
    n_orbits = 0
    for key in orbits.keys():
        n_orbits += orbit_count(key)
        print(f"KEY: {key} Orbits: {n_orbits}")
    print(f"Num Orbits: {n_orbits}")

    # Part 2
    G = nx.from_dict_of_lists(orbits)
    sp = nx.shortest_path_length(G, source="SAN", target="YOU")
    print("Distance", sp-2)



main()