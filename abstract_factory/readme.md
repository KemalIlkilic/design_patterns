# Abstract Factory

## Explanation

Lets you produce families of related objects without specifying their concrete classes.

2. “Without specifying their concrete classes”

Client (kullanan kod) hangi sınıftan nesne üretiliyor bilmez.
Yalnızca arayüzü (interface/abstract class) bilir.
• Mesela Pistol interface’in olduğunu biliyorsun ama Fiveseven mı Tec9 mı olduğunu bilmiyorsun.
• Hangi “concrete class” kullanılacağına factory karar veriyor.

## Relations with Other Patterns

• Builder focuses on constructing complex objects step by step.
Abstract Factory specializes in creating families of related
objects. Abstract Factory returns the product immediately,
whereas Builder lets you run some additional construction
steps before fetching the product.

• Abstract Factory classes are often based on a set of Facto-
ry Methods, but you can also use Prototype to compose the
methods on these classes.

• Abstract Factory can serve as an alternative to Facade when
you only want to hide the way the subsystem objects are cre-
ated from the client code.

• You can use Abstract Factory along with Bridge. This pairing
is useful when some abstractions defined by Bridge can only
work with specific implementations. In this case, Abstract Fac-
tory can encapsulate these relations and hide the complexity
from the client code.

• Abstract Factories, Builders and Prototypes can all be imple-
mented as Singletons.
