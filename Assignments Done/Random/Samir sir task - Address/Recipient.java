
package com.codekat.project1;

public class Recipient {
    
    String name;
    String contactNumber;
    String email;
    Address address;
    
    Recipient(String name, String contactNumber, String email, Address address) {
        this.name = name;
        this.contactNumber = contactNumber;
        this.email = email;
        this.address = address;
    }
    
    public void getRecipient() {
        System.out.print("Recipient Name : " + this.name + "\n" +
                         "Contact Number : " + this.contactNumber + "\n" + 
                         "Email          : " + this.email + "\n" +
                         " ---- ADDRESS ---- \n" );
        address.getAddress();
    }
    
}
