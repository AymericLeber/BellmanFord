package Bellman;
import java.util.ArrayList;

public class BellmanFord
{
	public static int[] bellmanFord(Graphe g, int[][] tabPoids, Sommet sommet)
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

	public static void afficherDistances(int[] dist)
	{
		for (int i = 0; i < dist.length; i++)
			System.out.println("Distance de la source vers le sommet " + i + " : " + dist[i]);
	}

	public static void afficherGraphe(Graphe g)
	{
		System.out.println("Graphe : ");
		for (Arete arete : g.getAretes())
			System.out.println(arete.getDepart() + " -> " + arete.getDesti());
	}
	
	public static void main(String[] args) {
		Graphe graphe = new Graphe();
		Sommet a = new Sommet("A");
		Sommet b = new Sommet("B");
		Sommet c = new Sommet("C");
		Sommet d = new Sommet("D");
		Sommet e = new Sommet("E");
		Sommet f = new Sommet("F");
		Sommet g = new Sommet("G");
		graphe.ajouterSommet(a);
		graphe.ajouterSommet(b);
		graphe.ajouterSommet(c);
		graphe.ajouterSommet(d);
		graphe.ajouterSommet(e);
		graphe.ajouterSommet(f);
		graphe.ajouterSommet(g);
		graphe.ajouterArete(new Arete(a, b));
		graphe.ajouterArete(new Arete(a, c));
		graphe.ajouterArete(new Arete(b, d));
		graphe.ajouterArete(new Arete(c, d));
		graphe.ajouterArete(new Arete(d, e));
		graphe.ajouterArete(new Arete(e, f));
		graphe.ajouterArete(new Arete(e, g));
		graphe.ajouterArete(new Arete(f, g));
		int[][] tabPoids = new int[graphe.getSommets().size()][graphe.getSommets().size()];
		tabPoids[graphe.getSommets().indexOf(a)][graphe.getSommets().indexOf(b)] = 2;
		tabPoids[graphe.getSommets().indexOf(a)][graphe.getSommets().indexOf(c)] = 3;
		tabPoids[graphe.getSommets().indexOf(b)][graphe.getSommets().indexOf(d)] = 1;
		tabPoids[graphe.getSommets().indexOf(c)][graphe.getSommets().indexOf(d)] = 2;
		tabPoids[graphe.getSommets().indexOf(d)][graphe.getSommets().indexOf(e)] = 3;
		tabPoids[graphe.getSommets().indexOf(e)][graphe.getSommets().indexOf(f)] = 4;
		tabPoids[graphe.getSommets().indexOf(e)][graphe.getSommets().indexOf(g)] = 5;
		tabPoids[graphe.getSommets().indexOf(f)][graphe.getSommets().indexOf(g)] = 1;
		afficherGraphe(graphe);
		int[] dist = bellmanFord(graphe, tabPoids, b);
		afficherDistances(dist);
	}
}

class Graphe
{
	private ArrayList<Sommet> sommets;
	private ArrayList<Arete> aretes;

	public Graphe()
	{
		sommets = new ArrayList<Sommet>();
		aretes = new ArrayList<Arete>();
	}

	public void ajouterSommet(Sommet sommet) {sommets.add(sommet);}
	public void ajouterArete(Arete arete) {aretes.add(arete);}
	
	public ArrayList<Sommet> getSommets() {return sommets;}
	public ArrayList<Arete> getAretes()	{return aretes;}
}

class Sommet
{
	private String id;
	public Sommet(String id)
	{
		this.id = id;
	}

	public String getId() {return id;}

	public String toString() {return id;}
}

class Arete
{
	private Sommet depart;
	private Sommet desti;

	public Arete(Sommet depart, Sommet desti)
	{
		this.depart = depart;
		this.desti = desti;
	}

	public Sommet getDepart() {return depart;}
	public Sommet getDesti() {return desti;}

	public String toString() {return depart + " -> " + desti;}
}