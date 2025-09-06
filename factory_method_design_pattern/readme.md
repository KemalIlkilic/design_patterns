# Factory Method

## Explanation

Provides an interface for creating objects in superclass but allows subclasses to alter the type of objects that will be created.

## Relations with Other Patterns

• Many designs start by using Factory Method (less complicat-
ed and more customizable via subclasses) and evolve toward
Abstract Factory,Prototype,or Builder( more flexible, but more
complicated ).

• Abstract Factory classes are often based on a set of Facto-
ry Methods, but you can also use Prototype to compose the
methods on these classes.

• You can use Factory Method along with Iterator to let collec-
tion subclasses return different types of iterators that are compatible with the collections.

• Prototype isn’t based on inheritance, so it doesn’t have its
drawbacks. On the other hand, Prototype requires a complicat-
ed initialization of the cloned object. Factory Method is based
on inheritance but doesn’t require an initialization step.

• Factory Method is a specialization of Template Method. At the
sametime,a Factory Method may serve as a step in a large Template Method.
