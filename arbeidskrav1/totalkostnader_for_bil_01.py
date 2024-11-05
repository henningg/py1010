#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:11:32 2024

@author: henninggundersen

Dette er et Python-program som leveres inn til Arbeidskrav1 i PY101-1 24H
Programmet skal beregne og presentere (i konsollen) de årlige
totalkostnadene for elbil og for bensinbil samt årlig
kostnadsdifferanse basert på informasjon gitt i oppgaven.

"""

# Her er grunnlaget for beregning av kostnader, hentet fra oppgaven
AarligKjoerelengde = 10000  # antall km kjørt pr år
ForsikringElbil = 5000  # Forsikringsum pr år
ForsikringBensinbil = 7500  # Forsikringsum pr år
TrafikkforsikringsAvgift = 8.38  # Kostnad i kr/dag
ElbrukElbil = 0.2  # Strømforbruk i kWh/km
ElPris = 2.00  # Kostand for strøm kr/kWh
DrivstoffbrukElbil = ElbrukElbil*ElPris  # BStrømkostnad i kr/km
DrivstoffbrukBensinbil = 1.0  # Bensinskostnad i kr/km
BomavgiftElbil = 0.1  # bomkostnader kr/km
BomavgiftBensinbil = 0.3  # bomkostnader kr/km

# Beregne kost elbil
AarligKostElbil = AarligKjoerelengde * \
    (DrivstoffbrukElbil + BomavgiftElbil) + \
    TrafikkforsikringsAvgift*365 + ForsikringElbil

# Beregne kost bensinbil
AarligKostBensinbil = AarligKjoerelengde * \
    (DrivstoffbrukBensinbil + BomavgiftBensinbil) + \
    TrafikkforsikringsAvgift*365 + ForsikringBensinbil

# Beregne årlig kostnadsdifferanse
AarligBesparelse = abs(AarligKostElbil - AarligKostBensinbil)

# Print årlige kostander Elbil
print("Årlige kostander for Elbil = ", AarligKostElbil)
# Print årlige kostnader Bensinbil
print("Årlige kostander for Bensinbil = ", AarligKostBensinbil)

# Print årlig kostnadsdifferanse
print("Årlige kostnadsdifferanse = ", AarligBesparelse)

# setter tekst som representerer den billigste bilen
BilligsteBil = "Bensinbil"
if (AarligKostElbil < AarligKostBensinbil):
    BilligsteBil = "Elbil"

# Lager en text til print, da den lengden på linje inne i print() ble for stor
BesparelseText = "Årlige besparelse ved å velge" + BilligsteBil +\
    "er kr :" + str(AarligBesparelse)

print(BesparelseText)
