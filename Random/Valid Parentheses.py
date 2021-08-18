class Solution:
    def isValid(self, s) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            if "()" in s:
                s= s.replace("()","")
            if "[]" in s:
                s= s.replace("[]","")
            if "{}" in s:
                s= s.replace("{}","")
        return s == ""
