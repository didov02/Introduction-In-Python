import re;

def matcher(regex, string):
    match = re.search(regex, string)
    if match is None:
        return string
    start, end = match.span()
    return f'{string[:start]}({string[start:end]}){string[end:]}'

print(matcher('o+', 'Goooooogle')) # 'G(oooooo)gle -> повече от един символ
print(matcher('[hH]o+','Hohohoho...')) # '(Ho)hohoho...'  -> един от всички сивмоли
print(matcher('([hH]o)+','Hohohoho...')) # '(Hohohoho)...' -> група
print(matcher('([hH]o){2,3}','Hohohoho...')) # '(Hohoho)ho...' -> група от 2 до 3 пъти

print(matcher('[hH]o+','Hoooooohohooo...')) # '(Hoooooo)hohooo...' 
print(matcher('[hH]o+?','Hoooooohohooo...')) # '(Ho)ooooohohooo...' -> non-gready

print(matcher('day|nice','A nice dance-day.')) # 'A (nice) dance-day.' -> или за думи
print(matcher('da(y|n)ce','A nice dance-day.')) # 'A nice (dance)-day.' -> или в дума
print(matcher('da(y|nce)','A nice dance-day.')) # 'A nice (dance)-day.'

print(matcher('[aeoui]', 'Google')) # 'G(o)ogle' -> един от всички символи
print(matcher('[^CBL][aeoui]','Cobol')) # 'Co(bo)l' -> отрицание

print(matcher('[0-9]{1,3}-[a-z]','Figure 42-b')) # 'Figure (42-b)' -> диапазон
print(matcher('[^a-zA-Z-]','Figure-42-b')) # 'Figure-(4)2-b' -> диапазон с отрицание

print(matcher(r'\d+', 'Phone number: 5551234')) # 'Phone number: (5551234)' -> число
print(matcher(r'\w+', 'Phone number: 5551234')) # '(Phone) number: 5551234' -> число или буква
print(matcher(r'\s+', 'Phone number: 5551234')) # 'Phone( )number: 5551234' -> спейс

print(matcher(r'(\w+).*\1', 'Matches str if str repeats one of its words.')) # 'M(atches str if str repeat)s one of its words.'
print(matcher(r'(\b\w+\b).*\1', 'Matches str if str repeats one of its words.')) # 'Matches (str if str) repeats one of its words.'

print(re.search(r'(\w+) \d', 'The 4 Horsemen of the Apocalypse').group()) # 'The 4'
print(re.search(r'(\w+) \d', 'The 4 Horsemen of the Apocalypse').groups()) # ('The',)

print(re.search(r'(?:\w+) \d', 'The 4 Horsemen of the Apocalypse').group()) # 'The 4' -> групи без да са групи
print(re.search(r'(?:\w+) \d', 'The 4 Horsemen of the Apocalypse').groups()) # () -> групи без да са групи

print(re.search(r'\w+\s*(?P<number_of_horses>\d)\s*\w+', 'The 4 Horsemen of the Apocalypse').group()) # 'The 4 Horsemen' -> именувани групи
print(re.search(r'\w+\s*(?P<number_of_horses>\d)\s*\w+', 'The 4 Horsemen of the Apocalypse').groups()) # ('4',) -> именувани групи

print(re.search(r'\w+\s*(?P<number_of_horses>\d)\s*\w+', 'The 4 Horsemen of the Apocalypse').groupdict()) # {'number_of_horses': '4'} -> именувани групи
print(re.search(r'\w+\s*(?P<number_of_horses>\d)\s*\w+', 'The 4 Horsemen of the Apocalypse').group('number_of_horses')) # '4' -> именувани групи

print(re.search(r'[Tt]he', 'The 4 Horsemen of the Apocalypse').group()) # 'The' -> look-ahead
print(re.search(r'[Tt]he(?=\s*Apocalypse)', 'The 4 Horsemen of the Apocalypse').group()) # 'the' -> look-ahead

print(re.search(r'[Tt]he', 'The 4 Horsemen of the Apocalypse').group()) # 'The' -> negative look-ahead
print(re.search(r'[Tt]he(?!\s*4)', 'The 4 Horsemen of the Apocalypse').group()) # 'the' -> negative look-ahead

print(re.search(r'[Tt]he', 'The 4 Horsemen of the Apocalypse').group()) # 'The' -> look-behind
print(re.search(r'(?<=\s)[Tt]he', 'The 4 Horsemen of the Apocalypse').group()) # 'the' -> look-behind

