package com.packg;

public class User {
    // public means that the variable is accessible from outside the class and package
    // attribute of the class is a variable that is associated with an object and is used to define the properties of an object
    public String name;
    public String age;

    // Constructor is a special type of method that is used to initialize the object
    // It is called when an object of the class is created and memory is allocated for the object
    public User(String name) {
        this.name = name;
    }

    public void sayHello(){
        System.out.println("Hi, my name is " + name);
    }
}
