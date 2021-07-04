import java.io.*;

class Parent1{

    void print(){

        System.out.println("Inside Parent1 class");

    }

}

class Parent2{

    void print(){

        System.out.println("Inside Parent2 class");

    }

}

class Child extends Parent1 , Parent2{

    public static void main(String arg[]){

        Child c = new Child();

        c.print();

    }

}

/*

Error :

Child.java:23: error: '{' expected
class Child extends Parent1 , Parent2{

*/

Ajay Binay Institute Of Technology