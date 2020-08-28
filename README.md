# data_analysis

This repo is part of the Energy Hack Days 2020: https://hack.opendata.ch/project/461/

## Ziel

### Anforderung allgemein

**Für wen**: Steuerungssystem einer Fernwärmeanlage, die von einem erneuerbaren Energiequelle (z.B. Holzkessel) betrieben wird, sowie zusätzlich bei Bedarf einen oder mehrere fossile Kessel (z.B. Gas). 

**Was**: Eine Prognose der benötigten Gesamtleistung (in kW) für jede Stunde der nächsten 24h, abhängig von der meteoroligischer Prognose für die Aussentemperatur
und weiteren relevanten Parametern". 

**Wieso**: Damit das Steuerungssystem 1) möglichst wenig Energie insgesamt verbraucht, und 2) auf den Einsatz der fossilen Quellen verzichten kann. Das Ziel ist, dass möglichst nur das Zusammenspiel des Holzkessels und des Speichers (eine Art grosser Boiler) benötigt werden, um die Wärmebedürfnisse zu decken

### Anforderungen detailliert

1. Als Data Scientist will ich wissen, welche Wetter-Faktoren aufgrund der historischen Daten die benötigte Gesamtleistung (in kW) beteutend beinflussen (z.B. neben der Aussentemperatur auch die globale Strahlung, Windstärke, Luftfeuchtigkeit,...), damit ich die richtigen Input-Daten für die Prognose wähle
2. Als Data Scientist will ich die fixe Betriebszeiten von Kunden-Boilers aus Verbrauchsdaten erkennen, damit ich diesen Input der Leistungs-Prognose hinzufügen kann
3. Als Entwickler brauche ich eine Prognose der benötigten Gesamtleistung (in kW) für jede Stunde der nächsten 24h, damit ich sie visualisieren kann. 
4. Als AEW möchten wir wissen, wieviel kW/h an Gaskessel-produzierte Wärme wir pro Jahr durch die Leistungsprognose hätten sparen können, um zu entscheiden ob es einen bedeutenden Einfluss auf die Klimaziele hätte. 

### Weitere Schritte: Anforderungen für die Integration ins Leisystem
Recommender: Speicher jetzt entladen oder füllen?
Recommenter: Wie viel Wärme soll der Holzkessel jetzt produzieren? 


## Über Fernwärmeverbunde

Ein Wärmeerzeuger kann an wenige bis 1000 Gebäude Wärme verteilen, je nach Grösse der Anlage. 

Die Wärmequelle kann z.B. eine Wärmepumpe, Kehrrichtverbrennungsanlage, oder ein Holzkessel sein. 

In unserem Data Sample geht es um ein Dorf-Fernwärmeverbund mit 9 Kunden (darunter private Haushalte, Industrie, Schulhaus, Gemeindehaus)

[Bild Netzplan]
Im Netzplan wird pro Kunde die maximale Leistung (in kW) angegeben.
Im Mittelland bedeutet diese maximale Leistung: wieviel Energie braucht es, um die Raumtemperatur auf 20°C zu heizen wenn die Aussentemperatur 8°C beträgt.

[Bild Heizzentrale]

* Der Holzkessel produziert in der Regel die Wärme (kann auf ca 30%-100% seiner Kapazität laufen oder ausgeschaltet sein)
* Die zwei Gaskessel werden bei Bedarf eingeschlatet um eine Spitzenlast zu decken. Sie dienen auch als Redundanz, sollte der Holzkessel ausfallen. 
* Der Speicher bekommt unten abgekühltes Wasser zurück aus dem Netz, oben warmes Wasser aus den Wärmeerzeugern. Er kann je nach Bedarf Wärme speichern oder abgeben. Er hat allerdings keine unbegrenzte Kapazität (also z.B muss der Holzkessel runterfahren, bevor der Speicher voll wird). 

Daten
-----
Gelb markiert = Wärmezählerdaten (reine Messdaten)

Weiss markiert = Leitsystemdaten (zur Steuerung)

Grau markiert = Soll-daten vom Leistsystem (zur Steuerung)

Die Zieltemperraturen (Soll Gesamtzentrale z.B. 85.0°C, Soll Wärmekessel z.B. 93.1°C) werden gerechnet anhand der momentanen Aussentemperatur. 
Wärmekessel: auch gerechnet anhand der Aussentemperatur



Zur Zeit steuert das Leitsystem die Kessel und den Speicher aufgrund der momentanen Aussentemperaturen. Er "weiss" sozusagen nicht, was in einigen Stunden passiert. 

Beispielsweise kann es in der Übergangszeit zu suboptimalen Spitzen kommen: am Nachmittag scheint die Sonne und der Holzkessel ist ausgeschaltet; der Speicher reicht nicht mehr um die kalte Nacht zu decken. Der Gaskessel wird eingeschlatet, obwohl der Holzkessel alleine hätte locker reichen können, wenn nachmittags mehr gespeichert worden wäre. 

Faktoren hinter den Wärme-Bedarf
-------
* Aussentemperatur
* Zeiten, an denen die individuellen Boiler der Kunden angestellt werden. Normalerweise regelmässig. Kann man bedingt beinflussen mit Fernsteuerung. 
* Globale Strahlung (Erwärmung durch Fenster) --> ?
* Wind (kühlt ab) --> ?
* Luftfeuchtigkeit --> ?
* Industrie-Gebäude abkoppeln: Bei einer Störung kann der Kunde Nr. 6 abgekoppelt werden (eigene Ölheizung vorhanden). Von der Ökobilanz her sind die Gaskessel aber klar besser als die individuelle Ölheizung.  

[Bilder Beispiele Kunden]

Wärmetauscher = Schnittstelle zwischen Netz und Kunden-Gebäude. Beide sind geschlossene Kreise

Spreizung = Temperaturunterschied zwischen den Fluss beim Eingang bzw. Ausgang. Diesen Wert probiert man möglichst gross zu halten. 
