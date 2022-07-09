
package com.codekat.project1;

public class Country {
    
    String countryName = "";
    String countryCode = "";
    String continent = "";
    
    Country (String countryName, String countryCode, String continent) {
        this.countryName = countryName;
        this.countryCode = countryCode;
        this.continent = continent;
    }
    
    public void getCountry() {    
        System.out.println( "Country        : " + this.countryName + "\n" +
                            "Country Code   : " + this.countryCode + "\n" + 
                            "Continent      : " + this.continent+"\n\n" );
    }
    
}
