package com.packg;
// interface: a collection of abstract methods. A class implements an interface, thereby inheriting the abstract methods of the interface
// interface is used to provide a way to define a contract for the subclasses to implement
// example: if you want to build a TaxCalculator class, that class should have this signature methods
public interface TaxCalculator {
    // abstract method
    float calculateTax();  // this method can't have a body
}
