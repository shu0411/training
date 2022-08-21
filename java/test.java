import java.util.*;
public class test
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer a = Integer.valueOf(sc.next());
        Integer b = Integer.valueOf(sc.nextInt());
        Integer c = Integer.valueOf(sc.nextInt());
        Integer ans = a+b+c;
        String s = sc.next();
        System.out.println(ans.toString() + " " + s);
        sc.close();
    }
}   