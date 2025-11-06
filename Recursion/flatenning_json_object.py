
# Problem Statement: Flattening a JSON Object
# You are given a nested JSON object (i.e., a dictionary in Python) that may contain other dictionaries or lists
#  as its values. Your task is to flatten this JSON object — meaning you must convert it into a single-level 
# dictionary where the nested keys are represented in a dot notation (".") or another consistent format.

'''
# Input1:
{
  "name": "Alice",
  "details": {
    "age": 25,
    "address": {
      "city": "London",
      "zip": "E1 6AN"
    }
  }
}

# Output1:
{
  "name": "Alice",
  "details.age": 25,
  "details.address.city": "London",
  "details.address.zip": "E1 6AN"
}

# Input2: 
{
  "user": {
    "name": "Bob",
    "hobbies": ["cricket", "reading"]
  }
}

# Output2: 
{
  "user.name": "Bob",
  "user.hobbies.0": "cricket",
  "user.hobbies.1": "reading"
}

'''
'''
# 1
class Solution:
    def flatenning_JSON_object(self, json_obj):
        
        res = []
        def rec(mapp, prev = ''):
            for key, value in mapp.items():
                if not isinstance(value, dict):
                    if not isinstance(value, list):
                        new = f"{prev}.{key}:{value}"
                        res.append(new)
                    else:
                        for index, list_val in enumerate(value):
                            new = f"{prev}.{key}.{index}:{list_val}"
                            res.append(new)
                else:
                    rec(value, f"{prev}.{key}")


        rec(json_obj)
        return res

# print(__name__)
'''
'''
# 2 
class Solution:
    def flattenning_JSON_object(self, json_obj):
        
        res = {}
        def rec(mapp, prev = ''):
            for key, value in mapp.items():
                if not isinstance(value, dict):
                    if not isinstance(value, list):
                        new = f"{prev}.{key}"
                        res[new] = value 
                    else:
                        for index, list_val in enumerate(value):
                            new = f"{prev}.{key}.{index}"
                            res[new] = list_val 
                else:
                    rec(value, f"{prev}.{key}")


        rec(json_obj)
        return res
'''
'''
# 3 
class Solution:
    def flattenning_JSON_object(self, json_obj):
        
        res = {}
        def rec(mapp, prev = ''):
            for key, value in mapp.items():
                if not isinstance(value, dict):
                    if not isinstance(value, list):
                        new = f"{prev}.{key}" if prev else key 
                        res[new] = value 
                    else:
                        for index, list_val in enumerate(value):
                            new = f"{prev}.{key}.{index}" if prev else f"{key}.{index}"
                            res[new] = list_val 
                else:
                    rec(value, f"{prev}.{key}" if prev else key )


        rec(json_obj)
        return res
'''
# 4 

class Solution:
    def flattenning_JSON_object(self, json_obj):
        
        res = {}
        def rec(mapp, prev = ''):
            for key, value in mapp.items():
                new = f"{prev}.{key}" if prev else key 
                if not isinstance(value, dict):
                    if not isinstance(value, list):
                        res[new] = value 
                    else:
                        for index, list_val in enumerate(value):
                            res[f"{new}.{index}"] = list_val 
                else:
                    rec(value, new)


        rec(json_obj)
        return res


if __name__ == "__main__":
    solve = Solution()
    json_obj = {
  "name": "Alice",
  "details": {
    "age": 25,
    "address": {
      "city": "London",
      "zip": "E1 6AN"
    }, 
    "interests": ["Cycling", "Traveling"]
    
  }
}
    res = solve.flatenning_JSON_object(json_obj)
    print(res)

