# levels.py
from grid import Level, Grid

def load_levels():
    return [
     

 Level(
    Grid( [
        [None, None, None,None],
        [None, None, 3,None],
        [None, 2, None,None]
    ], [
        (1, 1),(1,3)  
    ]),
    max_moves=5
),

 Level(
    Grid( [
        [None, None, None, None, None],
        [None, None, 3, None, None],
        [None, 3, None, 3, None],
        [None, None, 3, None, None],
        [2, None, None, None, None]
      
    ], [
         (0, 2), (2, 0), (2, 2),(2,4) ,(4,2) 
    ]),
    max_moves=5
),
 Level(
    Grid( [
        [None, None, None, None],
        [None, None, 3, None],
        [2, None, None, None],
    ], [
         (0, 3), (2, 3),  
    ]),
    max_moves=5
),
 Level(
    Grid( [
        [None, None, None],
        [None, 3, None],
        [2, None, None],
        [None, 3, None],
        [None, None, None],
      
    ], [
         (0, 0), (0, 2), (4, 1)  
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, None, None],
        [3, None, 3],
        [3, None, 3],
        [None, 2, None],
    ], [
         (0, 0), (0, 2),(3,0),(1,0),(1,2)
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, None, None,None,None],
        [None, 3, None,3,None],
        [2, None, None,None,None],
    ], [
         (0, 3), (1, 2),(2,3)
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, None, None , None],
        [3, None, None , None],
        [3, 2, None , None],
        [None, 3, 3 , None],
        [None, None, None , None],
    ], [
         (0, 0), (1, 0),(2,3),(3,2),(4,3)
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, None, None , None],
        [None, 3, 3 , None],
        [2, None, None , None],
    ], [
         (0, 0), (0, 2), (2, 2),
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [2, None, None,3,None,3,None],

    ], [
         (0, 1), (0, 3), (0, 6),
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [2, None, None,None],
        [None, None, None,None],
        [None, None, 3,3],
        [None, 3, None,None],
    ], [
         (1, 1), (1, 3), (3, 0),(3, 3),
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [3, None, None,None,3],
        [None, None, 1,None,None],

    ], [
         (0, 1), (0, 2),(0,3)
    ]),
    max_moves=1
),
 Level(
    Grid( [
        [3, None, None,None],
        [3, None, None,None],
        [None, None, None,None],
        [None, 1, None,None],
        [None, None, None,3],
    ], [
         (1, 0), (2, 0), (4, 0),(4, 2),
    ]),
    max_moves=1
),
 Level(
    Grid( [
        [3, None, None,None, 3 , 3],
        [None, None, None,None, None , None],
        [None, None, None,1, None , None],
    ], [
         (0, 3), (0, 4), (1, 1),(2, 1),
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, None, None,3],
        [None, None, None,None],
        [3, None, None,None],
        [3, None, None,1],
    ], [
         (1, 0), (1, 2), (2, 1),(2, 2),
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, 3, None,3 ,None],
        [None, None, 2,None ,None],
        [None, None, 1,None ,None],
    ], [
         (0, 0), (0, 2), (1, 4),(2, 4),
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, None, None,None,None],
        [None, None, 3,None,None],
        [1, None, None,None,2],
        [None, None, 3,None,None],
        [None, None, None,None,None],
    ], [
         (0, 3), (0, 4), (4, 0),(4, 3),
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [1, None, 3,None],
        [None, None, None,None],
        [3, None, None,None],
        [None, None, None,2],
    ], [
         (1, 1), (2, 2), (1, 3),(3, 1),
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, None, None,3,None,None],
        [None, None, None,None,None,None],
        [3, None, None,None,None,3],
        [None, None, None,None,None,None],
        [None, None, 1,2,None,None],
    ], [
         (1, 3), (2, 1), (2, 2),(2, 3),(2,5)
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, 3, 2,3,None],
        [None, None, None,None,None],
        [None, None, 1,None,None],
        [None, None, None,None,None],
        [None, 3, None,3,None],
    ], [
         (1, 0), (1, 4), (2, 1),(3, 0),(3,2),(3,4)
    ]),
    max_moves=4
),
 Level(
    Grid( [
        [None, 3, 3,None],
        [None, None, None,None],
        [None, None, None,None],
        [None, None, None,None],
        [3, None, 2,1],
    ], [
         (0, 1), (0, 3), (1, 0),(2, 0),(3,0)
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [None, 3, None,None],
        [None, 3, 3,None],
        [2, None, None,1],
    ], [
         (0, 2), (1, 0), (2, 0),(1, 1),(2,1)
    ]),
    max_moves=2
),
 Level(
    Grid( [
        [2, None, None,3,3],
        [None, None, None,None,None],
        [None, None, None,None,None],
        [3, None, 1,None,None],
    ], [
         (0, 1), (0, 3), (1, 0),(1, 4),(2,1)
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [None, None, None,3,None],
        [None, None, None,None,3],
        [3, None, None,None,None],
        [None, None, 1,None,2],
    ], [
         (0, 2), (2, 1), (2, 2),(2, 3),(3,2)
    ]),
    max_moves=3
),

 Level(
    Grid( [
        [None, 3, None,None,None],
        [None, None, None,3,2],
        [None, None, None,None,None],
        [1, None, None,None,3],
        [None, None, None,None,None],
    ], [
         (0, 3), (2, 1), (2, 3),(4, 1),(4,2)
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [3, None, None,1],
        [None, None, 3,None],
        [None, None, None,None],
        [None, None, 3,None],
        [2, None, None,3],
    ], [
         (0, 0), (0, 3), (2, 0),(4, 0),(4,1),(4,2)
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [None, None, None,None, None],
        [2, 3, None,None, None],
        [None, None, None,3, None],
        [1, None, None,None, None],
    ], [
         (0, 0), (3, 0), (3, 2),(3, 3),
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [None, None, None,None, 3,None],
        [None, None, None,None, None,None],
        [None, 3, None,1, 3,None],
        [None, 2, None,1, 3,None],
    ], [
         (0, 1), (0, 2), (0, 3),(0, 5),
         (1, 1), (1, 4),
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [None, 3, None],
        [None, None, None],
        [None, None, 2],
        [1, None, None],
        [None, 3, None],
        [None, 3, None],
    ], [
         (1, 0), (1, 2), (2, 1),(4, 1),
         (5, 0),
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [None, None, None,3, None,None,None],
        [None, 3, None,1, None,None,None],
        [None, None, None,None, None,3,None],
        [None, 2, 3,None, None,1,None],
    ], [
         (0, 5), (0, 6), (1, 0),(1, 1),
         (1, 3),(1, 6),(2, 2),
    ]),
    max_moves=3
),
 Level(
    Grid( [
        [None, None, 3,None, None],
        [None, None, None,None, None],
        [None, None, None,None, None],
        [1, None, None,None, 3],
        [None, None, 3,None, None],
        [None, None, 2,None, None],
    ], [
         (1, 1), (1, 3), (2, 2),(3, 3),
         (4, 1),
    ]),
    max_moves=3
),
    ]
