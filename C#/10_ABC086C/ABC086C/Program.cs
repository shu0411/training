using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC086C
{
    class Program
    {
        //シカのAtCoDeerくんは二次元平面上で旅行をしようとしています。
        //AtCoDeerくんの旅行プランでは、時刻 0 に 点 (0,0) を出発し、
        //1 以上 N 以下の各 i に対し、時刻 t i​に 点 (x i​ ,y i ) を訪れる予定です。
        //AtCoDeerくんが時刻 t に 点 (x,y) にいる時、 時刻 t+1 には 点 (x+1,y), (x−1,y), (x,y+1), (x,y−1) のうちいずれかに存在することができます。
        //その場にとどまることは出来ないことに注意してください。 AtCoDeerくんの旅行プランが実行可能かどうか判定してください。
        //制約
        //1 ≤ N ≤ 10^5
        //0 ≤ x i​≤ 10^5
        //0 ≤ y i​≤ 10^5
        //1 ≤ t i​≤ 10^5
        //t i < t i+1 (1 ≤ i ≤ N−1)
        //入力は全て整数
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //N
        //t 1 x 1 ​y 1
        //t 2 ​x 2 ​y 2
        //:
        //t N​ x N ​y N
        //出力
        //旅行プランが実行可能ならYesを、不可能ならNoを出力してください。
        static void Main(string[] args)
        {
            //入力
            string N = Console.ReadLine();
            int lineCount = Convert.ToInt32(N);
            string[] inputStrAll = new string[lineCount];
            for(int i = 0; i < lineCount; i++)
            {
                inputStrAll[i] = Console.ReadLine();
            }

            //処理
            bool ret = true;
            int beforeT = 0;
            int beforeX = 0;
            int beforeY = 0;
            string[] inputStrColumns;
            int inputT = 0;
            int inputX = 0;
            int inputY = 0;
            int dist = 0;   //前の点からの移動距離を取得
            foreach (string inputStrLine in inputStrAll)
            {
                //入力文字列の行の数字を取得
                inputStrColumns = inputStrLine.Split(' ');
                inputT = Convert.ToInt32(inputStrColumns[0]);
                inputX = Convert.ToInt32(inputStrColumns[1]);
                inputY = Convert.ToInt32(inputStrColumns[2]);

                //距離計算
                dist = Math.Abs(inputX - beforeX) + Math.Abs(inputY - beforeY);

                //距離と移動回数の大小関係
                if (dist > inputT - beforeT)
                {
                    //距離が移動回数より多かったら移動不可なのでfalseを返して処理終了
                    ret = false;
                    break;
                }

                //距離と移動回数の偶奇関係
                //1回の移動でX方向かY方向の値が必ず変わるので、
                //距離の偶奇と移動回数の偶奇は一致する必要がある。
                if()
                {
                    //距離と移動回数の偶奇が一致しない場合移動不可なのでfalseを返して処理終了
                    ret = false;
                    break;
                }
            }

            //出力
            if (ret)
            {
                Console.WriteLine("Yes");
            }
            else
            {
                Console.WriteLine("No");
            }
        }
    }
}
