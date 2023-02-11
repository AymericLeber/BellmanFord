package Bellman;
import java.util.ArrayList;
import java.util.Arrays;

public class BellmanFord
{
	public static int[] bellmanFord(Graphe g, int[][] tabPoids, String sommet)
	{
		int[] dist = new int[g.getSommets().size()];

		for (int i = 0; i < g.getSommets().size(); i++)
			dist[i] = Integer.MAX_VALUE;		
		dist[g.getSommets().indexOf(sommet)] = 0;
		
		
		for (int i = 0; i < g.getSommets().size() - 1; i++)
		{
			for (Arete arete : g.getAretes())
			{
				int depart = g.getSommets().indexOf(arete.getDepart());
				int desti  = g.getSommets().indexOf(arete.getDesti());
				int poids  = tabPoids[depart][desti];
				if (dist[depart] + poids < dist[desti])
					dist[desti] = dist[depart] + poids;
			}
		}

		return dist;
	}

	public static void afficherDistances(Graphe g, int[] dist)
	{
		String[] tabSommets = g.getSommetsTab();
		for (int i = 0; i < dist.length; i++)
			System.out.println("Distance de la source vers le sommet " + tabSommets[i] + " : " + dist[i]);
	}

	public static void afficherGraphe(Graphe g)
	{
		System.out.println("Graphe : ");
		for (Arete arete : g.getAretes())
			System.out.println(arete.getDepart() + " -> " + arete.getDesti());
	}
	
	public static void main(String[] args) 
	{
		String[] sommets = {"a", "b", "c", "d", "e", "f", "g"};
		String[][] aretes = {	{"a", "b"}, {"a", "c"}, 
								{"b", "d"}, {"c", "d"}, 
								{"d", "e"}, {"e", "f"}, 
								{"e", "g"}, {"f", "g"}};
		Graphe graphe = new Graphe(sommets, aretes);
		int[][] tabPoids = {	{0, 1, 2, 0, 0, 0, 0},
								{0, 0, 0, 1, 0, 0, 0},
								{0, 0, 0, 1, 0, 0, 0},
								{0, 0, 0, 0, 1, 0, 0},
								{0, 0, 0, 0, 0, 1, 1},
								{0, 0, 0, 0, 0, 0, 1},
								{0, 0, 0, 0, 0, 0, 0}};
		afficherGraphe(graphe);
		int[] dist = bellmanFord(graphe, tabPoids, "a");
		afficherDistances(graphe, dist);
	}
}

class Graphe
{
	private ArrayList<String> sommets;
	private ArrayList<Arete> aretes;

	public Graphe()
	{
		sommets = new ArrayList<String>();
		aretes = new ArrayList<Arete>();
	}

	public Graphe(String[] sommets, String[][] aretes)
	{
		this();
		this.sommets = new ArrayList<String>(Arrays.asList(sommets));	
		for (String[] arete : aretes)
		{
			this.aretes.add(new Arete(arete[0], arete[1]));
		}
	}

	public void ajouterSommet(String sommet) {sommets.add(sommet);}
	public void ajouterArete(Arete arete) {aretes.add(arete);}

	public String[] getSommetsTab() {return sommets.toArray(new String[sommets.size()]);}
	
	public ArrayList<String> getSommets() {return sommets;}
	public ArrayList<Arete> getAretes()	{return aretes;}
}

class Arete
{
	private String depart;
	private String desti;

	public Arete(String depart, String desti)
	{
		this.depart = depart;
		this.desti = desti;
	}

	public String getDepart() {return depart;}
	public String getDesti() {return desti;}

	public String toString() {return depart + " -> " + desti;}
}