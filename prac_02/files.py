# Question 1
out_file = open("name.txt")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt")
name = in_file.read().strip()
in_file.close()
print("Your name is,", name)

# Question 3
in_file = open("numers.txt")
number_1 = int(in_file.readline().strip())
number_2 = int(in_file.readline().strip())
in_file.close()
print(number_1 + number_2)

# Question 4
in_file = open("numbers.txt")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)