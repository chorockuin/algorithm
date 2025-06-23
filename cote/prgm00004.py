def get_changable_words(begin, words_dict):
    changable_words = []
    for w, _ in words_dict.items():
        c = 0
        for i in range(len(w)):
            if begin[i] != w[i]:
                c += 1
        if c == 1:
            changable_words.append(w)
    return changable_words

def dfs(begin, target, words_dict, memo):
    if begin in memo:
        return memo[begin]
    
    if begin == target:
        return 0
    
    if (len(words_dict) == 0):
        return -1
    
    min_c = []
    changable_words = get_changable_words(begin, words_dict)
    for w in changable_words:
        words_dict.pop(w)
        c = dfs(w, target, words_dict, memo)
        if c != -1:
            min_c.append(c)
        words_dict[w] = 0
        
    if (len(min_c) == 0):
        memo[begin] = -1
        return -1

    min_c = min(min_c) + 1
    memo[begin] = min_c
    
    return min_c

def solution(begin, target, words):
    words_dict = {}
    memo = {}
    for w in words:
        words_dict[w] = 0
    answer = dfs(begin, target, words_dict, memo)
    if answer == -1:
        return 0
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0


print(set("hot") & set("oth"))