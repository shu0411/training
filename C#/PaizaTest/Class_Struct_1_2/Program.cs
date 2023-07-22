using System;

namespace Class_Struct_1_2
{
    class Program
    {
        static void Main(string[] args)
        {
            //入力
            int N = Convert.ToInt32(Console.ReadLine());
            string[] inputList = new string[4];
            for (int i = 0; i < N; i++)
            {
                //入力
                inputList = new string[4];
                inputList = Console.ReadLine().Split(' ');

                //出力
                Console.WriteLine("User{");
                Console.WriteLine("nickname : " + inputList[0]);
                Console.WriteLine("old : " + inputList[1]);
                Console.WriteLine("birth : " + inputList[2]);
                Console.WriteLine("state : " + inputList[3]);
                Console.WriteLine("}");
            }
        }
    }
}
