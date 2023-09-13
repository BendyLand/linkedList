using System;

namespace LinkedList
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("C# Program:");
            
            LinkedList<string> list = new LinkedList<string>("Ben");

            list.InsertBeginning("Olivia");

            Console.WriteLine(list.Stringify());

            LinkedList<int> li = new LinkedList<int>();
            for (int i = 1; i < 10; i++)
            {
                li.InsertBeginning(i);
            }
 
            LinkedList<int>.SwapNodes(li, 9, 5);            

            Console.WriteLine(li.Stringify());
        }
    }
}