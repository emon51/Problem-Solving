
#    https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=false


#Brute_Forces-(TLE)

def repeatedString(s, n):
    
    temp_s = s
    while len(s) < n:
        s += temp_s
    
    cnt = 0
    for i in range(n):
        cnt += 1 if s[i] == 'a' else 0
    
    return cnt  

#Optimal

def repeatedString(s, n):
    
    a_cnt = s.count('a')
    s_len = len(s)
    
    req_repeatation = n // s_len
    total_a_cnt = a_cnt * req_repeatation + s[: n % s_len].count('a')
    return total_a_cnt
