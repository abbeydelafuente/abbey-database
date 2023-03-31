# 1 Relationship Status

def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph.get(from_member, []):
        if from_member in social_graph.get(to_member, []):
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph.get(to_member, []):
        return "followed by"
    else:
        return "no relationship"
      
# 2 Tic Tac Toe
def tic_tac_toe(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return row[0]
    for col in range(len(board[0])):
        if len(set([row[col] for row in board])) == 1 and board[0][col] != "":
            return board[0][col]
    if len(set([board[i][i] for i in range(len(board))])) == 1 and board[0][0] != "":
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1 and board[0][len(board)-1] != "":
        return board[0][len(board)-1]
    return "NO WINNER"
  
# 3 
def eta(first_stop, second_stop, route_map):
    current_stop = first_stop
    total_time = 0
    while current_stop != second_stop:
        for leg, details in route_map.items():
            if current_stop in leg:
                total_time += details['travel_time_mins']
                current_stop = leg[1] if leg[0] == current_stop else leg[0]
                break
    return total_time
