"""
Created on Thu Nov  7 10:07:21 2024

@author: erikas
"""

"""
Årlige kostnader for elbil og for bensinbil
"""
  
#Antall kjørte km/år / dager i året /tfa
km_per_år = 10000
dager_i_år = 365
tfa = 8.38 # [kr/dag] Trafikkforsikring per dag

#Elbil kostnader
elbil_forsikring = 5000  # [kr/år] Forsikring for elbil
strompris = 2 # [kr/kWh] Strømpris per kWh
stromforbruk = 0.2 # [kWh/km] Strømforbruk per km
elbil_bomavgift = 0.1 # [kr/km] Bomavgift per km for elbil

#total elbil kostnader
elbil_drivstoff = stromforbruk * km_per_år * strompris # [kr/år] Strømforbruk per år
elbil_tfa_år = tfa * dager_i_år  # [kr/år] Trafikkforsikring per år
elbil_bomavgift_år= elbil_bomavgift* km_per_år # [kr/år] Bomavgift per år
elbil_total_kostnader_år = elbil_forsikring + elbil_drivstoff + elbil_tfa_år + elbil_bomavgift_år

#bensinbil kostnader
bensinbil_forsikring = 7500 # [kr/år] Forsikring for bensinbil
bensinbil_pris = 1 # [kr/km] Bensinpris per km
bensinbil_bomavgift = 0.3 # [kr/km]  Bomavgift per km for bensinbil


#Total bensinbil kostnader
bensinbil_bensin_år = bensinbil_pris * km_per_år # [kr/år] Bensinforbruk per år
bensinbil_tfa_år= tfa * dager_i_år  # [kr/år] Trafikkforsikring per år
bensinbil_bomavgift_år = bensinbil_bomavgift * km_per_år # [kr/år] Bomavgift per år
bensinbil_total_kostnader_år = bensinbil_forsikring + bensinbil_bensin_år + bensinbil_tfa_år + bensinbil_bomavgift_år

#kostnadsdifferanse
kostnadsdifferanse = bensinbil_total_kostnader_år - elbil_total_kostnader_år


print ("Årlige kostnader for elbil =", elbil_total_kostnader_år)
print ("Årlige kostnader for bensinbil =", bensinbil_total_kostnader_år)
print ("årlig kostnadsdifferanse =", int(kostnadsdifferanse))