using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC081B_2
{
    class Program
    {
        //【全探索】
        static void Main(string[] args)
        {
            //入力値取得
            string input1 = Console.ReadLine();
            int arraySize = Convert.ToInt32(input1);
            string input2 = Console.ReadLine();
            string[] inputStrArray = input2.Split(' ');
            int[] inputIntArray = Array.ConvertAll(inputStrArray, int.Parse);

            //計算処理
            int ansNum = 0; //出力値
            bool isExistsOdd = false;
            while (true)
            {
                isExistsOdd = false;

                //すべての項目が偶数か確認
                foreach (int checkNum in inputIntArray)
                {
                    if (checkNum % 2 == 1)
                    {
                        isExistsOdd = true;
                    }
                }

                //1件でも奇数があればbreak
                if (isExistsOdd)
                {
                    break;
                }

                //すべて偶数の場合
                //全項目を2で割る
                inputIntArray = Array.ConvertAll(inputIntArray, i => i / 2);

                //答えを＋１
                ansNum++;
            }

            //出力処理
            Console.WriteLine(ansNum.ToString());
        }
    }
}
