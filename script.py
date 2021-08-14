# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def damages_updater(damages_data):
    
    multiplier = {"M":1000000, "B":1000000000}
    damages_new = []
    
    for storm_damage in damages_data:
        
        if storm_damage == "Damages not recorded":
            damages_new.append(storm_damage)
        else:
            damages_new.append(int(float(storm_damage[:-1]) * multiplier[storm_damage[-1]]))

    return damages_new

#testing function
damages_updated = damages_updater(damages)



# write your construct hurricane dictionary function here:

def hurricane_dict(names_data, month_data, year_data, max_wind_data, areas_data, damage_data, death_data):
    
    hurricane_data = {}
    i = 0
    for name in names_data:
        storm_to_add = {}
        storm_to_add["Name"] = name
        storm_to_add["Month"] = month_data[i]
        storm_to_add["Year"] = year_data[i]
        storm_to_add["Max Sustained Wind"] = max_wind_data[i]
        storm_to_add["Areas Affected"] = areas_data[i]
        storm_to_add["Damage"] = damage_data[i]
        storm_to_add["Deaths"] = death_data[i]
        hurricane_data[name] = storm_to_add
        i += 1
    
    return hurricane_data

storm_data = hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths)

# write your construct hurricane by year dictionary function here:

def storm_by_year(storm_dict):
    
    year_list = []
    for storm in storm_dict:
        if storm_dict[storm]["Year"] not in year_list:
            year_list.append(storm_dict[storm]["Year"])
    
    storm_by_year_dict = {}
    
    for year in year_list:
        storm_in_year = []
        for storm in storm_dict:
            if storm_dict[storm]["Year"] == year:
                storm_in_year.append(storm_dict[storm])
        storm_by_year_dict[year] = storm_in_year
    
    return storm_by_year_dict

annual_data = storm_by_year(storm_data)  

# write your count affected areas function here:

def storm_occurence_by_area(storm_dict):
    
    area_dict = {}
    for storm in storm_dict:
        for area in storm_dict[storm]["Areas Affected"]:
            if area not in area_dict:
                area_dict[area] = 1
            else:
                area_dict[area] += 1
                
    return area_dict

area_count = storm_occurence_by_area(storm_data)

#print(area_count)


# write your find most affected area function here:
    
def most_affected(storm_dict):
    
    area_affected_data = storm_occurence_by_area(storm_dict)
    max_affected = 0
    
    for area in area_affected_data:
        if area_affected_data[area] > max_affected:
            max_affected = area_affected_data[area]
            max_area = area
    
    print("The most affected area by Cat 5 hurricanes is {area}, which has been hit {max_affected} times.".format(area=max_area, max_affected=max_affected))
    
    return max_area, max_affected

max_area, max_affected = most_affected(storm_data)


# write your greatest number of deaths function here:

def most_deaths(storm_dict):
    
    max_deaths = 0
    for storm in storm_dict:
        if storm_dict[storm]["Deaths"] > max_deaths:
            max_deaths = storm_dict[storm]["Deaths"]
            max_deaths_storm = storm
    
    print("The deadliest Cat 5 storm on record is {storm} with {death_num} deaths.".format(storm=max_deaths_storm, death_num=max_deaths))
    
    return max_deaths_storm, max_deaths

most_deaths(storm_data)

# write your catgeorize by mortality function here:


def storms_by_mortality(storm_dict):
    
    mortality_dict = {1:[], 2:[], 3:[], 4:[], 5:[]}
    
    for storm in storm_dict:
        death_ct = storm_dict[storm]["Deaths"]  
        if death_ct > 0 and death_ct <= 100:
            mortality_dict[1].append(storm_dict[storm])
        elif death_ct > 100 and death_ct <= 500:
            mortality_dict[2].append(storm_dict[storm])
        elif death_ct > 500 and death_ct <=1000:
            mortality_dict[3].append(storm_dict[storm])   
        elif death_ct > 1000 and death_ct <=10000:
            mortality_dict[4].append(storm_dict[storm])
        else:
            mortality_dict[5].append(storm_dict[storm])

    return mortality_dict

mort_sort = storms_by_mortality(storm_data)

# write your greatest damage function here:

def most_damage(storm_dict):
    
    max_damage = 0
    for storm in storm_dict:
        try:
            if storm_dict[storm]["Damage"] > max_damage:
                max_damage = storm_dict[storm]["Damage"]
                max_damage_storm = storm
        except TypeError:
            continue
    print("The most damaging Cat 5 storm on record is {storm} which cost {damage_num} dollars.".format(storm=max_damage_storm, damage_num=max_damage))
    
    return max_damage_storm, max_damage

most_damage(storm_data)

# write your catgeorize by damage function here:

def storms_by_damage(storm_dict):
    
    damage_dict = {1:[], 2:[], 3:[], 4:[], 5:[]}
    
    for storm in storm_dict:
        damage_num = storm_dict[storm]["Damage"]  
        try:
            if damage_num > 0 and damage_num <= 100000000:
                damage_dict[1].append(storm_dict[storm])
            elif damage_num > 100000000 and damage_num <= 1000000000:
                damage_dict[2].append(storm_dict[storm])
            elif damage_num > 1000000000 and damage_num <=10000000000:
                damage_dict[3].append(storm_dict[storm])   
            elif damage_num > 10000000000 and damage_num <=50000000000:
                damage_dict[4].append(storm_dict[storm])
            else:
                damage_dict[5].append(storm_dict[storm])
        except TypeError:
            continue
        
    return damage_dict

damage_storm = storms_by_damage(storm_data)