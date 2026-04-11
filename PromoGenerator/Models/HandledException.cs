using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

[Serializable]
public class HandledException : Exception
{
    public HandledException()
    { }

    public HandledException(string message)
        : base(message)
    { }

    public HandledException(string message, Exception innerException)
        : base(message, innerException)
    { }
}
