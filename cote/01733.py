from typing import List
from collections import defaultdict

# 언어의 개수 n : 2 <= n <= 500
# 사용자 수 m : 1 <= m <= 500
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cant_talk_users = set()
        for f in friendships:
            user1_languages = set(languages[f[0]-1])
            user2_languages = set(languages[f[1]-1])
            # print(f'user1: {f[0]} language: {user1_languages}')
            # print(f'user2: {f[1]} language: {user2_languages}')
            intersection_languages = list(user1_languages & user2_languages)
            if len(intersection_languages) == 0:
                cant_talk_users.add(f[0])
                cant_talk_users.add(f[1])
        if len(cant_talk_users) == 0:
            return 0
        merged_languages = []
        for cant_talk_user in cant_talk_users:
            merged_languages.extend(languages[cant_talk_user-1])
        teach_lang = max(merged_languages,key=merged_languages.count)
        teach_lang_num = 0
        for cant_talk_user in cant_talk_users:
            if teach_lang not in languages[cant_talk_user-1]:
                teach_lang_num += 1
        return teach_lang_num
    
print(Solution().minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]])) # 1
print(Solution().minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]])) # 2
print(Solution().minimumTeachings(11,[[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]],[[1,4],[1,2],[3,4],[2,3]])) # 0
print(Solution().minimumTeachings(17,
                                  [[4,7,2,14,6],[15,13,6,3,2,7,10,8,12,4,9],[16],[10],[10,3],[4,12,8,1,16,5,15,17,13],[4,13,15,8,17,3,6,14,5,10],[11,4,13,8,3,14,5,7,15,6,9,17,2,16,12],[4,14,6],[16,17,9,3,11,14,10,12,1,8,13,4,5,6],[14],[7,14],[17,15,10,3,2,12,16,14,1,7,9,6,4]],
                                  [[4,11],[3,5],[7,10],[10,12],[5,7],[4,5],[3,8],[1,5],[1,6],[7,8],[4,12],[2,4],[8,9],[3,10],[4,7],[5,12],[4,9],[1,4],[2,8],[1,2],[3,4],[5,10],[2,7],[1,7],[1,8],[8,10],[1,9],[1,10],[6,7],[3,7],[8,12],[7,9],[9,11],[2,5],[2,3]])) # 4