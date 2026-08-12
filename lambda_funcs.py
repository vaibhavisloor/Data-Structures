students = [("alice", 85), ("bob", 92), ("charlie", 78), ("diana", 92)]

students.sort(key=lambda x:x[1],reverse=True)

print(students)

words = ["banana", "apple", "fig", "cat", "kiwi", "mango"]

words.sort(key = lambda x : (len(x),x))

print(words)



nums = [9, 7, 3, 11, 6, 14, 2]

nums.sort(key = lambda x: (x%3,x),reverse=True)

print(nums)




words = ["python", "java", "rust", "go", "ruby"]

words.sort(key = lambda x: (x[::-1]))

print(words)



nums = [21, 9, 105, 32, 74]
nums.sort(key=lambda x: sum(int(a) for a in str(x)))
print(nums)



words = ["education", "sky", "apple", "rhythm", "ocean"]

words.sort(key= lambda x: sum(1 for a in x if a in {'a','e','i','o','u'}))

print(words)