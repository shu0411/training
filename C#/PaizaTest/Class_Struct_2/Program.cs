using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Class_Struct_2
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
            string K = Console.ReadLine();

            //出力
            foreach (string[] student in studentList)
            {
                //年齢(2つ目要素)とKを比較
                if(student[1] == K)
                {
                    Console.WriteLine(student[0]);
                }
            }
        }
    }
}
