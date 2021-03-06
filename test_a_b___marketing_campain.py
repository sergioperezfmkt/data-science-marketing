# -*- coding: utf-8 -*-
"""test_A/B _ marketing_campain

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QL_l9Or1neIcVnigOm9xl0g42Cg7JS7R
"""

# import packages
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, chi2 

# import data
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name = "campaign_data")
campaign_data.head(2)

# check number of sign-ups
campaign_data.groupby("mailer_type")["signup_flag"].value_counts()

observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values
observed_values

# compute sign-up rate

campaign_data.groupby("mailer_type")["signup_flag"].value_counts()
mailer1_signup_rate = 123 / (252 + 123) 
mailer2_signup_rate = 127 / (209 + 127)


print("mailer1_signup_rate: ", mailer1_signup_rate)
print("mailer2_signup_rate: ", mailer2_signup_rate)
print("")


# state hypotheses & set acceptance criteria
null_hypothesis = "There is no relationship between mailer type and signup rate. They are independent."#tipo de correo

alternate_hypothesis = "There is a relationship between mailer type and signup rate. They are not independent."

acceptance_criteria = 0.05


# calculate expected frequencies & chi square statistic
observed_values = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"]).values

chi2_statistic, p_value, dof, expected_values = chi2_contingency(observed_values, correction = False)

# import chi2_contingency to compute for the chi-square statistics and the p-value for the particular hypothesis test
print("chi2_statistic: ",chi2_statistic)
print("p_value: ",p_value)
print("")
# find the critical value for our test

# import chi2 to find the critical value based on the acceptance criteria
critical_value = chi2.ppf(1 - acceptance_criteria, dof)
print("critical_value: ",critical_value)
print("")

if chi2_statistic >= critical_value:
    print(f"As our chi-square statistic of {chi2_statistic} is higher than our critical value of {critical_value}")
    print(f"we reject the null hypothesis, and conclude that:")
    print(f"{alternate_hypothesis}.")
else:
    print(f"As our chi-square statistic of {chi2_statistic} is lower than our critical value of {critical_value}")
    print(f" we retain the null hypothesis, and conclude that:")
    print (f"{null_hypothesis}.")

if p_value <= acceptance_criteria:
    print(f"As our p_value of {p_value} is lower than our acceptance_criteria of {acceptance_criteria}") 
    print(f"we reject the null hypothesis, and conclude that:")
    print(f"{alternate_hypothesis}.")
else:
    print(f"As our p_value of {p_value} is higher than our acceptance_criteria of {acceptance_criteria}") 
    print(f"we retain the null hypothesis, and conclude that:")
    print(f"{null_hypothesis}.")

"""
The sample problem I had assessed the difference in sign-up rate to the club between two different mailers that were sent. 
And based on the data provided and using the chi-squared test for independence, 
I can now recommend to ABC Grocery and maybe its marketing department that they can stop sending
an expensive looking mailer or even a simple mailer to save costs as it does not 
help in getting customers to sign-up for the delivery club promo."""