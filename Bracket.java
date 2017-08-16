import java.io.*;
import java.util.*;
class Bracket
{
public static void main(String args[])
{	
	Scanner a=new Scanner(System.in);
	System.out.println("Enter the Bracket sequence \n");
	String s=a.next();
	System.out.println("Checking the string");
	String x=s.replace("(","*");
	String y=x.replace(")",".");
	int length=s.length();
	int q=0;
	String z=".";
	int count1=0,count2=0;
	char temp;
	for( int i = 0; i < s.length( ); i++ )
	{
    temp = y.charAt( i );
    if(temp=='*')
    	{	
    		count1=count1+1;
    	}  
    if(temp=='.')
    	{	
    		count2=count2+1;
    	}  
	}
	
	if(count1==count2)
	{
		System.out.println("Brackets are balanced");
	}
	else
	{
		System.out.println("Imbalanced bracket");
	}
		
}
}
