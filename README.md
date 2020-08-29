# Optimierung von Fernwärmeverbünden

## Ziel - Goal
[DE] 

1. Energieverbrauch von Fernwärmeanlagen allgemein minimieren (Primärenergieeinsatz). 
2. Einsatz von Spitzenlast-Kesseln minimieren. Typischerweise verwenden diese Kessel fossilen Brennstoffen, während der Haupt-Kessel erneuerbare Energien verwendet.  

[EN] 

1. Minimize the energy consumption of disctrict heating netowrks (primary energy use)
2. Minimize the use of peak load boilers. These boilers typically use fossil fuels, while the main boiler uses an renewable energy source.

## Hintergrund - Big Picture:

[DE] 

Fernwärmeverbünde auf Basis erneuerbarer Energien sind ein wesentlicher Bestandteil der Energiestrategie 2050. Ressourceneffizienz ist ein Hauptthema und soll im Rahmen der Optimierung bestehender Fernwärmeverbünde mittels Datenanalyse im Mittelpunkt stehen.

Die AEW als Betreiber von mehr als 80 Fernwärmeverbünden sieht durch diese Challenge eine sehr gute Möglichkeit der Replizierbarkeit.

[EN] 

District heating networks based on renewable energies are an essential part of the Energy Strategy 2050. Resource efficiency is a main goal and should be the focus of the optimisation of existing district heating networks through data analysis.

AEW as operator of more than 80 district heating networks sees a very good opportunity for replicability for this challenge.

## Idee - Idea
[DE]

- Lastprognosen auf Basis von historischen Verbrauchsdaten, Wetterdaten, etc projizieren.
- Leistungs-Scheduling innerhalb des Verbundes unter Ausnutzung der thermischen Masse der belieferten Objekte oder Einsatz von verteilten kleineren Zwischenspeichern.

[EN]

- Load forecasts based on historical consumption data, weather data, etc.
- Performance scheduling within the network by exploiting the thermal mass of the supplied objects or using distributed smaller intermediate storage facilities.

## Daten - Data

[DE]

