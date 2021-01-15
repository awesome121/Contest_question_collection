"""
Solutions to 'island of love' 

Auther: Changxing Gong

"""



"""Using BFS traverses the relationship recursively"""

def main():
    N, F, Q = [int(i) for i in input().split()]
    adj_ls = [[] for i in range(N+1)]
    for _ in range(F):
        l_val, r_val = [int(i) for i in input().split()]
        adj_ls[l_val].append(r_val)
        adj_ls[r_val].append(l_val)
        
    for _ in range(Q):
        mode, l_val, r_val = input().split()
        if mode == 'E':
            adj_ls[int(l_val)].remove(int(r_val))
            adj_ls[int(r_val)].remove(int(l_val))
        else:
            visited = [0 for _ in range(len(adj_ls))]
            visited[int(l_val)] = 1      
            if is_connected(visited, adj_ls, int(l_val), int(r_val)):
                print("YES")
            else:
                print("NO")
                
def is_connected(visited, adj_ls, l_val, r_val):
    #print(visited)
    for adj_node in adj_ls[l_val]:
        if visited[adj_node] == 0:
            visited[adj_node] = 1
            if adj_node == r_val or is_connected(visited, adj_ls, adj_node, r_val):
                return True
    return False
            
main()
            
            


"""Using BFS traverses the relationship iteratively (using stack)"""

def main():
    N, F, Q = [int(i) for i in input().split()]
    adj_ls = [[] for i in range(N+1)]
    for _ in range(F):
        l_val, r_val = [int(i) for i in input().split()]
        adj_ls[l_val].append(r_val)
        adj_ls[r_val].append(l_val)
        
    for _ in range(Q):
        mode, l_val, r_val = input().split()
        if mode == 'E':
            adj_ls[int(l_val)].remove(int(r_val))
            adj_ls[int(r_val)].remove(int(l_val))
        else:
            visited = [0 for _ in range(len(adj_ls))]
            visited[int(l_val)] = 1
            stack = [int(l_val)]
            found = False
            while stack and not found:
                value = stack.pop()
                for adj_node in adj_ls[value]:
                    if visited[adj_node] == 0:
                        visited[adj_node] = 1
                        stack.append(int(adj_node))
                        if adj_node == int(r_val):
                            found = True
                            break
                
            if found:
                print("YES")
            else:
                print("NO")
                
            
main()
            
            



