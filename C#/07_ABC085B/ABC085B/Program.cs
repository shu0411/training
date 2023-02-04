using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC085B
{
    class Program
    {
        //X 段重ねの鏡餅 (X≥1) とは、X 枚の円形の餅を縦に積み重ねたものであって、
        //どの餅もその真下の餅より直径が小さい（一番下の餅を除く）もののことです。
        //例えば、直径 10、8、6 センチメートルの餅をこの順に下から積み重ねると 3 段重ねの鏡餅になり、
        //餅を一枚だけ置くと 1 段重ねの鏡餅になります。
        //ダックスフンドのルンルンは N 枚の円形の餅を持っていて、そのうち i 枚目の餅の直径は d i​センチメートルです。
        //これらの餅のうち一部または全部を使って鏡餅を作るとき、最大で何段重ねの鏡餅を作ることができるでしょうか。
        //制約
        //1≤N≤100
        //1≤d i≤100
        //入力値はすべて整数である。
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //N
        //d 1
        //:
        //d N
        //出力
        //作ることのできる鏡餅の最大の段数を出力せよ。
        static void Main(string[] args)
        {
            //入力
            string inputStr1 = Console.ReadLine();
            int arraySize = Convert.ToInt32(inputStr1);

            string[] inputStrArray = new string[arraySize];
            for(int i = 0; i < arraySize; i++)
            {
                inputStrArray[i] = Console.ReadLine();
            }

            //処理
            //並べ替え
            int[] inputIntArray = Array.ConvertAll(inputStrArray, Convert.ToInt32);
            Array.Sort(inputIntArray);
            Array.Reverse(inputIntArray);

            //段数確認
            int beforeNum = 101;  //前回の値格納用
            int count = 0;      //カウント用

            foreach (int targetNum in inputIntArray)
            {
                if(beforeNum > targetNum)
                {
                    count++;
                }
                beforeNum = targetNum;
            }

            //出力
            Console.WriteLine(count.ToString());
        }
    }
}
