public class Transportmittel {
    private String name;
    private double grundVerbrauch;
    private double extraVerbrauch;
    private int plaetze;

    static double preis = 1.71;
    static double streckeInKm = 3.9;

    public Transportmittel(String name, double grundVerbrauch, double extraVerbrauch, int plaetze){
        this.name = name;
        this.grundVerbrauch = grundVerbrauch;
        this.extraVerbrauch = extraVerbrauch;
        this.plaetze = plaetze;
    }



    public double berechneVerbrauch(int passagiere) {
        int anzahlTransportmittel = gibAnzahl(passagiere);

        return (grundVerbrauch * anzahlTransportmittel + passagiere * extraVerbrauch) * streckeInKm;
    }

    public int gibAnzahl(int passagiere){
        return (int) Math.ceil(passagiere / (double) plaetze);
    }

    public static void gibErgebnisAus(Transportmittel[] transportmittelArray, int passagiere){
        Transportmittel guenstigstes = transportmittelArray[0];

        for(int i = 0; i < transportmittelArray.length; i++){
            double verbrauch = transportmittelArray[i].berechneVerbrauch(passagiere);
            if (verbrauch < guenstigstes.berechneVerbrauch(passagiere)){
                guenstigstes = transportmittelArray[i];
            }
        }

        System.out.println(guenstigstes.name);
        System.out.println(guenstigstes.berechneVerbrauch(passagiere));
    }

    public static void main(String args[]){
        int passagiere = Integer.parseInt(args[0]);

        Transportmittel[] transportmittelArray = {
                new Transportmittel("zug", 50.0,0.1, 80),
                new Transportmittel("taxi", 7.0, 0.07, 4),
                new Transportmittel("kleinesTaxi",6, 0.07, 3),
                new Transportmittel("plane", 450, 24, 150)
        };

        gibErgebnisAus(transportmittelArray, passagiere);
    }
}