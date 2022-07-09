package com.codekat.project1;

public class Address {

    String houseName = "";
    String roadNo = "";
    String area = "";
    PostOffice PO;
    String city = "";
    Country country;

    Address(String houseName, String roadNo, String area, String city, Country country) {
        this.houseName = houseName;
        this.roadNo = roadNo;   
        this.area = area;
        this.city = city;
        this.country = country;
    }
    
    Address(String houseName, String roadNo, PostOffice PO, String city, Country country) {
        this.houseName = houseName;
        this.roadNo = roadNo;   
        this.PO = PO;
        this.city = city;
        this.country = country;
    }
    
    public void getAddress() {
    
        if (this.area != "") {
            System.out.print ( "House name     : " + this.houseName +"\n"+
                               "Road no        : " + this.roadNo +"\n"+
                               "Area           : " + this.area+"\n"+
                               "City           : " + this.city+"\n");
            country.getCountry();
        }
        else {
            System.out.print ( "House name     : " + this.houseName +"\n"+
                               "Road no        : " + this.roadNo +"\n");
            PO.getPostOffice();
            System.out.print(  "City           : " + this.city+"\n");
            country.getCountry();
        }
    }

}
