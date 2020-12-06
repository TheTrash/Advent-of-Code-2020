import re
f = open('input.txt', 'r').read().replace("\n"," ").split('  ')

count = 0
rules = {'byr': re.compile(r'byr:(\d{4})(\s|$)'),
         'iyr': re.compile(r'iyr:(\d{4})(\s|$)'),
         'eyr': re.compile(r'eyr:(\d{4})(\s|$)'),
         
         'hgt': re.compile(r'hgt:(\d+)(cm|in)(\s|$)'),
         'hcl': re.compile(r'hcl:#[0-9a-f]{6}(\s|$)'),
         'ecl': re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)'),
         'pid': re.compile(r'pid:\d{9}(\s|$)')
         }
for form in f:
    try:
        byr = re.findall(rules['byr'], form)[0][0]
        assert(1920 <= int(byr) <= 2002)

        iyr = re.findall(rules['iyr'], form)[0][0]
        assert(2010 <= int(iyr) <= 2020)

        eyr = re.findall(rules['eyr'], form)[0][0]
        assert(2020 <= int(eyr) <= 2030)
        
        hgt, units , _ = re.findall(rules['hgt'], form)[0]
        if units=='cm':
            assert(150 <= int(hgt) <= 193)
        else:
            assert(59 <= int(hgt) <= 76)

        hcl = re.findall(rules['hcl'], form)[0]
        assert(hcl is not None)

        ecl = re.findall(rules['ecl'], form)[0]
        assert(ecl is not None)

        pid = re.findall(rules['pid'], form)[0]
        assert(pid is not None)
        
        count += 1
    except (IndexError, AssertionError) as err:
        print(err)
print(count)