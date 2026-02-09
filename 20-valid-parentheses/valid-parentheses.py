class Solution:
    def isValid(self, s: str) -> bool:
        # is_good=True
        # for i in range(len(s)):
        #     for j in range(i+1,i+1):
                
        #         n=s[i:j]
        #         if n == "[]":
        #             is_good=True
        #         elif n == "()":
        #             is_good=True
        #         elif n == "{}":
        #             is_good=True
        #         else:
        #             is_good=False
        # return is_good
        stack = []
        # Mapping closing to opening for easy lookup
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping: # If it's a closing bracket
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the opener matches the required opener for this closer
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched correctly
        return not stack