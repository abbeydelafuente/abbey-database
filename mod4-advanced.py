# ADVANCED PYTHON

# 1 Relationship Status

def relationship_status(from_member, to_member, social_graph):
    from_following = social_graph.get(from_member, {}).get('following', [])
    to_following = social_graph.get(to_member, {}).get('following', [])
    
    if to_member in from_following and from_member in to_following:
        return "friends"
    elif to_member in from_following:
        return "follower"
    elif from_member in to_following:
        return "followed by"
    else:
        return "no relationship"
    
# sample data
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

# test
output = relationship_status("@joaquin", "@chums", social_graph)
print(output)

output = relationship_status("@chums", "@joaquin", social_graph)
print(output) 

output = relationship_status("@joeilagan", "@bongolpoc", social_graph)
print(output) 

output = relationship_status("@eeebeee", "@jobenilagan", social_graph)
print(output)
      
# 2 Tic Tac Toe
def tic_tac_toe(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]
    for col in range(len(board)):
        if len(set([row[col] for row in board])) == 1 and board[0][col] != '':
            return board[0][col]
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != '':
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1 and board[0][len(board)-1] != '':
        return board[0][len(board)-1]
    return "NO WINNER"

# sample data
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

# test
print(tic_tac_toe(board1))
print(tic_tac_toe(board2))
print(tic_tac_toe(board3))
print(tic_tac_toe(board4))
print(tic_tac_toe(board5))
print(tic_tac_toe(board6))
print(tic_tac_toe(board7))
  
# 3 
def eta(first_stop, second_stop, route_map):
    total_time = 0
    current_stop = first_stop
    
    while current_stop != second_stop:
        if (current_stop, second_stop) in route_map:
            total_time += route_map[(current_stop, second_stop)]['travel_time_mins']
            break  
        found_next_stop = False
        for route in route_map:
            if route[0] == current_stop:
                total_time += route_map[route]['travel_time_mins']
                current_stop = route[1]
                found_next_stop = True
                break       
        if not found_next_stop:
            raise ValueError('Invalid route map')
    return total_time
