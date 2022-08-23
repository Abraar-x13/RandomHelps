using NUnit.Framework;

namespace Iteration1
{
    [TestFixture]
    public class Tests
    {
        [Test]
        public void TestAreYou()
        {
            IdentifiableObject id = new IdentifiableObject(new string[] { "fred", "bob" });
            Assert.IsTrue(id.AreYou("fred"));
            Assert.IsTrue(id.AreYou("bob"));
        }

        [Test]
        public void TestNotAreYou()
        {
            IdentifiableObject id = new IdentifiableObject(new string[] { "fred", "bob" });
            Assert.IsFalse(id.AreYou("ben"));
            Assert.IsFalse(id.AreYou("kai"));
        }

        [Test]
        public void TestCaseSensitive()
        {
            IdentifiableObject id = new IdentifiableObject(new string[] { "fred", "bob" });
            Assert.IsTrue(id.AreYou("FRED"));
            Assert.IsTrue(id.AreYou("BOB"));
        }

        [Test]
        public void TestFirstID()
        {
            IdentifiableObject id = new IdentifiableObject(new string[] { "fred", "bob" });
            Assert.IsTrue(id.FirstId == "fred");
        }
        
        [Test]
        public void TestFirstIDWithNoID()
        {
            IdentifiableObject id = new IdentifiableObject(new string[] { });
            Assert.IsTrue(id.FirstId == " ");
        }

        [Test]
        public void TestAddID()
        {
            IdentifiableObject id = new IdentifiableObject(new string[] { "fred", "bob" });

            id.AddIdentifier("wilma");
            IdentifiableObject unitTests;
            Assert.IsTrue (id.AreYou("fred"));
            Assert.IsTrue(id.AreYou("bob"));
            Assert.IsTrue(id.AreYou("wilma"));
        }
    }
}