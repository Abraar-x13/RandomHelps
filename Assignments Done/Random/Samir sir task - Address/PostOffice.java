
package com.codekat.project1;


public class PostOffice {
    String POname = "";
    String areaName = "";
    String zipCode = "";
    String contactNumber = "";
    String officerInCharge = "";
    
    PostOffice(String POname, String areaName, String zipCode, String contactNumber, String officerInCharge) {
        this.POname = POname;
        this.areaName = areaName;
        this.zipCode = zipCode;
        this.contactNumber = contactNumber;
        this.officerInCharge = officerInCharge;
    }
    
    PostOffice(String POname,String areaName, String zipCode) {
        this.POname = POname;
        this.areaName = areaName;
        this.zipCode = zipCode;
    }

    void getPostOffice() {
        if ("".equals(contactNumber)) {
            System.out.println("Post Office    : " + this.POname + "\n" +
                               "Area           : " + this.areaName + "\n" +
                               "Zip Code       : " + this.zipCode);
        }
        else {
            System.out.println("Post Office    : " + this.POname + "\n" +
                               "Area           : " + this.areaName + "\n" +
                               "Zip Code       : " + this.zipCode + "\n" +
                               "PO contact     : " + this.contactNumber + "\n" +
                               "Off In Charge  : " + this.officerInCharge + "\n");
        }
    }
    
}
