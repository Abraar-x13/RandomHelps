using System.Collections.Generic;
using System.Linq;

namespace Iteration1
{
    public class IdentifiableObject
    {
        private readonly List<string> _identifiers;

        public IdentifiableObject(string[] idents)
        {
            _identifiers = new List<string>();
            foreach (var id in idents) _identifiers.Add(id.ToLower());
        }
        
        public bool AreYou(string id)
        {
            return _identifiers.Any(i => id.ToLower() == i);
        }
        public string FirstId => _identifiers.Count == 0 ? " " : _identifiers[0];

        public void AddIdentifier(string id)
        {
            _identifiers.Add(id.ToLower());
        }
    }
}