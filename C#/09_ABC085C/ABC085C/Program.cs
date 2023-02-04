using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC085C
{
    class Program
    {
        //日本でよく使われる紙幣は、10000 円札、5000 円札、1000 円札です。
        //以下、「お札」とはこれらのみを指します。
        //青橋くんが言うには、彼が祖父から受け取ったお年玉袋にはお札が N 枚入っていて、合計で Y 円だったそうですが、嘘かもしれません。
        //このような状況がありうるか判定し、ありうる場合はお年玉袋の中身の候補を一つ見つけてください。
        //なお、彼の祖父は十分裕福であり、お年玉袋は十分大きかったものとします。
        //制約
        //1≤N≤2000
        //1000≤Y≤2×10^7
        //N は整数である。
        //Y は 1000 の倍数である。
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //N Y
        //出力
        //N 枚のお札の合計金額が Y 円となることがありえない場合は、-1 -1 -1 と出力せよ。
        //N 枚のお札の合計金額が Y 円となることがありうる場合は、
        //そのような N 枚のお札の組み合わせの一例を「10000 円札 x 枚、5000 円札 y 枚、1000 円札 z 枚」として、
        //x、y、z を空白で区切って出力せよ。複数の可能性が考えられるときは、そのうちどれを出力してもよい。
        static void Main(string[] args)
        {
            //入力
            string inputStr = Console.ReadLine();
            string[] inputStrArray = inputStr.Split();
            int N = Convert.ToInt32(inputStrArray[0]);
            int Y = Convert.ToInt32(inputStrArray[1]);

            //処理
            int outX = -1;
            int outY = -1;
            int outZ = -1;
            int checkZ = 0;
            int sum = 0;

            for(int checkX = 0; checkX <= N; checkX++)
            {
                for(int checkY = 0; checkY <= N - checkX; checkY++)
                {
                    checkZ = N - checkX - checkY;
                    sum = 10000 * checkX + 5000 * checkY + 1000 * checkZ;
                    if(sum == Y)
                    {
                        outX = checkX;
                        outY = checkY;
                        outZ = checkZ;
                        break;
                    }
                }
            }

            //出力
            string outStr = outX.ToString() + " " + outY.ToString() + " " + outZ.ToString();
            Console.WriteLine(outStr);
        }
    }
}
