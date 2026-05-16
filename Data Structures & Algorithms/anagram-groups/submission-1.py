class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = []
        result = []
        for string in strs:
            mapping = {}
            for character in string:
                mapping[character] = mapping.get(character, 0) + 1
            
            dict_list.append(mapping)

        for i in range(len(dict_list)):
            if dict_list[i] == None: continue
            addition = [strs[i]]
            for j in range(i + 1, len(dict_list)):
                if dict_list[i] == dict_list[j]:
                    addition.append(strs[j])
                    dict_list[j] = None

            result.append(addition)
                
        return result

