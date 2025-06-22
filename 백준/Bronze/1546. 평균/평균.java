import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int largest_array = 0;
		double sum = 0;
		
		int answer = sc.nextInt();
		sc.nextLine();
		
		int[] array = new int[answer];
		double[] f_array = new double[answer];
		
		for (int i = 0; i < answer; i++) {
            array[i] = sc.nextInt();
            if (array[i] > largest_array) {
                largest_array = array[i]; // 최댓값 업데이트
            }
        }
		
		for (int k = 0; k < answer; k++) {
			f_array[k] = (double)array[k] / largest_array * 100;
			sum += f_array[k];
		}
		
		System.out.println(sum / answer);
	}
	
	

}
