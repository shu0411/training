using System;
using System.Collections.Generic;

namespace Class_Struct_5
{
    class Program
    {
        public class Employee
        {
            public int Id { get; set; }
            public string Number { get; set; }
            public string Name { get; set; }
        }
        static void Main(string[] args)
        {
            //入力(1行目)
            int N = Convert.ToInt32(Console.ReadLine());

            //入力(2行目～)
            List<Employee> employeeTable = new List<Employee>();
            string inputStr;    //命令を受け取る用
            string[] inputList; //make用
            Employee inputEmployee; //make用
            int getId;  //EmployeeTableからgetするためのID
            for (int i = 0; i < N; i++)
            {
                inputStr = Console.ReadLine();

                switch (inputStr.Substring(0, 5))
                {
                    case "make ":
                        inputList = new string[3];
                        inputList = inputStr.Split(' ');
                        inputEmployee = new Employee();
                        inputEmployee.Number = inputList[1];
                        inputEmployee.Name = inputList[2];
                        employeeTable.Add(inputEmployee);
                        break;
                    case "getnu":
                        getId = Convert.ToInt32(inputStr.Substring(7)) - 1;
                        Console.WriteLine(employeeTable[getId].Number);
                        break;
                    case "getna":
                        getId = Convert.ToInt32(inputStr.Substring(8)) - 1;
                        Console.WriteLine(employeeTable[getId].Name);
                        break;
                }
            }
        }
    }
}
