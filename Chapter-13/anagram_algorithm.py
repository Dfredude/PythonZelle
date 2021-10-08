def getAnagrams(s:str):
    if s == '': return [s]
    else: 
        ans = []
        for w in getAnagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans

if __name__ == "__main__": print(getAnagrams('hello'))
