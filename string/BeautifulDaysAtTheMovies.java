import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BeautifulDaysAtTheMovies {
    public static void main(String[] args) throws IOException {
        int i, j, k;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        i = Integer.parseInt(temp[0]);
        j = Integer.parseInt(temp[1]);
        k = Integer.parseInt(temp[2]);
        int beautifulDays = 0;
        while (i <= j) {
            if (Math.abs(i - reverse(i)) % k == 0) {
                beautifulDays++;
            }
            i++;
        }
        System.out.println(beautifulDays);
    }

    private static int reverse(Integer val) {
        String temp = val.toString();
        StringBuilder tem = new StringBuilder(temp);
        tem = tem.reverse();
        temp = tem.toString();
        return Integer.parseInt(temp);
    }
}
