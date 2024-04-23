#!/usr/bin/python3

"""

"""

# import cgitb
# cgitb.enable(format="html")

import cgi
import projects
import _tpl

form = cgi.FieldStorage()
proj_id = form.getfirst('proj','none')

next_id = ''
prev_id = ''
for i in range(len(projects.PROJECTS)):
    if projects.PROJECTS[i] == proj_id:
        next_id = projects.PROJECTS[i-1]      # якщо індекс буде -1, то це буде останній ел-нт

        if i == len(projects.PROJECTS)-1:     # а тут треба перевіряти вихід за межі останнього ел-нта
            prev_id = projects.PROJECTS[0]    # і призначати перший, якщо так
        else:
            prev_id = projects.PROJECTS[i+1]
        break

_tpl.set_tpl_dir(['/home/lex/web/different.com.ua/public_html/_tpl/',])

tpl_vars = dict(
    NEXT = next_id,
    PREV = prev_id,
)

print('Content-Type: text/html; charset=utf-8\n')
print(_tpl.render('arrows_navigation.htm', tpl_vars))
