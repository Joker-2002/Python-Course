# Mutable and Immutable
- Mutable => means its value can be changed runtime(in the same address)
    - If two variables is assign to same value. different reference is given (as immutable) to both variables.
    ## example:
    ``` python
    list1 = [1,2,3,4] #list1 has different address for the list
    list2 = [1,2,3,4] #list2 has different address for the list
    list1[1] = 55
    print(list1)
    print(list2)
    ``` 
- Immutable => means its value cannot be changed in meanwhile/runtime(in the same memory address).we have to assign new var for that.
    - If two variables is assign to same value. same reference is given (as mutable) to both variables.
    ### example:
    ```python
    num1 = 5  #num1 has same address for the 5 as num2
    num2 = 5  #num1 has same address for the 5 as num2
    num1 = 7
    print(num1)
    print(num2)
    ```

# OBJECT TYPES / DATA TYPES

### Variables doesn't have datatype it is just a container. However Datatype/Object type is only for the values assigned to that variable. example:
```python
score = 100 #here score is just a variable. The value 100 is a datatype known as Number.
```

- Numbers : 1234, 3.145, 3+4j, 0b111, Decimal(),Fraction()

- String : 'spam', "Bob's", b'a\x01c',u'sp\xc4m'

- List : [1,2,'spam',['three',4],7], list(range(10))

- Tuple : (1,'spam',5,'U'),tuple('spam'),namedtuple

- Dictionary : {'food':'spam','taste':'yum',1:'key'} , dict(hours=10)

- Set : set('abc'),{'a','b','c'}

- File : open("new.txt"), open(r'C:\ham.bin','wb')

- Boolean : True,False

- None : None

- Functions, Modules, Classes

- Advance : Decorators,Generators,Iterators,Meta Programming