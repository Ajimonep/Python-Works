from json import load

f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\jsonWorks\\countries.json",encoding="UTF-8")

items=load(f)


#1 print name of all country

country_names=[i.get("name")for i in items ]

# print(country_names)

#3 print asian countries

asian=[i.get("name") for i in items  if i.get("region")=="Asia"]
# print(asian)

#4 print non independent countries
non_independant=[i.get("name") for i in items if i.get("independent")==False]
# print(non_independant)


#5 print countries with population greater than 400000000
countries_with_polulation=[i.get("name") for i in items if i.get("population")>40000000]
# print(countries_with_polulation)

#6 print countries with border to pakistan
border_with_pakistan=[i.get("name") for i in items  if "PAK" in i.get("borders",[])]
# print(border_with_pakistan)

#7 print countries with timezones UTC+04:30
time_zone = [i.get("name") for i in items if "UTC+04:30" in i.get("timezones", [])]
# print(time_zone)

# 8 english speaking countries
# for c in items:
#     for l in

#9 print countries with calling code 
calling_codes = [(i.get("name"), i.get("callingCodes")) for i in items if i.get("callingCodes")]
# for country, codes in calling_codes:
    # print(f"{country}: {codes}")

#10 print countries with currency name
currency_name = [(i.get("name"), [curr.get("name") for curr in i.get("currencies", [ ])]) for i in items]
# print(currency_name)

# 11 sort countries by name
sorted_countries = sorted(items, key=lambda x: x.get("name"))
# print(sorted_countries)

#12 sort countries by population
sorted_countries_by_population = sorted(items, key=lambda x: x.get("population"))
# print(sorted_countries_by_population)


#13 count languages spoken by countries

languages = {}
for country in items:
    for language in country.get("languages",):
        if language["name"] in languages:
            languages[language["name"]] += 1
        else:
            languages[language["name"]] = 1

# print(languages)

#14 most spoken language
    
key_value=[(v,k) for k,v in languages.items()]
print(max(key_value))


all_region={c.get("region") for c in items}

region_summary={}

for c in items:

    region_name=c.get("region")

    if region_name in region_summary:

        region_summary[region_name]+=c.get("area",0)

    else:
        region_summary[region_name]=c.get("area",0)

# print(region_summary)

value_key=[(v,k) for k,v in region_summary.items()]
# print(max(value_key))

