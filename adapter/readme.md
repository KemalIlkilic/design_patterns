# Adapter

## Explanation

Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

## How it works

1. Adapter, client’in beklediği interface modelini implement eder.
2. Bunu da yaparken dependency injection ile Adaptee'yi içine alıyor ve halihazırdaki adaptee'nin fonksiyonlarını kendi iç class yapısında kullanıyor. Adaptee'nin fonksiyonlarını kullanıp kendi dönüştürmek istediği interface yapısına dönüştürürken kendi logic'ini de ekliyor ve sonuç olarak client'in beklediği interface yapısında sonuç elde etme amacı güdüyor.
3. Böylece client, Adaptee’nin farklı yapısından habersiz bir şekilde, beklediği interface ile sorunsuz çalışır.
   Client interface ile calısır burası önemli. Adapter'i baz almaz interface yapısını baz alır. Boylece abstraction saglanıyor.

The adapter gets an interface, compatible with one of the existing objects.

Using this interface, the existing object can safely call the adapter’smethods.

Upon receiving a call, the adapter passes the request to the second object,
but in a format and order that the second object expects.

## Relations with Other Patterns
