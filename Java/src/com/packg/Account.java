package com.packg;
// explains encapsulation
public class Account {
    // balance kept private so that it cannot be accessed or assigned from outside the class
    private float balance;

    // real example of encapsulation
    public void deposit(float amount){
        if(amount > 0){
            this.balance += amount;
            System.out.println("Deposited: " + amount);
        }
    }

    public void withdraw(float amount){
        if(amount > 0 && this.balance >= amount){
            this.balance -= amount;
            System.out.println("Withdrawn: " + amount);
        }
    }

    // setter method to set the balance, where we can set some validation rules for setting the balance
    public void setBalance(float balance){
        if(balance > 0){
            this.balance = balance;
        }
    }

    // getter method to get the balance
    public float getBalance(){
        return balance;
    }
}
