class Solution:
    def isValid(self, s: str) -> bool:
        # is_good=True
        # for i in range(len(s)):
        #     for j in range(i+1,i+2):
                
        #         n=s[i:j+2]
        #         print(n)
        #         if n == "[]":
        #             is_good=True
        #         elif n == "()":
        #             is_good=True
        #         elif n == "{}":
        #             is_good=True
        #         else:
        #             is_good=False
        # return is_good

        
        # stack = []
        
        # mapping = {")": "(", "}": "{", "]": "["}

        # for char in s:
        #     if char in mapping: 
        #         top_element = stack.pop() if stack else '#'
                
        #         if mapping[char] != top_element:
        #             return False
        #     else:
        #         stack.append(char)

        # return not stack

        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # If it's a closing bracket
            if ch in pairs:
                # If stack is empty OR top is not matching opening bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                # If matching, remove the opening bracket from stack
                stack.pop()
            else:
                # If it's an opening bracket, push into stack
                stack.append(ch)

        # If stack is empty => all brackets matched
        return len(stack) == 0