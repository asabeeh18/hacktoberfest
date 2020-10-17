import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class DivisibleSumPairs {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String temp = br.readLine();
		int n, k, count = 0;
		int[] a;
		int[] mod;
		n = Integer.parseInt(temp.split(" ")[0]);
		k = Integer.parseInt(temp.split(" ")[1]);
		a = new int[n];
		mod = new int[k];
		temp = br.readLine();
		for(int i = 0; i < n; i++) {
			a[i] = Integer.parseInt(temp.split(" ")[i]);
			mod[i] = a[i] % k;
		}
		for(int i = 0; i < n; i++) {
			for(int j = i + 1; j < n; j++) {
				if((mod[i] + mod[j]) % k == 0)
					count++;
			}
		}
		System.out.println(count);
	}

}
