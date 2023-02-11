import java.awt.*;
import java.awt.geom.*;
import javax.swing.*;

public class GrapheUI extends JPanel {

    private String[] sommets;
    private String[][] aretes;

    public GrapheUI(String[] sommets, String[][] aretes) {
        this.sommets = sommets;
        this.aretes = aretes;
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D)g;

        int nbSommets = sommets.length;
        int rayon = 150;
        int xCentre = getWidth()/2;
        int yCentre = getHeight()/2;
        int x, y;
        double angle;

        // dessiner les sommets
        for (int i = 0; i < nbSommets; i++) {
            angle = 2 * Math.PI * i / nbSommets;
            x = (int)Math.round(xCentre + rayon * Math.cos(angle));
            y = (int)Math.round(yCentre + rayon * Math.sin(angle));
            g2.draw(new Ellipse2D.Double(x-rayon/2, y-rayon/2, rayon, rayon));
            g2.drawString(sommets[i], x, y);
        }

        // dessiner les arêtes
        for (int i = 0; i < aretes.length; i++) {
            String u = aretes[i][0];
            String v = aretes[i][1];
            int poids = Integer.parseInt(aretes[i][2]); // récupérer le poids
            angle = 2 * Math.PI * getIndex(u) / nbSommets;
            int x1 = (int)Math.round(xCentre + rayon * Math.cos(angle));
            int y1 = (int)Math.round(yCentre + rayon * Math.sin(angle));
            angle = 2 * Math.PI * getIndex(v) / nbSommets;
            int x2 = (int)Math.round(xCentre + rayon * Math.cos(angle));
            int y2 = (int)Math.round(yCentre + rayon * Math.sin(angle));
            g2.draw(new Line2D.Double(x1, y1, x2, y2));
            g2.drawString(Integer.toString(poids), (x1+x2)/2, (y1+y2)/2); // afficher le poids
        }
    }

    // obtenir l'index du sommet correspondant à une étiquette
    private int getIndex(String etiquette) {
        for (int i = 0; i < sommets.length; i++) {
            if (sommets[i].equals(etiquette)) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String[] sommets = {"a", "b", "c", "d", "e", "f", "g"};
        String[][] aretes = {   {"a", "b", "1"}, {"a", "c", "2"},
                                {"b", "d", "3"}, {"c", "d", "4"},
                                {"d", "e", "5"}, {"e", "f", "6"},
                                {"e", "g", "7"}, {"f", "g", "8"}};
        GrapheUI grapheUI = new GrapheUI(sommets, aretes);
        JFrame frame = new JFrame("GrapheUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(grapheUI);
        frame.setSize(1500, 1500);
        frame.setVisible(true);
    }
}