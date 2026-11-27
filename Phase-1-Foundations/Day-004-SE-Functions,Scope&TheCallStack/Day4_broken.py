"""
BROKEN

def add_numbers(a,b):
    result = a + b
    # Bug 1: Missing Return Statement 

def greet(name):
    #Bug 2: variable scope error 
    greeting_text ="Hello " + name

print(greeting_text)

def main():
    sum_result =add_numbers(5, 5)
    print(sum_result) #Will Print "None" Because of Bug 1

    greet("Nahum")

    #Bug 3: Wrong number of argumnts
    add_numbers(10)

if __name__ == "__main__":
    main()

"""
# FIXED 

def add_numbers(a,b):
    result = a + b
    return result
    # Bug 1: Missing Return Statement (Fixed) 

def greet(name):
    #Bug 2: variable scope error (Fixed) 
    greeting_text ="Hello " + name
    print(greeting_text)

def main():
    sum_result = add_numbers(5, 5)
    print(sum_result) #Will Print "None" Because of Bug 1 (Fixed)
    greet("Nahum")

    #Bug 3: Wrong number of argumnts (Fixed)
    add_numbers(10)

if __name__ == "__main__":
    main()
