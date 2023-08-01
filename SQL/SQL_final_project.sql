USE world_death;
SELECT * from caus_death;

SELECT country, SUM(meningitis) as 'num_meningitis', SUM(alzheimer_and_other_dementias) as 'num_alzheimer_and_other_dementias', 
SUM(parkinson) as 'num_parkinson', SUM(nutritional_deficiencies) as 'num_nutritional_deficiencies', SUM(malaria) as 'num_malaria', 
SUM(drowning) as 'num_drowning', SUM(interpersonal_violence) as 'num_interpersonal_violence', SUM(maternal_disorders) as 'num_maternal_disorders',
SUM(hiv) as 'num_hiv', SUM(drug_use_disorder) as 'num_drug_use_disorder', SUM(tuberculosis) as 'num_tuberculosis', 
SUM(cardiovascular_diseases) as 'num_cardiovascular_diseases', 
SUM(lower_respiratory_infections) as 'num_lower_respiratory_infections', SUM(neonatal_disorders) as 'num_neonatal_disorders', SUM(alcohol_use_disorders) as 'num_alcohol_use_disorders', 
SUM(self_harm) as 'num_self_harm', SUM(exposure_to_force_of_nature) as 'num_exposure_to_force_of_nature', SUM(diarrheal_diseases) as 'num_diarrheal_diseases', SUM(environmental_heat_and_cold_exposure) as 'num_environmental_heat_and_cold_exposure', SUM(neoplasms) as 'num_neoplasms', SUM(conflict_and_terrorism) as 'num_conflict_and_terrorism', 
SUM(diabetes_mellitus) as 'num_diabetes_mellitus', SUM(chronic_kidney_disease) as 'num_chronic_kidney_disease', SUM(poisonings) as 'num_poisonings',
SUM(protein_energy_malnutrition) as 'num_protein_energy_malnutrition', SUM(road_injuries) as 'num_road_injuries', 
SUM(chronic_respiratory_diseases) as 'num_chronic_respiratory_diseases', SUM(cirrhosis_and_other_chronic_liver_diseases) as 'num_cirrhosis_and_other_chronic_liver_diseases', SUM(digestive_diseases) as 'num_digestive_diseases', SUM(fire_heat_and_hot_dubstances) as 'num_fire_heat_and_hot_dubstances', SUM(acute_hepatitis) as 'num_acute_hepatitis'from caus_death
group by country
order by country DESC;