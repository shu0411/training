using System;
using System.Collections.Generic;

namespace PaizaTest
{
    class Program
    {
        public class Profile
        {
            public string Nickname { get; set; }
            public string Old { get; set; }
            public string Birth { get; set; }
            public string State { get; set; }
            public void WriteLine()
            {
                Console.WriteLine("User{");
                Console.WriteLine("nickname : " + Nickname);
                Console.WriteLine("old : " + Old);
                Console.WriteLine("birth : " + Birth);
                Console.WriteLine("state : " + State);
                Console.WriteLine("}");
            }
        }

        static void Main(string[] args)
        {
            int N = Convert.ToInt32(Console.ReadLine());
            //List<List<string>> inputTable = new List<List<string>>();
            //List<string> inputList = new List<string>();
            List<Profile> inputTable = new List<Profile>();
            string[] inputList = new string[4];
            Profile inputProfile = new Profile();
            for (int i = 0; i < N; i++)
            {
                inputList = new string[4];
                inputProfile = new Profile();
                inputList = Console.ReadLine().Split(' ');
                inputProfile.Nickname = inputList[0];
                inputProfile.Old = inputList[1];
                inputProfile.Birth = inputList[2];
                inputProfile.State = inputList[3];
                inputTable.Add(inputProfile);
            }

            foreach(Profile outProfile in inputTable)
            {
                outProfile.WriteLine();
            }
        }
    }
}
