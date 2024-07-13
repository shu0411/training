Console.WriteLine("Signed integral types:");

Console.WriteLine($"sbyte  : {sbyte.MinValue} to {sbyte.MaxValue}");
Console.WriteLine($"short  : {short.MinValue} to {short.MaxValue}");
Console.WriteLine($"int    : {int.MinValue} to {int.MaxValue}");
Console.WriteLine($"long   : {long.MinValue} to {long.MaxValue}");

Console.WriteLine("");
Console.WriteLine("Unsigned integral types:");

Console.WriteLine($"byte   : {byte.MinValue} to {byte.MaxValue}");
Console.WriteLine($"ushort : {ushort.MinValue} to {ushort.MaxValue}");
Console.WriteLine($"uint   : {uint.MinValue} to {uint.MaxValue}");
Console.WriteLine($"ulong  : {ulong.MinValue} to {ulong.MaxValue}");

Console.WriteLine("");
Console.WriteLine("Floating point types:");
Console.WriteLine($"float  : {float.MinValue} to {float.MaxValue} (with ~6-9 digits of precision)");
Console.WriteLine($"double : {double.MinValue} to {double.MaxValue} (with ~15-17 digits of precision)");
Console.WriteLine($"decimal: {decimal.MinValue} to {decimal.MaxValue} (with 28-29 digits of precision)");

int[] data;
data = new int[3];

string shortenedString = "Hello World!";
Console.WriteLine(shortenedString);

string value_3 = "bad";
int result = 0;
if (int.TryParse(value_3, out result))
{
    Console.WriteLine($"Measurement: {result}");
}
else
{
    Console.WriteLine("Unable to report the measurement.");
}
Console.WriteLine($"Check: {result}");
if (result > 0)
    Console.WriteLine($"Measurement (w/ offset): {50 + result}");

// 4/9
string[] values = { "12.3", "45", "ABC", "11", "DEF" };

string message = "";
double total = 0;
foreach (string value_4 in values)
{
    double number;
    if (double.TryParse(value_4, out number))
    {
        total += number;
    }
    else
    {
        message += value_4;
    }
}
Console.WriteLine($"Message: {message}");
Console.WriteLine($"Total: {total}");

// 5/9
int value1 = 11;
decimal value2 = 6.2m;
float value3 = 4.3f;

int result1 = 0;
decimal result2 = 0;
float result3 = 0;

//result1 = (int)Math.Round((double)value1 / (double)value2);
result1 = Convert.ToInt32(value1 / value2);
result2 = value2 / (decimal)value3;
result3 = value3 / value1;

// Your code here to set result1
// Hint: You need to round the result to nearest integer (don't just truncate)
Console.WriteLine($"Divide value1 by value2, display the result as an int: {result1}");

// Your code here to set result2
Console.WriteLine($"Divide value2 by value3, display the result as a decimal: {result2}");

// Your code here to set result3
Console.WriteLine($"Divide value3 by value1, display the result as a float: {result3}");