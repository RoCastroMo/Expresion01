def rental_car_cost(d):
    rent = 40
    if d == 1:
        return rent
    if d >= 7:
        rent *= d
        result2 = rent - 50
        return result2
    if d >= 3:
        rent *= d
        result1 = rent - 20
        return result1


print(rental_car_cost(1))
print(rental_car_cost(4))
print(rental_car_cost(7))
print(rental_car_cost(8))


def get_age(age):
    age2 = f'{int(age)} years old'
    return age2