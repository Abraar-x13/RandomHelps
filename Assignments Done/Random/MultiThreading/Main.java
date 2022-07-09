/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.Scanner;
public class Main {
            
    public static void main(String[] args) {
        
        int[] a1 = {1,2,3,4,5,6,7,8,9,10};
        int[] a2 = {10,9,8,7,6,5,4,3,2,1};
        int[] a12 = new int[10];
        int[] result = new int[10];
        int total=0;
        
        Class1 t1 = new Class1();
        Thread t = new Thread(t1);
        t.start();
        
        for(int i = 0; i < 10;i++)
        {
            a12[i] = a1[i]+a2[i];
            try
            {
                Thread.sleep(100);
            }
            catch (Exception e) 
            { 
                System.out.println ("Exception found"); 
            } 
        }
         try
        {
            t.join();
        }
        catch (Exception e) 
        { 
            System.out.println ("Exception found"); 
        }
        System.out.println(" The sum of the four arrays are : ");
        for(int i =0; i < 10;i++)
        {
            result[i] = a12[i]+t1.a12[i];
            total += result[i];
            System.out.print("\t" + result[i]);
        }
        
    }
}
