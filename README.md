# Incarceration

|Feature|Type|Dataset|Description|
|---|---|---|---|
|state| object | 2020 U.S. Census | Name of each state in U.S., as well as Washington D.C. | 
| 2020_pop | int | 2020 U.S. Census | 2020 state population. | 
| 2020_whitepop | int | 2020 U.S. Census |Number of residents of state the 2020 Census determined to be 100% white. | 
| 2020_white_per | float |  2020 U.S. Census | Percentage of state that is 100% white, 2020. | 
|conv_18to21 |int| U.S. Sentencing Commission (USCC) (2018-2021) | Number of federal convictions in each state, 2018 to 2021. | 
| conv_per100K | float | Census/USCC | Number of federal convictions from 2018 to 2021 per state per 100,000 residents of state as of 2020. | 
| conv_white_per | float | U.S. Sentencing Commission (USCC) (2018-2021) | Percentage of people who were convicted in a federal court in a state, 2018 to 2021, whom the USCC determined to be white.  | 
| by_white_pop | float | Census/USCC |The difference between the percentage of a state population that is 100% white in 2020 and the percentage of individuals convicted in federal court in that state from 2018-2021 whom the USS determined to be white. | 

Year
State
Age
Gender

U.S. Citizen
Yes (1) - Defendant is a U.S. citizen.
No (0) - Defendant is not a U.S. citizen.

Dependents
Yes (1) - Defendant has dependents whom they support.
No (0) - Defendant does not have any dependents whom they support.

Some College
Yes (1) – Attended some college, or is college graudate.
No (0) – Did not attend any college.

Criminal History
Yes (1) – Indicates defendant has been arrested or incarcerated previously. 
No(0) – Indicates defendant has not been arrested prior.

Disposition
Guilty Plea (1) – Defendant has plead guilty to charge(s). No trial.
No Contest (2) – Special case in which prosecutor proceeds as if there has been a Guilty Plea, with no admission of guilt from defendant.
Jury Trial (3) – Defendant tried before a jury.
Judge Trial (4) – Defendant tried before a judge.
Guilty Plea and Trial (5) – Special case in which a trial is convened, and a guilty plea is also entered at some point in the proceedings.


Presentence Status
In Custody – Trial/plea and sentencing proceeds with defendant in federal custody.
On Bail – Trial/plea proceeds with the defendant released from custody, with cash or bond pledged to the court.
Released on Recognizance – Defendant is released from custody without cash or bond pledged to the court.

Crime Type
Type of Crime Carrying the Largest Minimum Sentence

Drug Type
Type of Drug for which the associated charge will incur the highest penalty

Weapon
Yes (1) – Defendant used or carried a firearm during the carrying out of the crime with which they are charged.
No (0) – Defendant did not use or carry a firearm during the carrying out of the crime with which they are charged.

Sentence type
0 – No Prison
1 – Prison Only
2 – Prison + Alternatives
3 – Probation + Alternatives
4- Probation Only

Imprisoned
0 – Not sentenced to prison
1 – Sentenced to Prison

Count Convictions – number of convictions

Race

Case type:
1 – Felony
2 – Misdemeanor A
3 – Misdemeanor B
