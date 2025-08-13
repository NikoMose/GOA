# 1. შექმენი ცარიელი სია და append()-ით ჩაამატე სამი რიცხვი, შემდეგ დაბეჭდე სიის სიგრძე
fruits = ['apple', 'banana']

fruits.append(5) # [] -> [5]
fruits.append('Hello World')

print(len(fruits))

# 2. სიაში ჩაამატე "apple" და "banana", შემდეგ ჩაამატე "cherry" და დაბეჭდე სია.
fruits.append('apple')
fruits.append('banana')
fruits.append('cherry')
print(fruits)

# 3. შექმენი სია 3 ელემენტით და pop()-ით წაშალე ბოლო ელემენტი, დაბეჭდე რა დარჩა.
nums = [1,2,3,4,5]
print(nums)
nums.pop()
print(nums)

# 4. შექმენი სია და  წაშალე პირველი ელემენტი, დაბეჭდე სია.
nums.pop( 0 )
print(nums)

# 5. შექმენი სია და  ჩასვი "orange" მეორე ადგილას(მეორე ინდექსზე არა. მეორე ადგილას).
fruits.insert(1, 'orange')
print(fruits)

# 6. შექმენი სია და append()-ით ჩაამატე მომხმარებლის შეყვანილი რიცხვი.
userInput = input("შეიყვანეთ რიცხვი: ")
lst = [1,'vashli']
lst.append(userInput)
print(lst)

# 7. შექმენი სია და pop()-ის გამოყენებით წაშალე ბოლო ელემენტი, შემდეგ დაბეჭდე სიის სიგრძე.
nums = [1,2,3,4,5]
print(len(nums))
nums.pop()
print(len(nums))

# 8. შექმენი სია "dog", "cat", "bird" და შუაში ჩაამატე "fish" (insert())
animals = ["dog", "cat", "bird"]
animals.insert(1, 'fish')
print(animals)

# 9. შექმენი სია და ჯერ append()-ით ჩაამატე 5 ელემენტი, შემდეგ ორჯერ გამოიყენე pop() რომ ბოლო ორი ელემენტი წაიშალოს
empty = []
empty.append(1)
empty.append(2)
empty.append(3)
empty.append(4)
empty.append(5)
print(empty)

empty.pop()
empty.pop()
print(empty)
