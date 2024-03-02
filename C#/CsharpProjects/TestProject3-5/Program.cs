Console.WriteLine("Enter an integer value between 5 and 10");
int value = 0;
while(true)
{
    try
    {
        value = int.Parse(Console.ReadLine());
    }
    catch (FormatException)
    {
        Console.WriteLine("Sorry, you entered an invalid number, please try again");
        continue;
    }

    if (value < 5 || value > 10)
    {
        Console.WriteLine($"You entered {value}. Please enter a number between 5 and 10.");
        continue;
    }
    else
    {
        break;
    }
}


Console.WriteLine("Enter your role name (Administrator, Manager, or User)");
string input;
while (true)
{
    input = Console.ReadLine().Trim();
    if (input.ToLower().Equals("administrator") || input.ToLower().Equals("manager") || input.ToLower().Equals("user"))
    {
        Console.WriteLine($"Your input value ({input}) has been accepted.");
        break;
    }
    else
    {
        Console.WriteLine($"The role name that you entered, \"{input}\" is not valid. Enter your role name (Administrator, Manager, or User)");
    }

}

string[] myStrings = new string[2] { "I like pizza. I like roast chicken. I like salad", "I like all three of the menu choices" };
string tempString = "";
int periodLocation;
foreach (string myString in myStrings)
{
    tempString = myString;
    while(true)
    {
        periodLocation = tempString.IndexOf(".");
        if (periodLocation > 0)
        {
            Console.WriteLine(tempString.Substring(0, periodLocation));
            tempString = tempString.Remove(0,periodLocation + 1).TrimStart();
        }
        else
        {
            Console.WriteLine(tempString);
            break;
        }
    }
}