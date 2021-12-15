def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

AccountType = enum('BLANK', 'MEMBER', 'COACH', 'ADMIN')