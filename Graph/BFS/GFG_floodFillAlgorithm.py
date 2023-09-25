from collections import deque
class Solution:
	def floodFill(self, image, sr, sc, newColor):
	    
	    m, n = len(image), len(image[0])
	    q = deque() 
	    q.append((sr, sc, newColor))
	    prev_color = image[sr][sc]
	    image[sr][sc] = newColor
	    vis = set()
	    vis.add((sr, sc))
	    
	    dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
	    
	    def _valid(r, c):
	        return r >= 0 and c >= 0 and r < m and c < n
	        
	    while q:
	        r, c, color = q.popleft()
	        #image[r][c] = color
	        for i, j in dirs:
	            dr, dc = r + i, c + j 
	            if _valid(dr, dc) and (dr, dc) not in vis and image[dr][dc] == prev_color:
	                q.append((dr, dc, color))
	                vis.add((dr, dc))
	                image[dr][dc] = color
	                
	    return image

