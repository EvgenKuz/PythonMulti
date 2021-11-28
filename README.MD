# IO-bound. Проверяем ссылки на страницах Википедии

## Синхронная проверка ссылок

![](Wikipedia/one_thread_GetLinks.PNG)

## 5 workers

![](Wikipedia/5workers.PNG)

Процент использования процессора почти не увеличивался за время исполнения, использование сети тоже
почти не менялось и не выходило за пределы 1,1 Мбит/с. Изменялась лишь память, её использование
постепенно росло и пошло до более чем 70 МБ.

## 10 workers

![](Wikipedia/10workers.PNG)

Использование ЦП точно так же не росло. Использование сети же вырастало до 2,5 Мбит/c.
Памяти потребовалось примерно столько же.

## 100 workers

![](Wikipedia/100workers.PNG)

Использование ЦП возросло примерно на 1 процент. Использование сети доходило до 30 Мбит/с.
Памяти потребовалось более чем 100 МБ.