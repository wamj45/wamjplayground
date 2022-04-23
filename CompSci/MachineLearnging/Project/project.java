import java.io.*;
import java.util.Scanner;
import java.util.Random;

enum GradientDescentChoice {
	STOCHASTIC, BATCH
}

public class project {

  public static String[] removeFirst(String[] set) {
    String[] new_arr = new String[set.length - 1];

    for (int i = 1; i < set.length; i++) {
      new_arr[i-1] = set[i];
    }
    return new_arr;
  }

  public static String[] getRanking(String[] arr) {
    String[] rankings = new String[arr.length];
    for (int i = 0; i < arr.length; i++) {
      char rankComma = arr[i].charAt(',');
      String rank = arr[1].subtring(rankComma);
    }
    return rankings;
  }



  public static void main(String[] args) throws Exception {
    project projectManager = new project();
    // LinearRegressionBasic linearRegress = new LinearRegressionBasic();
    String[] data = new String[631];
    int count = 0;


    Scanner dataset = new Scanner(new File("spi_global_rankings.csv"));
    dataset.useDelimiter(";");

    while (dataset.hasNext())
    {
      String teamData = dataset.next();
      data[count] = teamData;
      count ++;
    }
    dataset.close();

    String[] remove_text = projectManager.removeFirst(data);
    String[] rankingsTest = projectManager.getRanking(remove_text);


  }
}

// public class LinearRegressionBasic {
// 	private double m;
// 	private double c;
// 	private double learningRate = 0.001d;
// 	private int epoch = 1000;
// 	private double[][] trainingSet;
// 	private GradientDescentChoice gradientChoice;
// 	public LinearRegressionBasic(double[][] set, int epoch, GradientDescentChoice gradientChoice) {
// 		this.trainingSet = set;
// 		this.epoch = epoch > 0 ? epoch : this.epoch;
// 		this.gradientChoice = gradientChoice;
// 		trainModel();
// 	}
// 	private final void trainModel() {
// 		stochasticGradientDescent();
// 	}
// 	private void stochasticGradientDescent() {
// 		for (int i = 0; i < epoch * 100; i++) {
// 			Random random = new Random();
// 			int randomIndex = random.nextInt(trainingSet.length);
// 			double slopeGradient = derivativeWithRespectToSlope(trainingSet[randomIndex][0],
// 					trainingSet[randomIndex][1], m, c);
// 			double interceptGradient = derivativeWithRespectToIntercept(trainingSet[randomIndex][0],
// 					trainingSet[randomIndex][1], m, c);
// 			this.m = m - learningRate * slopeGradient;
// 			this.c = c - learningRate * interceptGradient;
// 		}
// 	}
// 	private double derivativeWithRespectToSlope(Double actual, Double x, Double slope, Double intercept) {
// 		double derivative = x * (slope * x + intercept - actual);
// 		return derivative;
// 	}
// 	private double derivativeWithRespectToIntercept(Double actual, Double x, Double slope, Double intercept) {
// 		double derivative = (slope * x + intercept - actual);
// 		return derivative;
// 	}
// 	public double predict(double predictForValue) {
// 		return c + (m * predictForValue);
// 	}
// }
