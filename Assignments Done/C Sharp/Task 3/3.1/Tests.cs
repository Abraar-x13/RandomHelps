using System;
using NUnit.Framework;

namespace TestProject1
{
    [TestFixture]
    public class Tests
    {
        [Test]
        public void Test1()
        {
            Clock c = new Clock();
            c.Tick();
            Assert.AreEqual("00:00:01", c.CurrentTime());
        }
        
        [Test]
        public void Test2()
        {
            Clock c = new Clock();
            for (int i = 0; i < 65; i++)
            {
                // Passing 1 Minute and 5 Seconds.
                c.Tick();
            }
            Assert.AreEqual("00:01:05", c.CurrentTime());
        }
        
        [Test]
        public void Test3()
        {
            Clock c = new Clock();
            for (int i = 0; i < 62*60; i++)
            {
                // Passing 1 hour and 2 minutes.
                c.Tick();
            }
            Assert.AreEqual("01:02:00", c.CurrentTime());
        }
        
        [Test]
        public void Test4()
        {
            Clock c = new Clock();
            for (int i = 0; i < 4*60*60 + 1; i++)
            {
                // Passing 4 hours and 1 second.
                c.Tick();
            }
            Assert.AreEqual("04:00:01", c.CurrentTime());
        }
        
        [Test]
        public void Test5()
        {
            Clock c = new Clock();
            c.Hours = 7;
            Assert.AreEqual("07:00:00", c.CurrentTime());
        }
        
        [Test]
        public void Test6()
        {
            Clock c = new Clock();
            c.Minutes = 45;
            Assert.AreEqual("00:45:00", c.CurrentTime());
        }
        
        [Test]
        public void Test7()
        {
            Clock c = new Clock();
            c.Seconds = 21;
            Assert.AreEqual("00:00:21", c.CurrentTime());
        }
        
        [Test]
        public void Test8()
        {
            Clock c = new Clock();
            c.Hours = 7;
            c.Minutes = 30;
            c.Seconds = 3;
            Assert.AreEqual("07:30:03", c.CurrentTime());
        }
    }
}