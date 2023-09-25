#0/1 knapsack

#W -> weights array
#V -> values array
#C -> capacity

def f(i, W, V, C):
	if i == len(W)-1:
		return V[i] if W[i] <= C else 0
	pick = float("-inf") 
	if W[i] <= C:
		pick = V[i] + f(i+1, W, V, C-W[i])
	notPick = f(i+1, W, V, C)
	
	return max(pick, notPick)
	
if __name__ == "__main__":
	W = [2, 3, 5]
	V = [30, 40, 50]
	C = 6
	print(f(0, W, V, C))