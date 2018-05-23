from bs4 import BeautifulSoup
# soup = BeautifulSoup(open('./html/test.html'))
# print(soup.prettify())

# Tag
# print(soup.title)

# string
# print(soup.a.string)

# comment
'''
print(type(soup.title.string))
print(type(soup.a.string))
'''

'''
<class 'bs4.element.NavigableString'>
<class 'bs4.element.Comment'>
'''

import sqlite3

conn = sqlite3.connect('./db/test.db')
create_sql = 'create table company(id int primary key not null, emp_name text not null);'
conn.execute(create_sql)
insert_sql = 'insert into company values(?, ?)'
conn.execute(insert_sql, (100, 'LY'))
conn.execute(insert_sql, (200, 'July'))
cursors = conn.execute('select id, emp_name from company')
for row in cursors:
    print(row[0], row[1])
conn.close()
