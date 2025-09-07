# Prototype

## Explanation

It is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

The pattern declares a common interface for all objects that support cloning. This interface lets you clone an object without coupling your code to the class of that object. Usually, such an interface contains just a single clone method.

The method creates an object of the current class and carries overall of the fiel dvalues of the old object in to the new one.

An object that supports cloning is called a prototype.

## How it works

You create a set of objects, configured in various ways.
When you need an object like the one you’ve configured, you just clone a prototype instead of constructing a new object from scratch.

## Relations with Other Patterns

The Singleton object can be mutable. Flyweight objects are immutable.
