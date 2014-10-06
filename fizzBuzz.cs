// https://www.codeeval.com/open_challenges/1/
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FizzBuzz
{
    class MainClass
    {
	    static public void FizzBuzz(int fizz, int buzz, int max)
	    {
            for (int i = 1; i <= max; i++)
            {
                if (i % fizz == 0 || i % buzz == 0)
                {
                    if (i % fizz == 0)
                        Console.Write("F");
                    if (i % buzz == 0)
                        Console.Write("B");
                }
                else
                    Console.Write(i);
                Console.Write(" ");
            }
		    return;
	    }

        static int Main(string[] args)
        {
		    StreamReader sr = new StreamReader(args[0]);
		    string line;
            while((line = sr.ReadLine()) != null)
		    {
			    string[] parameters = line.Split(new Char [] {' '});
                FizzBuzz(Int32.Parse(parameters[0]), Int32.Parse(parameters[1]), Int32.Parse(parameters[2]));
                Console.WriteLine("");
		    }

		    return 0;
        }
    }
}
