#!/usr/bin/python3

"""

"""

# import cgitb
# cgitb.enable(format="html")

import projects
import _tpl

_tpl.set_tpl_dir(['/home/lex/web/different.com.ua/public_html/_tpl/',])

all_proj = ''
for proj in projects.PROJECTS:
    tpl_vars = dict(
        ID = proj,
    )
    all_proj += _tpl.render('select_list.htm', tpl_vars)


print('Content-Type: text/html; charset=utf-8\n')
print(all_proj)
