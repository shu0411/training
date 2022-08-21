using System;

namespace ABC086A
{
    class ABC086A
    {
        static void Main(string[] args)
        {
            string[] s = Console.ReadLine().Split(" ",2);
            int a = int.Parse(s[0]);
            int b = int.Parse(s[1]);
            int ans = a * b;

            string ret;
            if( ans % 2 == 1 ){
                ret = "Odd";
            }
            else{
                ret = "Even";
            }
            Console.WriteLine(ret);
        }
    }

}