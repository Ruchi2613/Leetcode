from typing import List, Any


class next_largest_element_to_left:
    @staticmethod
    def next_largest_element(nums: List[int]) -> list[Any]:

        stack = []
        res = []

        for num in nums:
            if not stack:
                res.append(-1)
            elif num < stack[-1]:
                res.append(stack[-1])
            elif num >= stack[-1]:
                while stack and num >= stack[-1]:
                    stack.pop()
                res.append(-1)
            stack.append(num)

        return res



cl = next_largest_element_to_left()
print(cl.next_largest_element(nums=[1,3,2,6,4]))


'''Notes:
Add @staticmethod above the method.

Remove self from parameters.

Now you can call it like:
ClassName.method_name(args)

self is not used in static methods.

You can call static methods directly with the class name.

Useful when method doesn't depend on instance variables.

In Python, when you define a method with @staticmethod, it becomes independent of the class instance — but you can still access it through the instance.

Python just ignores the self part and executes the method normally.

So both these will work:

--Using class name (recommended for static):

next_largest_element_to_left.next_largest_element([1,3,2,6,4])

--Using object (allowed, but not necessary):

cl = next_largest_element_to_left()
cl.next_largest_element([1,3,2,6,4])

1. Static method (@staticmethod):
✅ Can be called using:

Class name: ClassName.method()

Object: object.method()

❌ Does not use self

✅ No object (instance) needed to call it — but you can use one.

2. Instance method (with self):
✅ Must be called using object only: object.method()

❌ Cannot be called directly using class name (unless you manually pass an object as the first argument)

✅ Uses instance variables via self
'''


'''2 Note:
Example to clarify:

class Test:
    def instance_method(self):
        print("I'm an instance method")

    @staticmethod
    def static_method():
        print("I'm a static method")
        
        
Calling:

t = Test()

t.instance_method()       # ✅ OK
Test.instance_method()    # ❌ Error: missing 1 required positional argument 'self'

t.static_method()         # ✅ OK
Test.static_method()      # ✅ OK


'''









