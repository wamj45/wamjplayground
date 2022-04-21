import java.io.*;
import java.util.Scanner;

public class project {

  public static String[] removeFirst(String[] set) {
    String[] new_arr = new String[set.length - 1];

    for (int i = 1; i < set.length; i++) {
      new_arr[i-1] = set[i];
    }
    return new_arr;
  }

  public static String[] getGroup(String[] champions, char groupName) {
    String[] group_arr = new String[4];
    int count = 0;
    for (int i=0; i<champions.length; i++) {
      char group = champions[i].charAt(champions[i].length() - 1);
      if (groupName == group) {group_arr[count] = champions[i]; count++;}
      }
    return group_arr;
  }

  public static String[] getChampionsLeague(String[] teams) {
    // There are 32 teams that qualify for the UEFA Champions League
    // Adding in a Mid Tier Brazilian team to replace missing team FC Sheriff from Moldova
    String[] champions = new String[32];
    int count = 0;
    for (int team = 0; team < teams.length; team++) {
        int star = teams[team].indexOf("*");
        if (star > 0) {
          champions[count] = teams[team];
          count++;
          }
        }
    return champions;
  }

  public static void main(String[] args) throws Exception {
    project projectManager = new project();
    String[] data = new String[631];
    int count = 0;
    char A = 'A';
    char B = 'B';
    char C = 'C';
    char D = 'D';
    char E = 'E';
    char F = 'F';
    char G = 'G';
    char H = 'H';

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

    String[] qualifiedTeams = projectManager.getChampionsLeague(remove_text);

    String[] groupA = projectManager.getGroup(qualifiedTeams, A);
    String[] groupB = projectManager.getGroup(qualifiedTeams, B);
    String[] groupC = projectManager.getGroup(qualifiedTeams, C);
    String[] groupD = projectManager.getGroup(qualifiedTeams, D);
    String[] groupE = projectManager.getGroup(qualifiedTeams, E);
    String[] groupF = projectManager.getGroup(qualifiedTeams, F);
    String[] groupG = projectManager.getGroup(qualifiedTeams, G);
    String[] groupH = projectManager.getGroup(qualifiedTeams, H);
  }
}
