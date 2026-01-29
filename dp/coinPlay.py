# Consider a row of n coins of values v1, . . . , vn. We play a
# game against an opponent by alternating turns. In each turn, 
# a player selects either the first or last coin from the row, 
# removes it from the row permanently, and receives the value of 
# the coin. Determine the maximum possible amount of money we can definitely win if we 
# move first. 
# Assume full competency by both players.

# v: list of coin values
# dp_arr: 2D array where dp_arr[i][j] will store the max value
#         the current player can guarantee from subarray v[i..j]
# find_choices(v, dp_arr, a, b) returns dp_arr[a][b] (or computes it if not done)

def max_win(v):
    n = len(v)
    dp_arr = [[0] * n for _ in range(n)]
    
    find_choices(v, dp_arr, 0, n-1)
    
    return dp_arr[0][n-1]


def find_choices(v, dp_arr, start, end):
    if dp_arr[start][end] != 0:
        return dp_arr[start][end]
    
    if start == end:
        dp_arr[start][end] = v[start]
    elif start+1 == end:
        dp_arr[start][end] = max(v[start], v[end])
    else:
        dp_arr[start][end] = max(
                # Option 1: you take the left coin v[start] now.
                # After you take v[start], it's opponent's turn with coins v[start+1 .. end].
                # Opponent has two choices:
                #   - He takes the left of remaining (v[start+1]) => remaining for you: v[start+2 .. end]
                #   - He takes the right of remaining (v[end])      => remaining for you: v[start+1 .. end-1]
                # From those two remaining intervals, your future guaranteed values are:
                #   find_choices(... start+2, end)    and find_choices(... start+1, end-1)
                # Because the opponent plays to minimize *your* final value, he will leave you
                # the worse (minimum) of these two. So total if you pick left now:
                v[start] + min(find_choices(v, dp_arr, start+2, end), find_choices(v, dp_arr, start+1, end-1)),

                # Option 2: you take the right coin v[end] now.
                # Symmetric reasoning:
                # After you take v[end], opponent can take:
                #   - left of remaining (v[start]) => remaining for you: v[start+1 .. end-1]
                #   - right of remaining (v[end-1])=> remaining for you: v[start .. end-2]
                # Your future guaranteed values are:
                #   find_choices(... start+1, end-1) and find_choices(... start, end-2)
                # Opponent will leave you the minimum of those, so total if you pick right now:
                v[end] + min(find_choices(v, dp_arr, start+1, end-1), find_choices(v, dp_arr, start, end-2))
            )
    return dp_arr[start][end]



# Example usage:
v = [8, 15, 3, 7]
print(max_win(v))  # Output: 22