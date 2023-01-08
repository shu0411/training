using System;

namespace PracticeA_2
{
    class Program
    {
        //高橋君はデータの加工が行いたいです。
        //整数 a,b,cと、文字列 s が与えられます。 a+b+c の計算結果と、文字列 s を並べて表示しなさい。
        //制約
        //1≤a,b,c≤1,000
        //1≤∣s∣≤100
        //入力
        //入力は以下の形式で与えられる。
        //a
        //b c
        //s
        //出力
        //a+b+c と s を空白区切りで 1 行に出力せよ。
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
            Console.WriteLine((a + b + c).ToString() + " " + s);
        }
    }
}
