def timeConversion(s):
    if s[-2] == 'A' and s[0: 2] != '12':
        return s[0: -2]
    elif s[-2] == 'A' and s[0: 2] == '12':
        return '00' + s[2: -2]
    elif s[-2] == 'P' and s[0: 2] == '12':
        return '12' + s[2: -2]
    elif s[-2] == 'P' and s[0: 2] != '12':
        return str(12 + int(s[0: 2])) + s[2: -2]
