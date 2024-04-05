import sys
readline = sys.stdin.readline

def solve(map):
  n = len(map)
  def traverse(r, c, d):
    if d == 1:
      return map[r][c]
    nd = d // 2
    nw = traverse(r, c, nd)
    ne = traverse(r, c + nd, nd)
    sw = traverse(r + nd, c, nd)
    se = traverse(r + nd, c + nd, nd)
    if len(nw) == 1 and nw == ne == sw == se:
      return nw
    return '(' + nw + ne + sw + se + ')'
  return traverse(0, 0, n)

n = int(readline())
rows = []
for i in range(n):
  rows.append(readline().strip())
res = solve(rows)
print(res)