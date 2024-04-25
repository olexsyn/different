#!/usr/bin/python3

"""

"""

# import cgitb
# cgitb.enable(format="html")

import cgi
import projects
import _tpl

form = cgi.FieldStorage()
skill = form.getfirst('list','skill')  # 'skill'/'index'

if skill != 'skill':
    skill = 'index'

_tpl.set_tpl_dir(['/home/lex/web/different.com.ua/public_html/_tpl/',])

selected_projects = ''

for proj in projects.PROJECTS:
    selected_projects += _tpl.render(f'{skill}_list.htm', { 'ID': proj })

print('Content-Type: text/html; charset=utf-8\n')
print(selected_projects)
