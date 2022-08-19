using System;

namespace ConsoleApplication1
{
    internal class Program
    {
        private static void PrintCounters(Counter[] counters)
        {
            foreach (Counter c in counters)
            {
                string name = c.Name;
                int ticks = c.Ticks;
                String s = String.Format("{0} is {1}", name, ticks);
                Console.WriteLine(s);
            }
            Console.WriteLine();
        }
        
        public static void Main(string[] args)
        {
            Counter[] myCounters = new Counter[3];

            myCounters[0] = new Counter("Counter 1");
            myCounters[1] = new Counter("Counter 2");
            myCounters[2] = myCounters[0];

            for (int i = 0; i <= 9; i++)
            {
                myCounters[0].Increment();
            }
        
            for (int i = 0; i <= 14; i++)
            {
                myCounters[1].Increment();
            }

            PrintCounters(myCounters);
            myCounters[2].Reset();
            PrintCounters(myCounters);
        }
    }
}