package com.packg;
// package in java is the collection of classes and interfaces that are bundled together as they are related to each other
public class Main {
    // public class and method means they are accessible from outside the class and package and can be called from anywhere in the project
    // static means that the method belongs to the class and not any object of the class and can be called without creating an object of the class
    // void means that the method does not return any value and is used just to perform an action
    // main is the name of the method and is the entry point of the program and is called by the JVM when the program is executed
    // String[] args is the parameter of the main method and is used to accept command line arguments
    // throws Exception is used to handle exceptions that may occur during the execution of the program
    public static void main(String[] args) throws Exception {
        // creating an object of the User class and passing the name of the user as an argument to the constructor
        User user = new User("John");
        System.out.println(user.name);
        user.sayHello();

        // create a new object of the User class without constructor
        User user2 = new User("John");
        user2.age = "52";
        System.out.println(user2.age);

        // interface example
        TaxCalculator calculator = getCalculator();
        calculator.calculateTax();

        // encapsulation example
        var account = new Account();
        account.deposit(10);
        account.withdraw(5);
        System.out.println(account.getBalance());

        // abstraction example
        var mailService = new MailService();
        mailService.sendMail();
    }
    // static method that returns an object of the TaxCalculator2024 class
    public static TaxCalculator getCalculator(){
        return new TaxCalculator2024();
    }
}
