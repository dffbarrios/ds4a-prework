
print(1675 - 886)


x = 1675
y = 886
z = x - y
print(z)


name = "John"
print(name)


a = 65.4
b = 7
c = 6
d = 2
result = a + b - c + d
print(result)



x = 4
print(x)
y = 2
x = y + x
print(x)



x = 2
y = 3
print (x + y ** x)
print((x+y)**x)



a = 3
b = 4
c = 5

print(c**2)
print(a**2 + b**2)



# Lines that start with the `#` symbol are comments, and are ignored by Python completely
# They only exist to make your code more readable for humans
# It's good practice to have one or more comments above non-obvious parts of code 
# to explain what they do

# Data on probability of expansion success by country estimates
success_estimates = {
    'Australia': [0.6, 0.33, 0.11, 0.14],
    'France': [0.66, 0.78, 0.98, 0.2],
    'Italy': [0.6],
    'Brazil': [0.22, 0.22, 0.43],
    'USA': [0.2, 0.5, 0.3],
    'England': [0.45],
    'Canada': [0.25, 0.3],
    'Argentina': [0.22],
    'Greece': [0.45, 0.66, 0.75, 0.99, 0.15, 0.66],
    'Morocco': [0.29],
    'Tunisia': [0.68, 0.56],
    'Egypt': [0.99],
    'Jamaica': [0.61, 0.65, 0.71],
    'Switzerland': [0.73, 0.86, 0.84, 0.51, 0.99],
    'Germany': [0.45, 0.49, 0.36]
}

#no quotations marks needed when printing an existing variable
print(success_estimates)

# Look at the keys...
success_estimates.keys()


# now let's look at the keys in list form. This is more legible and usable for us later on.
list(success_estimates.keys())

# We can also see the corresponding values (estimates) for each key as follows
list(success_estimates.values())


print('Checking if Morocco key is present:')
print('Morocco' in success_estimates) # print the VALUE of "Morocco in success_estimates"

print('Checking if Japan key is present:')
japan_boolean = 'Japan' in success_estimates
print(japan_boolean)



success_estimates['Jamaica']


jamaica_list = success_estimates['Jamaica'] 

print(jamaica_list)


# Each successive print statement will print on a new line
print(jamaica_list[0]) # prints the first element of the list
print(jamaica_list[1]) # prints the second element of the list
print(jamaica_list[2]) # prints the third element of the list



# taking the last 2 elements of jamaica_list
print(jamaica_list[-2:])  # (go from the second last element until the end)
print(jamaica_list[1:])  # (go from the secon d element until the end)



# multi-layered slicing
print(success_estimates['Jamaica'][0]) # getting the first jamaican estimate from the dictionary


len(jamaica_list) # returns the length of the list


print('Number of estimates for France:')
print(len(success_estimates['France']))

print('Number of estimates for Greece:')
print(len(success_estimates['Greece']))

print('Number of estimates for Morocco:')
print(len(success_estimates['Morocco']))



avg_jamaica = (0.61 + 0.65 + 0.71) / 3
print(avg_jamaica)



country_name = 'Jamaica'
jamaica_list = success_estimates[country_name] # list of the estimates for Jamaica
print(jamaica_list)


avg_jamaica = sum(jamaica_list) / len(jamaica_list)
min_jamaica = min(jamaica_list)
max_jamaica = max(jamaica_list)
print("Country:",country_name,", Average:",avg_jamaica)
print("Country:",country_name,", Min:",min_jamaica)
print("Country:",country_name,", Max:",max_jamaica)



avg_jamaica = round(sum(jamaica_list) / len(jamaica_list),2)
min_jamaica = round(min(jamaica_list),2)
max_jamaica = round(max(jamaica_list),2)
print("Country:",country_name,", Average:",avg_jamaica)
print("Country:",country_name,", Min:",min_jamaica)
print("Country:",country_name,", Max:",max_jamaica)



# One possible solution
print("Country:",'France',", Average:",sum(success_estimates['France']) / len(success_estimates['France']))
print("Country:",'Brazil',", Average:",sum(success_estimates['Brazil']) / len(success_estimates['Brazil']))
print("Country:",'Argentina',", Average:",sum(success_estimates['Argentina']) / len(success_estimates['Argentina']))
print("Country:",'Germany',", Average:",sum(success_estimates['Germany']) / len(success_estimates['Germany']))
print("Country:",'Australia',", Average:",sum(success_estimates['Australia']) / len(success_estimates['Australia']))
print("Country:",'Canada',", Average:",sum(success_estimates['Canada']) / len(success_estimates['Canada']))
print("Country:",'Greece',", Average:",sum(success_estimates['Greece']) / len(success_estimates['Greece']))
print("Country:",'USA',", Average:",sum(success_estimates['USA']) / len(success_estimates['USA']))
print("Country:",'Switzerland',", Average:",sum(success_estimates['Switzerland']) / len(success_estimates['Switzerland']))
print("Country:",'Tunisia',", Average:",sum(success_estimates['Tunisia']) /len(success_estimates['Tunisia']))
print("Country:",'Italy',", Average:",sum(success_estimates['Italy']) / len(success_estimates['Italy']))
print("Country:",'Egypt',", Average:",sum(success_estimates['Egypt']) / len(success_estimates['Egypt']))
print("Country:",'Jamaica',", Average:",sum(success_estimates['Jamaica']) / len(success_estimates['Jamaica']))
print("Country:",'Morocco',", Average:",sum(success_estimates['Morocco']) / len(success_estimates['Morocco']))
print("Country:",'England',", Average:",sum(success_estimates['England']) / len(success_estimates['England']))




