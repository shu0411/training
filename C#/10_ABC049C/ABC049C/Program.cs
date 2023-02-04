using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ABC049C
{
    class Program
    {
        //英小文字からなる文字列 S が与えられます。 
        //Tが空文字列である状態から始め、
        //以下の操作を好きな回数繰り返すことで S=T とすることができるか判定してください。
        //T の末尾に dream dreamer erase eraser のいずれかを追加する。
        //制約
        //1≦∣S∣≦10^5
        //S は英小文字からなる。
        //入力
        //入力は以下の形式で標準入力から与えられる。
        //S
        //出力
        //S=T とすることができる場合 YES を、そうでない場合 NO を出力せよ。
        static void Main(string[] args)
        {
            //入力
            string S = Console.ReadLine();

            //処理
            //Sの先頭からそれぞれの文字列が当てはまるかどうかチェック
            //チェックする文字列の長さが0になるまで続ける
            //当てはまったらその分を削って次へ
            //当てはまらなかった時点で結果をfalseとしてループを抜ける
            bool ret = true;
            string checkStr = S;

            while(ret && checkStr.Length > 0)
            {
                if(checkStr.Length < 5)
                {
                    //文字列の長さが5文字未満の場合、S=Tになることがないのでループを抜ける。
                    //※2周目以降を考慮し、ここでチェックする
                    ret = false;
                    break;
                }

                //文字列の先頭が該当文字列かどうかチェック
                //文字列の長さが0になるまでループを抜けなければ結果はtrue
                switch (checkStr.Substring(0,5))
                {
                    case "dream":
                        //文字列の先頭が"dream"の場合、"dreamer"の可能性もあるためそのチェック
                        if (checkStr.Length >= 7 && checkStr.Substring(5,2) == "er")
                        {
                            //文字列の先頭が"dreamer"の場合、
                            //"dream"のあとに"erase"が続く可能性があるためそのチェック
                            if (checkStr.Length >= 10 && checkStr.Substring(5, 5) == "erase")
                            {
                                //文字列の先頭が"dreamerase"の場合、チェックする文字列に6文字目以降を格納する
                                checkStr = checkStr.Substring(5);
                            }
                            else
                            {
                                //文字列の先頭が"dreamer"("dreamerase"ではない)の場合、チェックする文字列に8文字目以降を格納する
                                checkStr = checkStr.Substring(7);
                            }
                        }
                        else
                        {
                            //文字列の先頭が"dream"("dreamer"ではない)の場合、チェックする文字列に6文字目以降を格納する
                            checkStr = checkStr.Substring(5);
                        }
                        continue;
                    case "erase":
                        //文字列の先頭が"erase"の場合、"eraser"の可能性もあるためそのチェック
                        if (checkStr.Length >= 6 && checkStr.Substring(5, 1) == "r")
                        {
                            //文字列の先頭が"eraser"の場合、チェックする文字列に7文字目以降を格納する
                            checkStr = checkStr.Substring(6);
                        }
                        else
                        {
                            //文字列の先頭が"erase"("eraser"ではない)の場合、チェックする文字列に6文字目以降を格納する
                            checkStr = checkStr.Substring(5);
                        }
                        continue;
                    default:
                        //文字列の先頭が、追加できる文字列のどれでもない場合
                        //S=Tになることがないのでループを抜ける。
                        ret = false;
                        break;
                }
            }

            //出力
            if (ret)
            {
                Console.WriteLine("YES");
            }
            else
            {
                Console.WriteLine("NO");
            }
        }
    }
}
