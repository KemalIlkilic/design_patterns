# Builder

## Explanation

Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to
produce different types and representations of an object using the same construction code.

## Relations with Other Patterns

• Builder focuses on constructing complex objects step by step.
Abstract Factory specializes in creating families of related
objects. Abstract Factory returns the product immediately,
whereas Builder lets you run some additional construction
steps before fetching the product.

• You can use Builder when creating complex Composite trees
because you can program its construction steps to work
recursively.

• You can combine Builder with Bridge: the director class plays
the role of the abstraction, while different builders act as
implementations.

• Abstract Factories, Builders and Prototypes can all be imple-
mented as Singletons.
