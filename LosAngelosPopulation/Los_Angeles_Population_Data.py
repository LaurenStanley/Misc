import pandas as pd

tract_locations = 'Census_Tract_Locations__LA_.csv'
data_file = 'County_of_Los_Angeles_Estimated_Population_by_Census_Tract__City_Name__Ethnicity__Gender___Age_Group__CY_2016.csv'

#Read the data from the CSV files and import into a pandas data frame
data = pd.read_csv(data_file)
tracts = pd.read_csv(tract_locations)

#Drop the age columms
data = data.drop(columns=['Age_0_15','Age_16_18','Age_19_20','Age_21_25','Age_26_59','Age_60_64','Age_65up']
)
#Add the male and female columns to get estimated total population
total_population = data['Female'] + data['Male']
data['Total_Population'] = total_population

#Print data frames
#print(data)
#print(tracts)

#Merge data frames using the tract ID
merged_data = pd.merge(data,tracts, left_on = 'Census_Tract',right_on = 'Tract Number')
merged_data.set_index('Census_Tract', inplace = True)

#Print merged data frame an save to new CSV
print(merged_data)
merged_data.to_csv('Los_Angeles_Aggregate_Tract_Data.csv')