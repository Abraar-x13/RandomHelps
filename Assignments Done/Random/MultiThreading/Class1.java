
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
 
public class Class1 implements Runnable{
    
    int[] a1 = {1,2,3,4,5,6,7,8,9,10};
    int[] a2 = {10,9,8,7,6,5,4,3,2,1};
    int[] a12 = new int[10]; 
  
    @Override
    public void run() {
        for(int i = 0;i < 10;i++)
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
    }
  
}
