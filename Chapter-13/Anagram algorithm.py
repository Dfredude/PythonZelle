def anagrams(s:str):
    if s == '': return [s]
    else: 
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                print(w[:pos] + s[0] + w[pos:])
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans

print(anagrams('abc'))
