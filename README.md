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

