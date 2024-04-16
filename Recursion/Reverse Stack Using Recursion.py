


def reverseStack(stack: List[int]) -> None:
    
    def fun(st):
        if not st:
            return 
        tmp = st.pop(0)
        fun(st)
        st.append(tmp)
    
    fun(stack)
    return stack
