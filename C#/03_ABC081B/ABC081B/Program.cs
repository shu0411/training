using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC081B
{
    class Program
    {
        //黒板に N 個の正の整数 A1,...,ANが書かれています．
        //すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
        //黒板に書かれている整数すべてを，2 で割ったものに置き換える．
        //すぬけ君は最大で何回操作を行うことができるかを求めてください．
        //制約
        //1≤N≤200
        //1≤Ai≤10^9
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //N
        //A1 A2 ... AN
        //出力
        //すぬけ君は最大で何回操作を行うことができるかを出力せよ．

        //【線形探索】
        static void Main(string[] args)
        {
            //入力値取得
            string input1 = Console.ReadLine();
            string input2 = Console.ReadLine();
            string[] inputStrArray = input2.Split(' ');

            //計算処理
            int ansNum = -1; //出力値
            foreach (string checkStr in inputStrArray)
            {
                //2で割っていって何回割れるか
                int countDevide = 0;
                int checkNum = Convert.ToInt32(checkStr);
                while (checkNum % 2 == 0)
                {
                    checkNum = checkNum / 2;
                    countDevide++;
                }

                //割った回数が今の出力値より多かったら出力値を更新
                if(ansNum == -1)
                {
                    ansNum = countDevide;
                }
                else
                {
                    ansNum = (countDevide < ansNum) ? countDevide : ansNum;
                }

                //出力値の最小は0なので0になったら後続をスキップ
                if(ansNum == 0)
                {
                    break;
                }
            }

            //出力処理
            Console.WriteLine(ansNum.ToString());
        }
    }
}
