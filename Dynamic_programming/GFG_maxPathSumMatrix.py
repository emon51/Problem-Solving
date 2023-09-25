
def _valid(r ,c, n):
	return r>=0 and r<n and c>=0 and c<n
	
def f(mat, n, r, c):
	if not _valid(r, c, n):
		return 0 
	if r == n-1:
		return mat[r][c]
	return mat[r][c]+max(f(mat, n, r+1,c-1), f(mat, n, r+1,c), f(mat, n, r+1,c+1))
	
	
if __name__ == "__main__":
	mat=[[1, 2], [3, 4]] 
	res = 0 
	n = len(mat)
	for c in range(n):
		res = max(res, f(mat, n, 0, c))
	print(res)
	