using System;
using System.Collections.Generic;

namespace Class_Struct_3
{
    class Program
    {
        static void Main(string[] args)
        {
            //入力
            int N = Convert.ToInt32(Console.ReadLine());
            List<string[]> studentList = new List<string[]>();
            string[] inputArray = new string[4];
            for (int i = 0; i < N; i++)
            {
                inputArray = new string[4];
                inputArray = Console.ReadLine().Split(' ');
                studentList.Add(inputArray);
            }

            //ソート処理
            studentList.Sort((a, b) => a[1].CompareTo(b[1]));

            //出力
            foreach (string[] student in studentList)
            {
                Console.WriteLine(student[0] + " " + student[1] + " " + student[2] + " " + student[3]);
            }
        }
    }
}
