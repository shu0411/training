using System;
using System.Collections.Generic;

namespace Class_Struct_4
{
    class Program
    {
        static void Main(string[] args)
        {
            //入力
            string[] NK = Console.ReadLine().Split(' ');
            int N = Convert.ToInt32(NK[0]);
            int K = Convert.ToInt32(NK[1]);

            List<string[]> studentList = new List<string[]>();
            string[] inputArray = new string[4];
            for (int i = 0; i < N; i++)
            {
                inputArray = new string[4];
                inputArray = Console.ReadLine().Split(' ');
                studentList.Add(inputArray);
            }

            //変換行の入力と処理
            string[] changeArray = new string[4];
            int changeLine = -1;
            string changedName = string.Empty;
            for (int i = 0; i < K; i++)
            {
                changeArray = new string[4];
                changeArray = Console.ReadLine().Split(' ');
                changeLine = Convert.ToInt32(changeArray[0]) - 1;
                changedName = changeArray[1];
                studentList[changeLine][0] = changedName;
            }

            //出力
            foreach (string[] student in studentList)
            {
                Console.WriteLine(student[0] + " " + student[1] + " " + student[2] + " " + student[3]);
            }
        }
    }
}
