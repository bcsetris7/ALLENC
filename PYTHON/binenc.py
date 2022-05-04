import time
  
print("\n===========================================\n")

print("\nEnter any number to see its binary form.\n")

print("\n===========================================\n")
time.sleep(0.5)
print("\nEnter your num:\n")

time.sleep(0.5)
n = int(input('==>')) 
bin = "" 
temp = n 

while n>0:
    rem = n % 2
    bin+=str(rem) 
    n = n // 2
print("Binary Form Of",temp,"is",bin[::-1],"\n")
time.sleep(0.5)
print("belajar dari sini gan <-_->\n")
time.sleep(1)
print("bye"
