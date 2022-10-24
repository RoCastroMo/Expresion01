fname = "Rodolfo"
lname = "Castro"
name = fname + ' ' + lname


def abbrev_name( name ):
    last = name.split()
    first = last[0]
    las = last[1]
    return f'{first[0].upper()}.{las[0].upper()}'


print(abbrev_name(name))
