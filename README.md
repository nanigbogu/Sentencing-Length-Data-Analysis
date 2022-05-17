# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Incarceration

### Overview



### Problem Statement


---

### Datasets

* [`df18to21H.csv`](../data/df18to21H.csv): Raw 2018 to 2021 Sentencing Commission Data 
* [`df18to21_cleanedH.csv`](../data/df18to21_cleanedH.csv): Cleaned, Imputed, Feature Engineered 2018 to 2021 Sentencing Commission Data
* [`PEPPOP2021.NST_EST2021_POP-2022-05-11T014539.csv`](../data/PEPPOP2021.NST_EST2021_POP-2022-05-11T014539.csv): Raw 2021 Census Data
* [`census_20.csv`](../data/census_20.csv): Raw 2020 Census Data
* [`population.csv`](../data/population.csv): Combined and Feature Engineered Population Data 

---

### Data Dictionary

**Cleaned, Imputed, Feature Engineered 2018- 2021 Sentencing Commission Data**

|Feature|Possible Values|Description|
|---|---|---|
|**sentence_length**|0 - 9998|Number of months imprisonment ordered| 
|**year_sentenced**|2018 - 2021|Sentence year| 
|**sentence_type**|0 = No Prison, 1 = Prison Only, 2 = Prison + Confinement Conditions, 3 = Probation + Confinement Conditions, 4 = Probation Only|What type of sentence was given| 
|**guideline_range**|0 = N/A, 1 = Guideline Minimum, 2 = Lower Half of Range, 3 = Midpoint of Range, 4 = Upper Half of Range, 5 = Guideline Maximum, 6 = Guideline Min/Max are Equal|Where within the guideline range a case was sentenced(if within range)| 
|**imprisoned**|0 = No, 1 = Yes|Whether the defendant received a prison sentence|
|**guideline_var_pct**|0% - 100%|The percent difference between the guideline minimum and the sentence length|
|**dependents**|0 = No, 1 = Yes|Whether the offender has dependents|
|**count_convictons**|1 - 999|The number of counts of conviction|
|**race**|0 = Info not available, 1 = White/Caucasion, 2 = Black/African American, 3 = American Indian/Alaskan Native, 4 = Asion or Pacific Islander,  7 = Other|Offender's race|
|**disposition**|1 = Guilty Plea, 2 = Nolo Contendere, 3 = Jury Trial, 4 = Trial by Judge or Bench Trial, 5 = Guilty Plea and Trial(>1 count)| Disposition of the case|
|**citizen**|1 = US Citizen, 2 = Not a US Citizen| 
|**state**|State in which defendant was sentenced|US states or District of Columbia|US citizenship|
|**criminal_hist**|0 = No, 1 = Yes|Whether the defendant has any criminal history|
|**drug_type**|0 = No drug charge, 1 = Cocaine, 2 = Crack, 3 = Heroin, 4 = Marijuana, 6 = Methamphetamine, 7 = Fentanyl, 77 = Other| Drug type|
|**case_type**|1 = Felony, 2 = Misdemeanor|Type of case|
|**age**|15 - 105 |Age of defendant at time of sentencing|
|**weapon**|0 = No, 1 = Yes|Whether there is an SOC enhancement for a weapon enhancement or an 18§924 conviction| 
|**presentence_stat**|1 = In custody, 2 = Out on Bail/Bond, 3 = Released on Own Recognizance, 4 = Other|Pre-sentence detention status |
|**gender**|0 = Male, 1 = Female|Offender's gender| 
|**crime_type**|(see code attachment)|Crime type of the primary count| 
|**region**|West, South, Midwest, Northeast|Region in which the defendant was sentenced| 
|**college**|0 = No, 1 = Yes|Whether the defendant has attended at least some college|
|**white**|0 = No, 1 = Yes|Whether the defendant is white| 
|**perc_charged**|0% - 100%|Percentage of state's population that has been convicted of a crime|



**Cleaned and Feature Engineered 2018- 2021 Population Data**


|Feature|Type|Description|
|---|---|---|
|state| object |Name of each state in U.S., as well as Washington D.C| 
| 2018 | int |2018 state population| 
| 2019 | int |2019 state population| 
| 2020 | int |2020 state population| 
| 2021 | int |2021 state population| 
| average | float |Average state population| 
| 2020_pop | int |2020 state population| 
| 2020_whitepop | int |Number of residents of state the 2020 Census determined to be 100% white| 
| 2020_white_per | float |Percentage of state that is 100% white in 2020| 
| 2020_minority_per | float |Percentage of state that is not white in 2020| 
|conv_18to21 |int|Number of federal convictions in each state, 2018 to 2021| 
| conv_per100K | float |Number of federal convictions from 2018 to 2021 per state per 100,000 residents of state as of 2020| 
| conv_white_per | float | Percentage of people who were convicted in a federal court in a state, 2018 to 2021, whom the USCC determined to be white| 
| conv_minority_per | float | Percentage of people who were convicted in a federal court in a state, 2018 to 2021, whom the USCC determined to not be white| 
| by_white_pop | float |The difference between the percentage of a state population that is 100% white in 2020 and the percentage of individuals convicted in federal court in that state from 2018-2021 whom the USS determined to be white| 
| by_minority_pop | float |The difference between the percentage of a state population that is not white in 2020 and the percentage of individuals convicted in federal court in that state from 2018-2021 whom the USS determined not to be white| 


---

## Data Analysis


---

## Conclusion and Recommendations


