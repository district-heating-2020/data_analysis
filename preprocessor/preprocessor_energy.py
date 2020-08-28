import pandas as pd

energy1 = pd.read_csv("./data_sources/energy/1_prot.csv")

columns_keys = ['Timestamp', 'T6 Aussentemp.(°C)', 'T7 RL Primär(°C)',
                    'T8 VL Sekundär(°C)', 'T11 RL Sekundär(°C)',
                    'Solltemp. VL Sekundär(°C)', 'Max.Rücklauftemp.primär(°C)',
                    'B-Solltemp.(°C)', 'B-Status Pumpe', 'B-Status Kreis',
                    'B-Status Mischer', 'Puffer EIN Oben(°C)', 'Puffer AUS Unten(°C)',
                    'Ventilstellung(%)', 'AT Mittel(°C)', 'AT Langzeit(°C)',
                    'WZ Wärmemenge(kWh)', 'WZ Leistung(kW)', 'WZ Duchfluss(l/h)',
                    'WZ Rücklauftemp.(°C)', 'WZ Vorlauftemp.(°C)', 'WZ Spreizung(°C)',
                    'Ventilstellung Gesamt(%)']

columns_values = ["timestamp", "aussentemperatur", "primär_temperatur",
               "sekundär_temperatur_vl", "sekundär_temperatur_rl",
               "sekundär_temperatur_vl_soll", "status_pump", "status_circle",
               "status_mischer", "puffer_oben_ein", "puffer_unten_aus",
               "ventilstellung", "aussentemperatur_mittel", "aussentemperatur_langzeit",
               "wärmemenge_kwh", "leistung_kw", "durchfluss_liter_per_hour",
               "rücklauftemperatur", "vorlauftemperatur", "spreizung_celsius",
               "ventilstellung_gesamt"]
columns_dict = dict(zip(columns_keys, columns_values))

energy1.rename(columns=columns_dict, inplace=True)
energy1.set_index("timestamp", inplace=True)



# energy2 = pd.read_csv("./data_sources/energy/2_prot.csv")
# energy3 = pd.read_csv("./data_sources/energy/3_prot.csv")
# energy4 = pd.read_csv("./data_sources/energy/4_prot.csv")
# energy5 = pd.read_csv("./data_sources/energy/5_prot.csv")
# energy6 = pd.read_csv("./data_sources/energy/6_protSPS.csv")
# energy7 = pd.read_csv("./data_sources/energy/7_prot.csv")
# energy8 = pd.read_csv("./data_sources/energy/8_prot.csv")
# energy9 = pd.read_csv("./data_sources/energy/9_prot.csv")
