using System;

namespace LinkedList
{
    class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("C# Program:");
            
            LinkedList<string> list = new LinkedList<string>("Ben");
            // Console.WriteLine(list.HeadNode.Value);

            list.InsertBeginning("Olivia");
            // Console.WriteLine(list.HeadNode.Value);

            // Prints Olivia; Ben;
            Console.WriteLine(list.Stringify());

            LinkedList<int> li = new LinkedList<int>();
            for (int i = 1; i < 10; i++)
            {
                li.InsertBeginning(i);
            }
            // Console.WriteLine(li.Stringify());
            LinkedList<int>.SwapNodes(li, 9, 5);            
            // Prints 5; 8; 7; 6; 9; 4; 3; 2; 1; 0; 
            Console.WriteLine(li.Stringify());
        }
    }
}