class Solution:
    def decodeString(self, s: str) -> str:
        decoder_stack = []
        encoded_str = ""
        str_multiplier= ""

        for c in s:
            if c == ']':
                x = len(decoder_stack)-1
                while x >= 0 and encoded_str.count('[') < 2:
                    if not decoder_stack[x].isdigit():
                        if str_multiplier: break
                        encoded_str += decoder_stack.pop()
                    else:
                        str_multiplier += decoder_stack.pop()
                    x -= 1
                decoder_stack.extend(list(encoded_str.replace("[", "")[::-1] * int(str_multiplier[::-1])))
                encoded_str = str_multiplier = ""
            else:
                decoder_stack.append(c)
        return "".join(decoder_stack)