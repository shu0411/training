using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC088B
{
    class Program
    {
        //N 枚のカードがあります. 
        //i 枚目のカードには, a i  という数が書かれています.
        //Alice と Bob は, これらのカードを使ってゲームを行います. 
        //ゲームでは, Alice と Bob が交互に 1 枚ずつカードを取っていきます. 
        //Alice が先にカードを取ります.
        //2 人がすべてのカードを取ったときゲームは終了し, 取ったカードの数の合計がその人の得点になります. 
        //2 人とも自分の得点を最大化するように最適な戦略を取った時, Alice は Bob より何点多く取るか求めてください.
        //制約
        //N は 1 以上 100 以下の整数
        //a i​  (1≤i≤N) は 1 以上 100 以下の整数
        //入力
        //入力は以下の形式で標準入力から与えられる.
        //N
        //a1​ a2​ a3 ... aN
        //出力
        //両者が最適な戦略を取った時, Alice は Bob より何点多く取るかを出力してください.
        static void Main(string[] args)
        {
            //入力
            string inputStr1 = Console.ReadLine();
            int arraySize = Convert.ToInt32(inputStr1);
            string inputStr2 = Console.ReadLine();
            string[] inputStrArray = inputStr2.Split(' ');
            int[] inputIntArray = Array.ConvertAll(inputStrArray, Convert.ToInt32);

            //計算
            //並べ替え
            Array.Sort(inputIntArray);
            Array.Reverse(inputIntArray);

            //合計計算
            int pointAlice = 0;
            int pointBob = 0;
            for (int i = 0; i < arraySize; i++)
            {
                if(i % 2 == 0)
                {
                    pointAlice += inputIntArray[i];
                }
                else
                {
                    pointBob += inputIntArray[i];
                }
            }

            //点差を計算
            int ans = pointAlice - pointBob;

            //出力
            Console.WriteLine(ans.ToString());
        }
    }
}
