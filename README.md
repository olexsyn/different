# different

Different Site

Для даного сайту сторінка - це окремий проект, а в якості теґів - виступають навички.

## Як створити проект

Проекти розміщені в _**public_html/projects/**_.

### Назва проекту

Для того, щоб додати новий проект необхідно в _**public_html/projects/**_ створити папку з його унікальним іменем (технічною мовою - ідентифікатором), що може складається з маленьких латинських літер, цифр і дефісу `-`.

Наприклад, ми хочемо додати проект під назвою "My New Work". Для цього краще створити таку папку: _**public_html/projects/my-new-work/**_. Не обов’зково, щоб літери точно співпадали з назвою проекта. Папку можна назвати і _**my-new-work-23**_, а також _**235847**_. Але краще, щоб ім’я несло в собі якийсь зрозумілий зміст...

### Файли проекту

В кожній такій папці має бути 4 файли:

```
public_html/projects/my-new-work/data.htm                 - дані проекту (ім’я, заголовок, опис, та ін.)
public_html/projects/my-new-work/index.htm                - головна сторінка-шаблон, яка "підтягує" дані
public_html/projects/my-new-work/my-new-work.jpg          - велике зображення проекту
public_html/projects/my-new-work/my-new-work_preview.jpg  - маленьке зображення (прев’юшка)
```

#### Зображення (jpg)

Файли `.jpg` повинні містити в собі точну назву проекту, тобто унікальної назви папки в якому він знаходиться. До назви маленького зображення додаємо `_preview` перед розширенням.

Великі зображення краще створювати з шириною 580 px. Можна робити і іншого розміру, але це може позначитися на якості, бо в цьому випадку вони будуть масштабовані. Висота великого зображення - довільна. Якщо маємо декілька зображень для проекту - краще об’єднати їх вертикально в одне зображення.

Аналогічно і з прев’юшками. Розмір при якому вони не будуть масштабуватися - 280×170 px. Якщо зберегти відповідні пропорції для усіх зображень - ми отримаємо вирінені по вертикалі і горизонталі клітинки. Якщо пропорцій не дотримуватися - зображення будуть вирівнені лише по колонках.


#### Код (htm)

```
<!--#set var="ID"     value="my-new-work"-->
<!--#set var="TITLE"  value="My New Work"-->
<!--#set var="DESCR"  value='I present to you my new work!'-->
<!--#set var="SKILL"  value="illustration"-->
<!--#set var="SKILL2" value=""-->
<!--#set var="SKILL3" value=""-->
<!--#set var="PREV"   value="vogue-cover"-->
<!--#set var="NEXT"   value="fruit-collection"-->
```

Про апострофи/лапки в назві

```html
<!-- ADDITIONAL CODE HERE -->
<p>У файлі <code>/projects/test-pirate/index.htm</code> може бути розміщений додатковий html-код.</p>
<p>Наприклад, посилання <a href="https://lamathebook.com/" target="_blank">lamathebook</a>, яке буде відкриватися у новій вкладці...</p>

```


Інші файли

```
.gitignore

_apache/different_com_ua.conf

public_html/.htaccess

public_html/_inc/

public_html/css/

public_html/favicon.ico
public_html/favicon_different_old.png

public_html/img/
public_html/img/icons/

public_html/js/
public_html/index.htm

public_html/projects/_list.htm
public_html/projects/_select.htm
public_html/projects/PROJECT_ID/

Назва проекту (project_id)

Кожний проект має 4 файли

public_html/projects/project_id/data.htm
public_html/projects/project_id/index.htm
public_html/projects/project_id/project_id.jpg
public_html/projects/project_id/project_id_preview.jpg

public_html/skill/
public_html/skill/_all.htm
public_html/skill/test.htm

public_html/about/Oleksandra-Syniashchok_CV_2022.docx
public_html/about/Template_eng_01.pdf
public_html/about/index.htm
public_html/about/sashakosmos.jpg

```
