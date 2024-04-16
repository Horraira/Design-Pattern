package com.packg;
// explains abstraction
public class MailService {
    public void sendMail(){
        connect();
        authenticate();
        disconnect();
    }

    // made the methods private so that they cannot be accessed from outside the class
    private void connect(){
        System.out.println("Connected to mail server.");
    }

    private void disconnect(){
        System.out.println("Disconnected from mail server.");
    }

    private void authenticate(){
        System.out.println("Authenticated.");
    }
}
