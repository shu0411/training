using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC083B
{
    class Program
    {
        //1 以上 N 以下の整数のうち、
        //10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。
        //制約
        //・1≤N≤10^4
        //・1≤A≤B≤36
        //・入力はすべて整数である
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //N A B
        //出力
        //1 以上 N 以下の整数のうち、
        //10 進法での各桁の和が A 以上 B 以下であるものの総和を出力せよ。
        static void Main(string[] args)
        {
            //入力
            string inputStr = Console.ReadLine();
            string[] inputStrArray = inputStr.Split(' ');
            int N = Convert.ToInt32(inputStrArray[0]);
            int A = Convert.ToInt32(inputStrArray[1]);
            int B = Convert.ToInt32(inputStrArray[2]);

            //処理
            int ans = 0;
            //1～Nまでのループ
            for(int i = 1; i <= N; i++)
            {
                //1の位～10000の位までの5桁の値を足す
                int sumDigit =
                            i / 10000               //10000の位の値
                            + (i % 10000) / 1000    //1000の位の値
                            + (i % 1000) / 100      //100の位の値
                            + (i % 100) / 10        //10の位の値
                            + (i % 10);             //1の位の値

                //その総和がA以上B以下だったら答えに加算する
                if (sumDigit >= A && sumDigit <= B)
                {
                    ans += i;
                }

            }

            //出力
            Console.WriteLine(ans.ToString());
        }
    }
}
