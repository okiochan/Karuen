#  Преобразование Карунена — Лоэва

Возьмем следующую выборку

![](https://raw.githubusercontent.com/okiochan/Karuen/master/img/i1.png)

Применим для нее преобразование Карунена — Лоэва. Метод используется для нормализации "отбеливания" данных.

Вначале центрируем данные, чтобы вращение было вокруг центра всех точек
```
X = X-X.mean(axis=0)
```

Сингулярное разложение
![](https://raw.githubusercontent.com/okiochan/Karuen/master/formula/f1.gif)
ковариационной матрицы 
![](https://raw.githubusercontent.com/okiochan/Karuen/master/formula/f2.gif)

новая матрица
![](https://raw.githubusercontent.com/okiochan/Karuen/master/formula/f3.gif)

получим

![]( https://raw.githubusercontent.com/okiochan/Karuen/master/img/i2.png)

В формуле, D - растянет выборку, а G - матрица поворота
Мы можем, для примера, заменить  так ("уберем" параметр растяжения, оставим вместо него просто I) и мы видим, что G делает поворот

![]( https://raw.githubusercontent.com/okiochan/Karuen/master/img/i3.png)

Наша выборка будет лучше работать с различными методами обучения