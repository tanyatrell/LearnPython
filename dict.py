weather = {
'city': 'Moscow', 
'temper': '20', 
'wind': 'ost'
}
print(weather['city'])

weather['temper']='25'
print(weather['temper'])

print(len(weather))
weather.get('country', 'No')
weather['date'] = '27.05.2017'
All_weathers = []
All_weathers.append(weather)

weather2 = {'city': 'Moscow', 'temper': '20', 'wind': 'ost', 'date': '22.10.2017'}
weather3 = {'city': 'Moscow', 'temper': '20', 'wind': 'ost', 'date': '23.10.2017'}
All_weathers.append(weather2)
All_weathers.append(weather3)
print(All_weathers)
