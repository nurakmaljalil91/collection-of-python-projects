def guest_list(guests):
    for (x, y, z) in range(0, len(guests)):
        if guests.isnull().all():
            return None
        else:
            name = x
            age = y
            job = z
            print("{} is {} years old and worsk as {}.".format(name, age, job))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
            ('Amanda', 25, "Engineer")])
