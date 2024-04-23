# Table of Contents

1 [Структура сайту](#1-Структура-сайту)  
2 [Як створити новий проект](#2-Як-створити-новий-проект)  
  2.1 [Вибір назви проекту](#21-Вибір-назви-проекту)  
  2.2 [Файли проекту](#22-Файли-проекту)  
    2.2.1 [Зображення (.jpg)](#221-Зображення-jpg)  
    2.2.2 [Код (.htm)](#222-Код-htm)  
      - [data.htm](#datahtm)  
      - [index.htm](#indexhtm)  
3 [Як додати нову навичку (skill)](#3-Як-додати-нову-навичку-skill)  
4 [Сторінка About](#4-Сторінка-About)  
5 [Оновлення файлів на сервері](#5-Оновлення-файлів-на-сервері)  
6 [Інші технічні деталі](#6-Інші-технічні-деталі)  

# 1 Структура сайту

Нижче наведена спрощена структура сайту, де прокоментовані директорії і файли в які можна вносити правки. Непрокоментовані директорії краще не займати, щоби сайт не зламався :).

```
public_html/
    _inc/ 
    about/        - сторінка About і її файли
    css/
    img/
        icons/    - іконки для різних операційних систем та браузерів
    js/
    projects/     - директорія проектів 
    skill/        - директорія навичок
    .htaccess
    index.htm
    favicon.ico   - головна іконка сайту
.gitignore
README.md
```

Для даного сайту **проект** - є окрема директорія з файлами, що утворюють _сторінку_, а коли говоримо про **навички** - маємо на увазі _теґи_.

[top](#table-of-contents)

# 2 Як створити новий проект

Проекти розміщені в _**public_html/projects/**_.

[top](#table-of-contents)

## 2.1 Вибір назви проекту

Для того, щоб додати новий проект необхідно в _**public_html/projects/**_ створити директорію з його унікальним ім’ям (ідентифікатором), що може складається з маленьких латинських літер, цифр і дефісу.

Наприклад, ми хочемо додати проект під назвою "Llama in the Moon Kingdom". Для цього краще створити таку директорію: _**public_html/projects/llama-in-the-moon-kingdom/**_.

Необов’язково, щоб літери точно співпадали з назвою проекта. Директорію можна назвати і _**llama-in-the-moon**_, а також _**llama-2**_. Але краще, щоб ім’я несло в собі якийсь зрозумілий зміст...

[top](#table-of-contents)

## 2.2 Файли проекту

В кожній директорії проекту має бути 4 файли. Краще не створювати файли з нуля, а скопіювати з іншого проекту і відредагувати.

Якщо ми розглядаємо проект "llama-in-the-moon-kingdom", то назви файлів будуть такими:

```
data.htm                               - дані проекту (ім’я, заголовок, опис, скіли, та ін.)
index.htm                              - головна сторінка-шаблон, яка "підтягує" дані
llama-in-the-moon-kingdom.jpg          - велике зображення проекту
llama-in-the-moon-kingdom_preview.jpg  - маленьке зображення (прев’юшка)
```

[top](#table-of-contents)

### 2.2.1 Зображення (.jpg)

Файли `.jpg` повинні містити в собі точну назву проекту, тобто, унікальної назви директорії в якій вони знаходиться. До назви маленького зображення додаємо `_preview` перед розширенням.

Великі зображення краще створювати з шириною **580 px**. Можна робити і іншого розміру, але це, в деякій мірі, може позначитися на якості їх відтворення, бо в цьому випадку вони будуть масштабовані. Висота великого зображення - довільна. Якщо маємо декілька зображень для проекту - краще об’єднати їх вертикально в одне зображення.

Розмір прев’ю-файлів при якому вони не будуть масштабуватися - **280×170 px**. Якщо зберегти відповідні пропорції для усіх зображень - ми отримаємо вирівнені по вертикалі і горизонталі клітинки. Якщо пропорцій не дотримуватися - зображення будуть вирівнені лише вертикально (по колонках).

[top](#table-of-contents)

### 2.2.2 Код (.htm)

#### data.htm

Приклад файлу для проекту "llama-in-the-moon-kingdom":

```
<!--#set var="ID"     value="llama-in-the-moon-kingdom"-->
<!--#set var="TITLE"  value="Llama in the Moon Kingdom"-->
<!--#set var="DESCR"  value="Creating and publishing my own book for children."-->
<!--#set var="SKILL"  value="illustration"-->
<!--#set var="SKILL2" value=""-->
<!--#set var="SKILL3" value=""-->
<!--#set var="PREV"   value="tenero-cheese"-->
<!--#set var="NEXT"   value="barrel-lvivske"-->
```
де
```
ID     - ідентифікатор (як і назва директорії)
TITLE  - заголовок
DESCR  - опис
SKILL  - скіл 1
SKILL2 - скіл 2
SKILL3 - скіл 3
PREV   - посилання на попередній проект
NEXT   - посилання на наступний проект
```
DESCR - може бути порожнім: `''`, як і SKILL2, SKILL3, PREV і NEXT.

Скрипти обробляють лише 3 скіли. Якщо додати параметр SKILL4 - це ні на що не вплине.

Необхідно звертати увагу на присутність подвійних лапок і апострофів в TITLE і DESC, щоб не виникла помилка при побудові сторінки. Про це - детальніше.

Значення value можна обмежувати як подвійними лапками, так і апострофами:
```
<!--#set var="TITLE"  value="Llama in the Moon Kingdom"-->
<!--#set var="DESCR"  value='Creating and publishing my own book for children.'-->
```
Якщо у тексті є символ апострофу `'`, то треба застосувати подвійні лапки: 
```
<!--#set var="DESCR"  value="Everyone's favorite game..."-->
```
Якщо у тексті є подвійні лапки `"`, то слід застосувати апострофи: 
```
<!--#set var="DESCR"  value='Advertising campaign for TM "Avenue".'-->
```
Але що робити, коли в тексті є і апострофи і подвійні лапки? (_"Everyone\'s favorite game "Mafia" with new characters..."_)

- Варіант 1: екранувати апостроф, якщо value обмежено апострофами  
`value='Everyone\'s favorite game "Mafia" with new characters...'`
- Варіант 2: екранувати подвійні лапки, якщо value обмежено лапками  
`value="Everyone's favorite game \"Mafia\" with new characters..."`
- Варіант 3: використати інші лапки `«»`  
`value="Everyone's favorite game «Mafia» with new characters..."`
- Варіант 4: лапки `“”` теж можна беспечно застосовувати в тексті  
`value="Kids always ask: “What should I do?”."`

#### index.htm

При необхідності надати більше інформації про проект (додаткові зображення, текст, посилання) це можна зробити у файлі index.htm, що знаходиться в директорії проекту, між мітками `<!-- ADDITIONAL CODE HERE -->` і `<!--#include virtual=...`. За допомогою текстового редактора додаємо необхідний HTML-код. Наприклад:

```html
<!-- ADDITIONAL CODE HERE -->

<p>У цьому місці може бути розміщений додатковий html-код.</p>
<p>Наприклад, ось посилання <a href="https://lamathebook.com/" target="_blank">lamathebook</a>,
що при натисканні буде відкриватися у новій вкладці...</p>

<!--#include virtual="/_inc/arrows_navigation.htm"-->
```
Більший приклад оформлення додаткової інформації дивись у файлі _**/projects/llama-in-the-moon-kingdom/index.thm**_

[top](#table-of-contents)

# 3 Як додати нову навичку (skill)

Скіли розміщені в _**public_html/skill/**_.

В цій директорії ми бачимо перелік файлів `.htm` ім’я яких є назвами скілів:

```
skill/_all.htm
skill/app.htm
skill/game.htm
skill/illustration.htm
skill/logo.htm
skill/packaging.htm
skill/print.htm
skill/watercolor.htm
skill/web.htm
```

_all.htm - використовується на головній сторінці, де ми відображуємо усі проекти з усіма скілами. А інші - на сторінках, де ми показуємо проекти, що мають відношення саме до цього скіла.

Для того, щоб додати новий скіл, наприклад, "test", беремо один з файлів (крім _all.htm), наприклад **watercolor.htm** і робимо його копію з іменем _**test.htm**_.
Потім, за допомогою текстового редактора відкриваємо цей файл знаходимо і підправляємо рядок
```
<!--#set var="SELSKILL" value="watercolor"-->
```
де заміняємо значення value іншого скіла на "test":
```
<!--#set var="SELSKILL" value="test"-->
```
Зберігаємо файл і можемо використовувати скіл в файлах data.htm:
```
...
<!--#set var="SKILL"  value="illustration"-->
<!--#set var="SKILL2" value="test"-->
...
```
[top](#table-of-contents)

# 4 Сторінка About

Сторінка About знаходиться тут: _**public_html/about/**_. 

Щоб відредагувати її зміст - треба відкрити за допомогою текстового редактора файл _**/about/index.htm**_ і внести в нього зміни. Це не важко зробити. Ось основні HTML-теґи, які там використовуються:

```html
<p>Це просто абзац з текстом.</p>

<p>Це абзац в якому наступні слова <b>написані жирним шрифтом</b>!</p>

<p>Цей теґ <br /> перенесе ось цю частину тексту на новий рядок в межах одного абзацу.</p>

<p>В цьому абзаці - посилання на файл file.docx, що лежить в цій же директорії <a href="file.docx">Завантаж мене!</a></p>

<p>А тут посилання на інший сайт: <a href="https://lamathebook.com">Відкрий мене!</a></p>

<p>
  А якщо у посилання додати target="_blank", то цей сайт буде відкритий у новій вкладці браузера:
  <a href="https://lamathebook.com" target="_blank">Я відкриюсь у іншій вкладці!</a>.
</p>


 target="_blank"

```

[top](#table-of-contents)


# 5 Оновлення файлів на сервері

[top](#table-of-contents)


# 6 Інші технічні деталі

Просто для інформації, можливо знадобиться.

Щоб не повторювати однаковий код я застосував технологію SSI (Server Side Includes) – потужний та гнучкий засіб для динамічного формування веб-сторінок на стороні сервера

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
[top](#table-of-contents)
