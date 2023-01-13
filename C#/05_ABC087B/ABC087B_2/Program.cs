using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC087B_2
{
    class Program
    {
        //【模範解答】
        static void Main(string[] args)
        {
            //入力
            int A = Convert.ToInt32(Console.ReadLine());
            int B = Convert.ToInt32(Console.ReadLine());
            int C = Convert.ToInt32(Console.ReadLine());
            int X = Convert.ToInt32(Console.ReadLine());

            //計算
            int sum = 0;
            int count = 0;

            //500円の判定
            for (int iA = 0; iA <= A; iA++)
            {
                for (int iB = 0; iB <= B; iB++)
                {
                    for (int iC = 0; iC <= C; iC++)
                    {
                        sum = 500 * iA + 100 * iB + 50 * iC;
                        if (sum == X)
                        {
                            //合計がちょうどXの場合だけ答えを1増やす
                            count++;
                        }
                    }
                }
            }

            //出力
            string ret = count.ToString();
            Console.WriteLine(ret);
        }
    }
}
