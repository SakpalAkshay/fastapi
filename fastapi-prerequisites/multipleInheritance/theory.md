Inheritance in Python is a mechanism that allows you to create a new class (the subclass or derived class) based on an existing class (the superclass or base class). The subclass inherits attributes and methods from the superclass, which promotes code reuse and supports the concept of **"is-a"** relationships.

 ## Key points about inheritance:

1. The derived class inherits all attributes and methods of the base class.
2. You can override methods in the derived class to provide specialized behavior.
3. Inheritance supports code reuse and promotes a hierarchical structure in your code.
4. Multiple levels of inheritance (subclass of a subclass) are possible, allowing for complex class hierarchies.



### Multiple Inheritance
Multiple Inheritance in Python is a feature that allows a class to inherit attributes and methods from multiple base classes. This means that a class can inherit from more than one parent class, combining their functionalities. While powerful, multiple inheritance can lead to complex class hierarchies and potential issues, so it should be used judiciously.

## Key points about multiple inheritance:

1. When a method or attribute is called on an instance of the derived class, Python looks for it in the derived class first. If not found, it searches through the base classes from left to right (in the order listed in the class definition) until it finds a match.
2. If there are naming conflicts (i.e., two base classes have methods or attributes with the same name), the method or attribute from the first base class listed in the parentheses takes precedence. You can access the method from the other base class using the class name.
3. Be cautious when using multiple inheritance, as it can lead to complex class hierarchies and potential ambiguities if not managed carefully. It's generally recommended to use it sparingly and consider alternative design patterns like composition when possible.

