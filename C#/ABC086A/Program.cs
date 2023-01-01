using System;

namespace ABC086A
{
    class ABC086A
    {
        //シカのAtCoDeerくんは二つの正整数 a,b を見つけました。 
        //a と b の積が偶数か奇数か判定してください。
        //制約
        //1 ≤ a,b ≤ 10000
        //a,b は整数
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //s1s2s3 
        //出力
        //答えを出力せよ。
        static void Main(string[] args)
        {
            //入力値取得
            string[] s = Console.ReadLine().Split(" ",2);
            int a = int.Parse(s[0]);
            int b = int.Parse(s[1]);

            //計算
            int ans = a * b;

            //出力値判定
            string ret;
            if( ans % 2 == 1 ){
                ret = "Odd";
            }
            else{
                ret = "Even";
            }

            //出力
            Console.WriteLine(ret);
        }
    }

}