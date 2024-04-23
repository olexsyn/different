# Table of Contents

1 [Як створити новий проект](#Як-створити-новий-проект)  
  1.1 [Вибір назви проекту](#Вибір-назви-проекту)  
  1.2 [Файли проекту](#Файли-проекту)  
    1.2.1 [Зображення (.jpg)](#Зображення-jpg)  
    1.2.2 [Код (.htm)](#Код-htm)  
2 [Як додати нову навичку (skill)](#Як-додати-нову-навичку-skill)
2 [Як додати нову навичку2](#Як-додати-нову-навичку2)

3 [Технічні деталі](#Технічні-деталі)


Для даного сайту сторінка - є окремим **проектом**, а в якості теґів - маємо на увазі **навички**.

## Як створити новий проект

Проекти розміщені в _**public_html/projects/**_.

### Вибір назви проекту

Для того, щоб додати новий проект необхідно в _**public_html/projects/**_ створити папку з його унікальним іменем (технічною мовою - ідентифікатором), що може складається з маленьких латинських літер, цифр і дефісу.

Наприклад, ми хочемо додати проект під назвою "Llama in the Moon Kingdom". Для цього краще створити таку папку: _**public_html/projects/llama-in-the-moon-kingdom/**_.

Необов’язково, щоб літери точно співпадали з назвою проекта. Папку можна назвати і _**llama-in-the-moon**_, а також _**llama-2**_. Але краще, щоб ім’я несло в собі якийсь зрозумілий зміст...

### Файли проекту

В кожній папці проекту має бути 4 файли:

```
llama-in-the-moon-kingdom/data.htm                               - дані проекту (ім’я, заголовок, опис, скіли, та ін.)
llama-in-the-moon-kingdom/index.htm                              - головна сторінка-шаблон, яка "підтягує" дані
llama-in-the-moon-kingdom/llama-in-the-moon-kingdom.jpg          - велике зображення проекту
llama-in-the-moon-kingdom/llama-in-the-moon-kingdom_preview.jpg  - маленьке зображення (прев’юшка)
```

#### Зображення (.jpg)

Файли `.jpg` повинні містити в собі точну назву проекту, тобто, унікальної назви папки в якому він знаходиться. До назви маленького зображення додаємо `_preview` перед розширенням.

Великі зображення краще створювати з шириною 580 px. Можна робити і іншого розміру, але це в деякій мірі може позначитися на якості їх відображення, бо в цьому випадку вони будуть масштабовані. Висота великого зображення - довільна. Якщо маємо декілька зображень для проекту - краще об’єднати їх вертикально в одне зображення.

Аналогічно і з прев’юшками. Розмір при якому вони не будуть масштабуватися - 280×170 px. Якщо зберегти відповідні пропорції для усіх зображень - ми отримаємо вирівнені по вертикалі і горизонталі клітинки. Якщо пропорцій не дотримуватися - зображення будуть вирівнені лише вертикально (по колонках).

#### Код (.htm)

- **data.htm**
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
ID     - ідентифікатор (як і назва папки)
TITLE  - заголовок
DESCR  - опис
SKILL  - скіл 1
SKILL2 - скіл 2
SKILL3 - скіл 3 (можна лише до 3х)
PREV   - посилання на попередній проект
NEXT   - посилання на наступний проект
```

DESCR - може бути порожнім: `''`, як і SKILL2, SKILL3, PREV і NEXT.

Необхідно звертати увагу на присутність в TITLE і DESC подвійних лапок і апострофів, щоб не виникла помилка при побудові сторінки. Пояснюю...

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

- Варіант 1: `value='Everyone\'s favorite game "Mafia" with new characters...'` (екранувати апостроф, якщо value обмежено апострофами)
- Варіант 2: `value="Everyone's favorite game \"Mafia\" with new characters..."` (екранувати подвійні лапки, якщо value обмежено лапками)
- Варіант 3: `value="Everyone's favorite game «Mafia» with new characters..."` (використати інші лапки `«»`)
- Варіант 4: `value="Kids always ask: “What should I do?”."` (такі лапки `“”` теж можна беспечно застосовувати в тексті)



```html
<!-- ADDITIONAL CODE HERE -->
<p>У файлі <code>/projects/test-pirate/index.htm</code> може бути розміщений додатковий html-код.</p>
<p>Наприклад, посилання <a href="https://lamathebook.com/" target="_blank">lamathebook</a>, яке буде відкриватися у новій вкладці...</p>

```

## Як додати нову навичку (skill)

Скіли розміщені в _**public_html/skill/**_.

В цій папці ми бачимо перелік файлів `.htm` і’мя яких є назвами скілів:

### HTML-файли (.htm)

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

_all.htm - використовується на головній сторінці, де ми відображуємо усі проекти з усіма скілами. А інші - на сторінках, де ми показуємо проекти, що мають відношення до цього скіла.

Для того, щоб додати новий скіл (наприклад, "test"), беремо один з файлів (крім _all.htm) і робимо його копію з іменем _**test.htm**_.
Потім, за допомогою текстового редактора відкриваємо цей файл знаходимо і підправляємо рядок
```
<!--#set var="SELSKILL" value="OLD_SKILL_NAME"-->
```
замінивши в value значення іншого скіла на "test":
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

## Технічні деталі

Просто для інформації, можливо знадобиться.

Щоб не повторювати однаковий код я застосував технологію SSI (Server Side Includes) – потужний та гнучкий засіб для динамічного формування веб-сторінок на стороні сервера
