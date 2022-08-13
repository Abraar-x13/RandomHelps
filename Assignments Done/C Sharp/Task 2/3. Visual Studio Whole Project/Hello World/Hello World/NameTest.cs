using System.Xml.Linq;
namespace HelloWorld
{
    internal class NameTest
    {
        string _name;
        Message m;
        public NameTest(string name)
        {
            _name = name;
            Greet();
        }
        public void Greet ()
        {
            bool areEqual = String.Equals(_name, "Meem", StringComparison.OrdinalIgnoreCase);
            if (areEqual)
            {
                m = new Message("Welcome Back"); m.Print(); return;
            }
            areEqual = String.Equals(_name, "Abraar", StringComparison.OrdinalIgnoreCase);
            if (areEqual)
            {
                m = new Message("What a lovely name"); m.Print(); return;
            }
            areEqual = String.Equals(_name, "Ian", StringComparison.OrdinalIgnoreCase);
            if (areEqual)
            {
                m = new Message("Great name"); m.Print(); return;
            }
            areEqual = String.Equals(_name, "Shanto", StringComparison.OrdinalIgnoreCase);
            if (areEqual)
            {
                m = new Message("Oh hi!"); m.Print(); return;
            }
            areEqual = String.Equals(_name, "Gomez", StringComparison.OrdinalIgnoreCase);
            if (areEqual)
            {
                m = new Message("Beautiful Name!"); m.Print(); return;
            }

            m = new Message("That is a silly name");
            m.Print();
            return;
        }
    }
}