- [Verbrauchs- und Erzeugungsdaten eines Dorf-Fernwärmenetzes mit 9 Abnehmern](https://github.com/district-heating-2020/data_analysis/tree/master/data/energy): 2 Jahren (2018-2019), alle 5 Minuten
- [Historische Wetterdaten für die Region](https://github.com/district-heating-2020/data_analysis/tree/master/data/weather)

[EN] 

- [Production and usage data of an existing distric heating network for 9 client buildings](https://github.com/district-heating-2020/data_analysis/tree/master/data/energy): 2 years (2018-2019), every 5 minutes 
- [Historical weather data for the area](https://github.com/district-heating-2020/data_analysis/tree/master/data/weather)

### Weitere potentielle Datenquellen
- Kalenderdaten (Feiertage, Ferienzeit, …)
- Kenndaten/Modelldaten Fernwärmesysteme
- Geodaten (Fernwärmenetz, Wärmebedarf, Wärmequelle, …)
- [HSLU Programm "Thermische Netze"](https://www.energieschweiz.ch/page/de-ch/thermische-netze): seems relevant, but is out of date
- [Statistics from Germany](https://de.statista.com/statistik/daten/studie/166824/umfrage/verbrauch-von-fernwaerme-in-deutschland/)

## Team

- Toni Wietlisbach, AEW --> Fernwärme
- [Andy Gubser](https://github.com/andygubser) --> Data science
- [Martin Horeni](https://github.com/Martin1877) --> Data Science
- Wolfram Willuhn
- [Emilie Boillat](https://github.com/boillat) --> Dokumentation

Dieses Projekt wurde im Rahmen der [Energy Hack Days 2020](https://hack.opendata.ch/event/31) lanciert. 

## Anforderungen

### Allgemein

**Für wen**: Steuerungssystem einer Fernwärmeanlage, die von einem erneuerbaren Energiequelle (z.B. Holzkessel) betrieben wird, sowie zusätzlich bei Bedarf einen oder mehrere fossile Kessel (z.B. Gas). 

**Was**: Eine Prognose der benötigten Gesamtleistung (in kW) für jede Stunde der nächsten 24h, abhängig von der meteoroligischer Prognose für die Aussentemperatur
und weiteren relevanten Parametern". 

**Wieso**: Damit das Steuerungssystem 1) möglichst wenig Energie insgesamt verbraucht, und 2) auf den Einsatz der fossilen Quellen verzichten kann. Das Ziel ist, dass möglichst nur das Zusammenspiel des Holzkessels und des Speichers (eine Art grosser Boiler) benötigt werden, um die Wärmebedürfnisse zu decken

### Detailliert 

1. Als AEW möchten wir wissen, wieviel kW/h an Gaskessel-produzierte Wärme wir pro Jahr durch die Leistungsprognose hätten sparen können, um zu entscheiden ob es einen bedeutenden Einfluss auf die Klimaziele hätte. 
2. Als Betriebsingenieur brauche ich eine Prognose der benötigten Gesamtleistung (in kW) für jede Stunde der nächsten 24h, damit ich sie visualisieren kann. 
3. Als Data Scientist will ich wissen, welche Wetter-Faktoren aufgrund der historischen Daten die benötigte Gesamtleistung (in kW) beteutend beinflussen (z.B. neben der Aussentemperatur auch die globale Strahlung, Windstärke, Luftfeuchtigkeit,...), damit ich die richtigen Input-Daten für die Prognose wähle
4. Als Data Scientist will ich die fixe Betriebszeiten von Kunden-Boilers aus Verbrauchsdaten erkennen, damit ich diesen Input der Leistungs-Prognose hinzufügen kann

### Weitere Schritte: Anforderungen für die Integration ins Leisystem
Recommender: Speicher jetzt entladen oder füllen?
Recommender: Wie viel Wärme soll der Holzkessel jetzt produzieren? 
Recommender: Soll der Ölkessel (Nr. 6) "abgeworfen" werden? 


## Über Fernwärmeverbunde

Ein Wärmeerzeuger kann an wenige bis 1000 Gebäude Wärme verteilen, je nach Grösse der Anlage. 

Die Wärmequelle kann z.B. eine Wärmepumpe, Kehrrichtverbrennungsanlage, oder ein Holzkessel sein. 

In unserem Data Sample geht es um ein Dorf-Fernwärmeverbund mit 9 Kunden (darunter private Haushalte, Industrie, Schulhaus, Gemeindehaus)

[Bild Netzplan]

Im Netzplan wird pro Kunde die maximale Leistung (in kW) angegeben.

Im Mittelland bedeutet diese maximale Leistung: wieviel Energie braucht es, um die Raumtemperatur auf 20°C zu heizen wenn die Aussentemperatur 8°C beträgt.

[Bild Heizzentrale]

![Heizzentrale](https://github.com/district-heating-2020/data_analysis/blob/master/doc/Heat-station.png?raw=true)

* Der Holzkessel produziert in der Regel die Wärme (kann auf ca 30%-100% seiner Kapazität laufen oder ausgeschaltet sein)
* Die zwei Gaskessel werden bei Bedarf eingeschlatet um eine Spitzenlast zu decken. Sie dienen auch als Redundanz, sollte der Holzkessel ausfallen. 
* Der Speicher bekommt unten abgekühltes Wasser zurück aus dem Netz, oben warmes Wasser aus den Wärmeerzeugern. Er kann je nach Bedarf Wärme speichern oder abgeben. Er hat allerdings keine unbegrenzte Kapazität (also z.B muss der Holzkessel runterfahren, bevor der Speicher voll wird). 

Daten
-----
* Gelb markiert = Wärmezählerdaten (reine Messdaten)
* Weiss markiert = Leitsystemdaten (zur Steuerung)
* Grau markiert = Soll-daten vom Leistsystem (zur Steuerung)

Die Zieltemperraturen (Soll Gesamtzentrale z.B. 85.0°C, Soll Wärmekessel z.B. 93.1°C) werden gerechnet anhand der momentanen Aussentemperatur. 
Wärmekessel: auch gerechnet anhand der Aussentemperatur

Systemsteuerung
------------------------

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

Kunden
----------

[Bilder Beispiele Kunden]

Kunde Nr 1: Gewerbe

Kunde Nr 2: Schulhaus

Kunde Nr 3: Schulhaus

Kunde Nr 4: Gemeindehaus

Kunde Nr 5: Turnhalle / Mehrzweckhalle

Kunde Nr 6: Gewerbe (Betrieb)

Kunde Nr 7: Gewerbe (Büro)

Kunde Nr 8: Gewerbe

Kunde Nr 9: Gewerbe

Wärmetauscher = Schnittstelle zwischen Netz und Kunden-Gebäude. Beide sind geschlossene Kreise

Spreizung = Temperaturunterschied zwischen den Fluss beim Eingang bzw. Ausgang. Diesen Wert probiert man möglichst gross zu halten. 
