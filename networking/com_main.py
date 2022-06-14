from com import com
# Define nodes and call com() from here

nodes = [
    {'x': 55, 'y': 42, 'weight': 1},
    {'x': 61, 'y': 46, 'weight': 1},
    {'x': 77, 'y': 55, 'weight': 1},
    {'x': 82, 'y': 65, 'weight': 1},
    {'x': 76, 'y': 72, 'weight': 1},
    {'x': 68, 'y': 65, 'weight': 1},
    {'x': 55, 'y': 53, 'weight': 1},
    {'x': 45, 'y': 55, 'weight': 1},
    {'x': 39, 'y': 62, 'weight': 1},
    {'x': 51, 'y': 64, 'weight': 1},
];


com(nodes, max_weight=4, min_weight=0, max_distance=1000, cluster_amount=3)