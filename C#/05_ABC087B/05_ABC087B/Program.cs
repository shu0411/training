using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _05_ABC087B
{
    class Program
    {
        //あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。
        //これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
        //同じ種類の硬貨どうしは区別できません。
        //2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。
        //制約
        //0≤A,B,C≤50
        //A+B+C≥1
        //50≤X≤20,000
        //A,B,C は整数である
        //X は 50 の倍数である
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //A
        //B
        //C
        //X
        //出力
        //硬貨を選ぶ方法の個数を出力せよ。
        static void Main(string[] args)
        {
            //入力
            int A = Convert.ToInt32(Console.ReadLine());
            int B = Convert.ToInt32(Console.ReadLine());
            int C = Convert.ToInt32(Console.ReadLine());
            int X = Convert.ToInt32(Console.ReadLine());

            //計算
            int sumA = 0;
            int sumB = 0;
            int sumC = 0;
            int count = 0;

            //500円の判定
            for(int iA = 0; iA <= A; iA++)
            {
                sumA = 500 * iA;
                
                if (sumA < X) 
                {
                    //合計がX未満なら100円の判定へ
                    for (int iB = 0; iB <= B; iB++)
                    {
                        sumB = sumA + 100 * iB;

                        if (sumB < X)
                        {
                            //合計がX未満なら50円の判定へ
                            for (int iC = 0; iC <= C; iC++)
                            {
                                sumC = sumB + 50 * iC;

                                if (sumC == X)
                                {
                                    //合計がちょうどXの場合だけ答えを1増やす
                                    count++;
                                }
                            }
                        }
                        else if (sumB == X)  
                        {
                            //合計がちょうどXなら答えを1増やす
                            count++;
                        }
                    }
                }
                else if (sumA == X)
                {
                    //合計がちょうどXなら答えを1増やす
                    count++;
                }
            }

            //出力
            string ret = count.ToString();
            Console.WriteLine(ret);
        }
    }
}
