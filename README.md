# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 4: Incarceration

### Overview

The U.S. Sentencing Commission keeps a comprehensive array of data regarding federal crime and sentencing for each year. This data includes information for each case with details related to
offense committed, defendant demographic, sentencing guidelines, location, and sentencing outcome, among other things. The commission uses this information to conduct analyses and to establish sentencing practices for federal courts. If you want to explore this further, click [here](https://www.ussc.gov/research/datafiles/commission-datafiles). The years 2018-2021 were selected as the commission amended its data formats in 2018, making the post-2017 data difficult to reconcile with the previous data.

Sentencing guidelines take into account seriousness of the offense and offender’s criminal history. Each type of crime is assigned a base offense level and is assigned specific offense characteristics that increase or decrease the base. If you want to learn more, click [here](https://www.ussc.gov/sites/default/files/pdf/about/overview/Overview_Federal_Sentencing_Guidelines.pdf).

The Sentencing Commission has itself conducted similar studies in the past. [Here](https://www.ussc.gov/sites/default/files/pdf/research-and-publications/research-publications/2010/20100311_Multivariate_Regression_Analysis_Report.pdf) is a study on demographic differences in federal sentencing practices from 2010, and [here](https://www.ussc.gov/sites/default/files/pdf/research-and-publications/research-publications/2017/20171114_Demographics.pdf) is a report from 2017. The structure of modeling and analysis differs significantly from that of the two cited studies, but the studies did provide a frame of reference through which we were able to assess our findings.

### Problem Statement

The United States Sentencing Commission engaged the team to analyze sentencing data for the years 2018-2021 to identify patterns and provide recommendations for future sentence practices, and to provide areas of focus moving forward. We will analyze the impact of variables relating to offender demographics, details of offense and trial proceedings on the sentencing outcomes of federal cases for this period. 

---

## Table of Contents

|Notebook & Content|Description|
|---|---|
|**README**|Overview, Background, Problem Statement, Datasets and Dictionaries, Overview of Data Analysis, Conclusions/ Recommendations| 
|**EDA, Cleaning, Imputing, & Feature Engineering**|Data Cleaning and Analysis| 
|**Visualizations**|Further Data Analysis with Graphics| 
|**Incarceration.pdf**|Sentencing Lengths Presentation Slides|
|**Tableau**|Data Dashboard [here](https://public.tableau.com/app/profile/nicole.anigbogu/viz/Incarceration_16521907161480/PresentationDashboard?publish=yes)|
|**final_model**|Best Model (Lasso) and Coefficient Analysis|
|**Streamlit App**|Live Sentence Length Predictions [here](https://share.streamlit.io/nanigbogu/incarceration/main/app.py)|


### Datasets

* [`df18to21H.csv`](../data/df18to21H.csv): Raw 2018 to 2021 Sentencing Commission Data 
* [`df18to21_cleanedH.csv`](../data/df18to21_cleanedH.csv): Cleaned, Imputed, Feature Engineered 2018 to 2021 Sentencing Commission Data
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
|**race**|0 = Info not available, 1 = White/Caucasian, 2 = Black/African American, 3 = American Indian/Alaskan Native, 4 = Asian or Pacific Islander,  7 = Other|Offender's race|
|**disposition**|1 = Guilty Plea, 2 = No Contest, 3 = Jury Trial, 4 = Trial by Judge or Bench Trial, 5 = Guilty Plea and Trial(>1 count)| Disposition of the case|
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
The sentencing data was collected from the U.S. Sentencing Commission's [website](https://www.ussc.gov/research/datafiles/commission-datafiles), in the form of an SAS file. Each year's file was converted to a csv file, which was read in to the workbooks via Pandas. With the sentencing data read in, with the desired columns kept, all life sentences or sentences longer than 70 years, were capped at 70 years (840 months) to allow for more coherent analysis and computation. 

Additional columns dropped upon further analysis. Sentencing data from 2017 had been included in the 2018 files on the U.S. Sentencing commission's website. These items were removed. Columns were renamed. Some of the race classes were consolidated.  Citizen, education (whether or not an offender had attended any college) and dependents (whether or not an offender had children) columns binarized. Court district identifiers were replaced with the appropriate state, and region variable added. 

Furthermore, the below criteria was used to impute missing values:

* 'age' - impute with mean
* 'criminal_hist' - impute with mode (yes)
* 'case_type' - impute with mode (felony)
* 'gender' - impute with mode (male)
* 'guideline_range' - impute with 0 (no deviation from guideline)
* 'guideline_var_pct' - impute with 0 (no deviation from guideline)
* 'drug_type' - impute with 0 (no drugs present)
* 'presentence_stat' - impute with 1 (in-custody for trial)

The data from the U.S. 2020 Census was downloaded in CSV form from the census [website](https://data.census.gov/cedsci/table?q=race%20states&tid=DECENNIALPL2020.P3) and read into the workbooks via Pandas. Additional columns were created using this data to calculate the percentage of a given state's population is White, as well as number in convictions in the state over the 4-year period per 100K residents (per 2020 Census).

In addition to the previously cited Pandas, sklearn and pickle were used for model construction and deployment. 

---

## Conclusion and Recommendations

We anticipated large variance in sentence length based on race. Largest impact on sentence length :
- Crime Types, Plea Deal/Trial, Possession or Use of Firearm when committing crime
- Midwestern, Southern vs. Northeast, West Coast States

Recommendations for U.S. Sentencing Commission, DOJ 
- Review of geographic variance
- Review of gender disparity 
- Ensure adequate legal counsel
- Address recidivism

Further Research
- Adding presiding judge, acting prosecutor to dataset to try to identify patterns in individual judge's sentencing practices, and individual prosecutor's plea data, that might provide additional explanation of the variance in sentencing length. The way certain judges apply guidelines and schedules may provide a source of bias not previously identified within the data.
