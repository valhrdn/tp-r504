public class Monprog
{
	public static void main( String[] args )
	{
		System.out.println( "nb args=" + args.length );
		for( int i=0; i<args.length; i++ )
			System.out.println( "- " + i + ": " + args[i] );
	}
}
