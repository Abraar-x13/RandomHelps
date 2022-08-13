using System;

namespace HelloWorld
{
    public class MainClass
    {
        public static void Main(string[] args)
        {
            Message myMassage = new Message("Hello World - from Message Object");
            myMassage.Print();

            Console.WriteLine("Enter your name : ");
            string name = Console.ReadLine();

            if (!string.IsNullOrEmpty(name))
            {
                _ = new NameTest(name);
            }

            Console.ReadLine();

        }
    }
}
