liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

first_node = 'B'

swap_list = []
def cal(path,flag):
  tol = 5
  pre = "tokenB"
  now = "tokenB"
  amountin = tol
  amountout = tol
  for i in range(len(path)-1):
    if(path[i+1] == 'A'):
      now = "tokenA"
    elif(path[i+1] == 'B'):
      now = "tokenB"
    elif(path[i+1] == 'C'):
      now = "tokenC"
    elif(path[i+1] == 'D'):
      now = "tokenD"
    else:
      now = "tokenE"
    if(pre > now):
      y , x = liquidity[(now , pre)]
    else :
      x , y = liquidity[(pre , now)]
    tol = (997 * tol * y)/(1000 * x + 997 * tol)

    if flag==1:
      amountout = tol
      global swap_list
      swap_list.append([amountin, amountout])
      amountin = amountout

    pre = now
  if pre < "tokenB":
    x, y = liquidity[(pre, "tokenB")]
  else :
    y, x = liquidity[("tokenB", pre)]
  tol = (997 * tol * y)/(1000 * x + 997 * tol)
  if flag==1:
      amountout = tol
      swap_list.append([amountin, amountout])
      amountin = amountout
  return tol



def dfs(graph, node, visited, path):
    visited[node] = True
    path.append(node)
    sum = 0

    if(len(path) > 1):
      sum = cal(path,0)

    if sum >= 20:
      sum = cal(path,1)
      ans = path.copy()
      ans.append('B')
      ans = ['token' + i for i in ans]
      print(" -> ".join(ans), ", tokenB balance=",sum)
      return

    else:
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited, path)

    visited[node] = False
    path.pop()


graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['A', 'B', 'C', 'D']
}

# 初始化
visited = {node: False for node in graph}
path = []

# 從點 B 開始進行 DFS
dfs(graph, 'B', visited, path)
for i in range(len(swap_list)):
  print("SWAP ", i+1, " : amountIn = ",swap_list[i][0],", amountOut = ",swap_list[i][1])

#test = ['B','A','D']
#cal(test)