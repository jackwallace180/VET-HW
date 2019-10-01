from pet import *
from owner import *
from vet import *
from Appointment_vet import *

vet1 = vet('Vishnu', '077', 'vish@spartaglobal.com', 'broken bones')
vet2 = vet('Shariq', '011', 'shar@spartaglobal.com', 'vommitting')
vet3 = vet('Rory', '033', 'RPS@spartaglobal.com', 'coughing')

owner1 = owner('Jack','07738233894','jwallace@spartaglobal.com','visa debit')
owner2 = owner('Shaggy','16','shaggy@scoobydoo.com', 'scooby snacks')
owner3 = owner('Hanz','12349274','hanz@schnitzel.com', 'euros')

pet1 = pet('red', 'viszla',owner1)
pet2 = pet('scooby', 'dog', owner2)
pet3 = pet('schnappi','crocodile', owner3)
pet4 = pet('sonic','hedgehog', owner1)

appointment1 = appointment('broken bones','1/10','£50')
appointment2 = appointment('vommitting','2/10','£20')
appointment3 = appointment('coughing','3/10','£20')
appointment4 = appointment('vommitting','4/10','£20')

appointment1.assign_pet(pet1)
appointment2.assign_pet(pet2)
appointment3.assign_pet(pet3)
appointment4.assign_pet(pet4)

appointment1.assign_vet(vet1)
appointment2.assign_vet(vet2)
appointment3.assign_vet(vet3)
appointment4.assign_vet(vet2)

appointment_list = []

appointment_list.append(appointment1)
appointment_list.append(appointment2)
appointment_list.append(appointment3)
appointment_list.append(appointment4)

print('#Appointment list:')
for list in appointment_list:
    print('Vet name: ' + list.vet.name, ', Pet name: ' + list.pet.name,
          ', injury: ' + list.injury, ', date: ' + list.date, ' , Price: ' + list.price, 'Owner: ' + list.pet.owner.name)
print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

print ('#Pet and owner:')
print(pet1.name + ' is owned by ' + pet1.owner.name)
print(pet2.name + ' is owned by ' + pet2.owner.name)
print(pet3.name + ' is owned by ' + pet3.owner.name)
print(pet4.name + ' is owned by ' + pet4.owner.name)
print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')


print('#Pet details:')
print(pet.pet_details(pet1))
print(pet.pet_details(pet2))
print(pet.pet_details(pet3))
print(pet.pet_details(pet4))
print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')

print('#Owner details:')
print(owner.owner_details(owner1))
print(owner.owner_details(owner2))
print(owner.owner_details(owner3))
print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')


# for appointment in appointment_list:
    # print ('vet :' + appointment.vet, 'pet :' + appointment.pet)

