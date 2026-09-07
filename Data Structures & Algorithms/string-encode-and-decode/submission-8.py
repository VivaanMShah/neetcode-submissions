class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for i in strs:
            leng = str(len(i))
            final_str+=leng+"#"+str(i)
        print(final_str)
        return final_str


    def decode(self, s: str) -> List[str]:
       index = 0
       final_list = []
       while index < len(s):
            digit = ""
            digit_idx = index
            while s[digit_idx].isdigit():
                digit += s[digit_idx] 
                digit_idx += 1
            digit = int(digit) if digit else 0
            index = digit_idx - 1
            final_index = index + 2 + digit
            final_list.append(s[index+2: final_index] if digit != 0 else "")
            index = final_index
       return final_list

