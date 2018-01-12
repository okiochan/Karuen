#  Преобразование Карунена — Лоэва

Возьмем следующую выборку

![](https://raw.githubusercontent.com/okiochan/Karuen/master/img/i1.png)

Применим для нее преобразование Карунена — Лоэва. Метод используется для нормализации "отбеливания" данных.

Сингулярное разложение
![](https://raw.githubusercontent.com/okiochan/Karuen/master/formula/f1.gif)
ковариационной матрицы 
![](https://raw.githubusercontent.com/okiochan/Karuen/master/formula/f2.gif)

новая матрица
![](https://raw.githubusercontent.com/okiochan/Karuen/master/formula/f3.gif)

получим

![](https://raw.githubusercontent.com/okiochan/Karuen/master/img/i2.png)

Наша выборка будет лучше работать с различными методами обучения