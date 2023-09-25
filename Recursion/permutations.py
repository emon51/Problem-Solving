#print all permutations
# s = "abc"
#op : [cba,bca,bac,cab,acb,abc]

def f(s, p=""):
	if not s:
		print(p, end = " / ")
		return 
	for i in range(len(p)+1):
		s1 = p[:i]
		s2 = p[i:]
		f(s[1:], s1+s[0]+s2)
		
if __name__ == "__main__":
	s = "abc"
	f(s)