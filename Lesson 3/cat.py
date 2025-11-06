#for loop that iterates on variable "i" on a list
for i in range(10):
  print("meow")

#declaring variable "i" with value "0"
i = 0
#while loop to iterate on variable "i"
while i < 3:
  print("meow")
  i += 1

#print meow 3 times + override default print end function
print("meow\n" * 3, end="")

while True:
  n = int(input("What's n?: "))
  if n > 0:
    break

for _ in range(n):
  print("meow")
