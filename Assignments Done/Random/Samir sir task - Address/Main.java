package com.codekat.project1;

// ctrl+shift+F - format code. alt in win.
import java.util.HashMap;
import java.util.Scanner;

public class Main {

    public static void main(String args[]) {

        HashMap<String, Country> countries = new HashMap<>();
        countries = initiateCountries();
        
        HashMap<String, PostOffice> POs = new HashMap<>();
        POs = initiatePostOffices();
        

        Address pannaAddress = new Address( "Panna Kutir", 
                                            "MC College Rd", "Tamabil", 
                                            "Sylhet", 
                                            countries.get("Bangladesh"));
        Address shantoAddress = new Address( "Shantor Matir Ghor", 
                                             "Sunnyvale", 
                                             "Sillicon Valley", 
                                             "California", 
                                             countries.get("USA"));
        
        Recipient panna = new Recipient( "Panna Das Aryan", 
                                         "0142069420", 
                                         "panna@gmail.com", 
                                          pannaAddress);
        Recipient shanto = new Recipient( "Ariful Islam Shanto", 
                                          "99999999", 
                                          "ami_shanto_na@gmail.com", 
                                          shantoAddress);
        
        panna.getRecipient();
        shanto.getRecipient();
        
        Address ifazAddress = new Address( "Ifaz Rajproshad", 
                                           "Lalbagh", 
                                           POs.get("New Market Post Office"), 
                                           "Dhaka", 
                                           countries.get("Bangladesh"));
        

        Recipient ifaz = new Recipient( "Sheikh Ifaz Aiman", 
                                        "12345678", 
                                        "ifaz31@gmail.com", 
                                        ifazAddress);
        ifaz.getRecipient();


//        // Input from user version : 
//        Scanner sc = new Scanner(System.in);
//        System.out.println("Taking Recipient Details..........");
//        System.out.println("Enter Recipient Name :");
//        String name = sc.nextLine();
//        System.out.println("Enter Contact Number :");
//        String number = sc.nextLine();
//        System.out.println("Enter Email :");
//        String email = sc.nextLine();
//        System.out.println("Now, Taking Adresss Details.......");
//        System.out.println("Enter House Name :");
//        String houseName = sc.nextLine();
//        System.out.println("Enter Road No. :");
//        String roadNo = sc.nextLine();
//        System.out.println("Enter Area :");
//        String area = sc.nextLine();
//        System.out.println("Enter City :");
//        String city = sc.nextLine();
//        System.out.println("Enter Country :");
//        String countryName = sc.nextLine();
//        
//        Address userAddress = new Address( houseName, roadNo, area, 
//                                           city, countries.get(countryName));
//
//        Recipient user = new Recipient(name, number, email, userAddress);
//        System.out.println("\n\n");
//        user.getRecipient();
        
    }
        
    private static HashMap<String, Country> initiateCountries() {
        
        HashMap<String, Country> countries = new HashMap<>();
        Country country;
        
        country = new Country("Bangladesh", "+880", "Asia");
        countries.put("Bangladesh", country);
        
        country = new Country("India", "+091", "Asia");
        countries.put("India", country);
        
        country = new Country("Myanmar", "+123", "Asia");
        countries.put("Myanmar", country);
        
        country = new Country("USA", "+001", "North America");
        countries.put("USA", country);
        
        country = new Country("Germany", "+666", "Europe");
        countries.put("Germany", country);
        
        country = new Country("Russia", "+999", "Russia");
        countries.put("Russia", country);
        
        return countries;
    }

    private static HashMap<String, PostOffice> initiatePostOffices() {
        HashMap<String, PostOffice> POs = new HashMap<>();
        PostOffice PO;
        
        PO = new PostOffice("Sylhet Head Post Office", "Tamabil", "1111");
        POs.put("Sylhet Head Post Office", PO);
        
        PO = new PostOffice("New Market Post Office", "New Market", "1205");
        POs.put("New Market Post Office", PO);
        
        PO = new PostOffice("Sub-Post office, SUST", "Akhalia", "2222");
        POs.put("Sub-Post office, SUST", PO);
        
        PO = new PostOffice("Putin bhai er post office", "Moscow", "9999");
        POs.put("Sub-Post office, SUST", PO);      
        
        return POs;
    }
}
