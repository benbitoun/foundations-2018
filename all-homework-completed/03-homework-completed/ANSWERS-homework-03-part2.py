# 1) Let's say we are terrible doctors and we have a patient. Define a dictionary called patient that works with the following code.

patient = {
  'name': 'Catbird',
  'complaint': 'shortness of breath'
} 
print("Doctor, it looks like the patient named", patient['name'], "is complaining about", patient['complaint'])
 
# 2) We aren't really listening to their complaint, but as more test results come in, we'll add these things to the patient's record. Add the following to the patient dictionary:

#     Heart rate: 70
#     Temperature: 98.6
#     Infection: No

# Notice that we're using False instead of "No" - it's because then if we need
# to we can use
#   if patient['infection']:
# instead of
#   if patient['infection'] == "No":

patient['heart_rate'] = 70
patient['temp'] = 98.6
patient['infection'] = False

# Do *not* create a new dictionary - each one of these should be added to the existing dictionary on a separate line.

# 3) Now let's be doctors! Diagnose the patient, and store your diagnosis in a key called 'diagnosis':

# * If their temperature is above 102 but they do not have an infection, they have heat stroke.
# * If they have a temperature above 102 and they have an infection, they have the flu.
# * If they have an infection but a normal temperature, it's probably a cold.
# * If none of the above, tell them to take an aspirin and call you in the morning.

if patient['temp'] > 102 and not patient['infection']:
  patient['diagnosis'] = 'heat stroke'
elif patient['temp'] > 102 and patient['infection']:
  patient['diagnosis'] = 'flu'
elif patient['infection']:
  patient['diagnosis'] = 'cold'
else:
  patient['diagnosis'] = 'take an aspirin and call me in the morning'

print('Your diagnosis is', patient['diagnosis'])

# When you are finished diagnosing the patient, display "Your diagnosis is _______."
 
# 4) Make a list of 3 different patients, each with different complaint, heart rate, temperature, and whether they have an infection or not (this will be a list of dictionaries). Use a for loop to diagnose each of them.

patients = [{
  'name': 'Dogbird',
  'complaint': 'shortness of breath',
  'temp': 103,
  'heart_rate': 30,
  'infection': True
},{
  'name': 'Dogcat',
  'complaint': 'being sleepy',
  'temp': 110,
  'heart_rate': 30,
  'infection': False
},{
  'name': 'Birdbird',
  'complaint': 'dancing too much',
  'temp': 80,
  'heart_rate': 30,
  'infection': True
}]

for patient in patients:
  if patient['temp'] > 102 and not patient['infection']:
    patient['diagnosis'] = 'heat stroke'
  elif patient['temp'] > 102 and patient['infection']:
    patient['diagnosis'] = 'flu'
  elif patient['infection']:
    patient['diagnosis'] = 'cold'
  else:
    patient['diagnosis'] = 'take an aspirin and call me in the morning'

  print('The diagnosis for', patient['name'], 'is', patient['diagnosis'])

