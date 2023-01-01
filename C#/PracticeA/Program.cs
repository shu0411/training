using System;

namespace PracticeA
{
    class Program
    {
        static void Main(string[] args)
        {
            //1行目
            int a = int.Parse(Console.ReadLine());
            //2行目
            string bcs = Console.ReadLine();
            string[] bc = bcs.Split(" ", 2);
            int b = int.Parse(bc[0]);
            int c = int.Parse(bc[1]);
            //3行目
            string s = Console.ReadLine();

            //出力
            Console.WriteLine((a+b+c).ToString() + " " + s);
        }
    }
}
