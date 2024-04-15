'''
Problem statement
You are given a stack ‘S’. Your task is to sort the sack recursively.



Note:
Looping through the stack is not allowed.
You need to return a stack that is sorted in descending order.


For example:
Given stack S = 1 3 2 
The output will be 3 2 1 since it is the sorted order.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
2
4
1 0 0 2 
3 
2 4 2
Sample Output 1 :
2 1 0 0
4 4 2
Explanation of the Sample Input 1:
For the first test case:
For the given stack, the resultant sorted stack would be 0 0 1 2.  

For the second test case:
For the given stack, the resulting sorted stack would be 2 2 4.   
Sample Input 2 :
2
4
1 2 3 4     
3    
5 1 2
Sample Output 2 :
4 3 2 1 
5 2 1
Constraints:
1 <= T <= 5
1 <=  N <= 2000
0 <= S[i] <= 1000

Where ‘T’ is the total number of test cases, and 'N’ is the size of the stack, and 'S[i]' is the element of the stack.

'''

def sortStack(s):
    if not s:
        return s

    def insert_sorted(stack, element):
        if not stack or stack[-1] <= element:
            stack.append(element)
            return
        else:
            temp = stack.pop()
            insert_sorted(stack, element)
            stack.append(temp)

    def sort_recursive(stack):
        if not stack:
            return
        temp = stack.pop()
        sort_recursive(stack)
        insert_sorted(stack, temp)

    sort_recursive(s)
    return s