# Get all the keys from the success_estimates dictionary
country_name_list = list(success_estimates.keys())
print(country_name_list)



# Loop through all countries and calculate their mean success estimate
for i in country_name_list:
    print('--Begin one iteration of loop--')
    print('Element of country_name_list, placeholder i = ' + i)
    print('Access value from dict success_estimates[i]: ', success_estimates[i])
    print('Average of list from success_estimates[i]: ', sum(success_estimates[i]) / len(success_estimates[i]))
    print('--Go to next iteration of loop--')
    print()



    for country in country_name_list:
        print('Country',country,', Min: ', min(success_estimates[country]))
        print('Country',country,', Max: ', max(success_estimates[country]))



    for country in country_name_list:
        country_range = max(success_estimates[country]) - min(success_estimates[country])
        print('Country: ', country, ", Range: ", country_range)



    key_name_list = [i for i in success_estimates] # loop over each item i in success_estimates and put i in the list
    key_name_list


    value_name_list = [success_estimates[country] for country in success_estimates] # loop over each item in success_estimates and put success_estimates[i] in the list
    value_name_list


    # Number of estimates available for each country
    [[i, len(success_estimates[i])] for i in success_estimates]


# One possible solution
sum_squares_list = [[i, sum([j**2 for j in success_estimates[i]])] for i in success_estimates]
sum_squares_list


# One possible solution
removed_mean_list = [[i, [round(j - sum(success_estimates[i])/len(success_estimates[i]),2) for j in success_estimates[i]]] for i in success_estimates]
removed_mean_list


italy = success_estimates['Italy']
jamaica = success_estimates['Jamaica']

print(len(italy) > 1)
print(len(jamaica) > 1)



if len(italy) > 1:
    print("Italy has more than 1 estimate")

if len(jamaica) > 1:
    print("Jamaica has more than 1 estimate")



# **Incorrect logic warning**
if len(italy) > 0:
    print("Italy has more than 0 estimates")
elif len(jamaica) > 0:
    print("Jamaica has more than 0 estimates")
else:
    print("this will only execute if neither of the above lines do")




    # Get a list of all the country names
country_name_list = list(success_estimates.keys())

# Create an empty dictionary to hold country mean estimates
country_means = {}

# Loop through all countries and calculate their mean success estimate
for i in country_name_list:
    list_country_estimates = success_estimates[i] # list of estimates for a country

# if more than one country estimate, then record the mean estimate, otherwise go to next loop iteration
if len(success_estimates[i]) > 1:
    print("adding the mean for",i)
    country_mean_value = sum(list_country_estimates) / len(list_country_estimates)
    country_means[i] =  country_mean_value # insert country mean value into dict using country name as key
else:
    print("....skipping", i)


# Nicely format the result for printing to the screen
for country_key in country_means: 
    print("Country: {0:s}, Avg Success Estimate: {1:.2f}".format(country_key, country_means[country_key]))


# Get a list of all the country names
country_name_list = list(success_estimates.keys())

# Create an empty dictionary to hold country mean estimates
country_means = {}

# Loop through all countries and calculate their mean success estimate
for i in country_name_list:
    list_country_estimates = success_estimates[i] # list of estimates for a country



# if more than one country estimate, then record the mean estimate, otherwise go to next loop iteration
if len(success_estimates[i]) > 2:
    country_mean_value = sum(list_country_estimates) / len(list_country_estimates)
    country_means[i] =  country_mean_value # insert country mean value into dict using country name as key
    print("Country: {0:s}, Avg Success Estimate: {1:.2f}".format(i, country_mean_value))
else:
    print("Country: {0:s}, *Does not Meet Company Policy*".format(i))



for country in success_estimates:
    largest_estimate = max(success_estimates[country])
    smallest_estimate = min(success_estimates[country])

rnge = largest_estimate - smallest_estimate
if rnge > 0.6:
    print(country, "Flagged because of range ", rnge)
    print(success_estimates[country])


country_name_list = list(success_estimates.keys())
for i in country_name_list:
    min_stat = min(success_estimates[i])
    mean_stat = sum(success_estimates[i]) / len(success_estimates[i])
    max_stat = max(success_estimates[i])
    len_stat = len(success_estimates[i])
    meets_policy = len_stat > 2
    print('Country:',i,', Min:',min_stat,', Average:',mean_stat,', Max:',max_stat,', NumEst:',len_stat,', MeetsPolicy:',meets_policy)


country_name_list = list(success_estimates.keys())

best_mean = 0
best_country = None

for i in country_name_list:
    min_stat = min(success_estimates[i])
    mean_stat = sum(success_estimates[i]) / len(success_estimates[i])
    max_stat = max(success_estimates[i])
    len_stat = len(success_estimates[i])
    meets_policy = len_stat > 2
    
    if mean_stat > best_mean:
        if meets_policy:
            best_mean = mean_stat
            best_country = i
        
print("The country with the highest mean was", best_country, "with a mean of", best_mean)



country_name_list = list(success_estimates.keys())

highest_minimum = 0
safest_country = None

for i in country_name_list:
    min_stat = min(success_estimates[i])
    mean_stat = sum(success_estimates[i]) / len(success_estimates[i])
    max_stat = max(success_estimates[i])
    len_stat = len(success_estimates[i])
    meets_policy = len_stat > 2
    
    if min_stat > highest_minimum and meets_policy:
        highest_minimum = min_stat
        safest_country = i
        
print(safest_country, "is the conservative choice", "with a minimum estimate of", highest_minimum)