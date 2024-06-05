# Робототехнічна система на основі мікроконтролера Micro:bit
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/rob1.png)
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/rob2.png)

# Ціль: Запрограмувати мікроконтролер на вирішення задачі слідування робоплатформи за цільовим об’єктом, дані про який зчитує відеодатчик.

# Принцип роботи алгоритму
Завданням є задіювати мотори так, аби цільовий об'єкт залишався на зображенні, що зчитує відеодатчик


# `Вид зверху`
Якщо цільовий об'єкт на зображенні, що зчитав відеодатчик, не знаходиться в області, що утворює кут A, необхідно задіяти мотор, протилежний стороні в якій знаходиться цільовий об'єкт (відносно області, що утворює кут A). Якщо цільовий об'єкт на зображенні зліва, необхідно задіяти правий мотор і робоплатформа разом з відеодатчиком здійснить рух так, аби розмістити об'єкт на зображені в допустимій області кута A.
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/top.png)


# `Вид збоку`
Якщо цільовий об'єкт на зображенні, що зчитав відеодатчик:
- має більшу висоту, ніж h1, необхідно задіяти два мотори для руху назад
- має меншу висоту, ніж h2, необхідно задіяти два мотори для руху вперед
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/side.png)



# Програмний опис алгоритму
Програмування мікроконтролера Micro:bit відбується за допомогою веб-ресурсу MakeCode.
У випадку з даним проектом буде використано мову Python. MakeCode також підтримує програмування на JavaScript або Блоками. При завантаженні коду на мікроконтролер, код, написаний будь-яким із способів, буде автоматично конвертовано в код мови TypeScript і потім завантажено на мікроконтролер.
Реалізація вище описаного алгоритму не потребувала великої кількості інструкцій, тому код розміщено в одному файлі - main.py.

В основі реалізації алгоритму лежить використання циклу while. У випадку з програмування мікроконтролера, замість while використовується конструкція:

```
def on_forever():
    ...
basic.forever(on_forever)
```

Інструкції, описані в функції on_forever будуть виконуватись постійно (по анології з while).

![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/x1h3.png)

Кожна ітерація on_forever має починатись зі зчитування даних із відеодатчика. Необхідно отримати позицію цетра по координаті х (x1) та висоту (h3) об'єкта на зображенні.
```
huskylens.request()

x_box_position = huskylens.reade_box(1, Content1.X_CENTER)
box_height = huskylens.reade_box(1, Content1.HEIGHT)
```

Маючи дані параметри, опишемо логіку руху:

![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/x2h4.png)

`width_center` - x2
`free_gap_x` - h4 (значення, що встановлюється вручну)

```
if x_box_position > width_center + free_gap_x:
    MoveRight()
elif width_center - free_gap_x > x_box_position and x_box_position > -1:
    MoveLeft()
```
(В умовних виразах використовується `... and x_box_position > -1`. Якщо відеодатчик не знаходить об'єкта на зображення, то повертає -1. Аби запобігти виходу за допустипі рамки можливих координат, використано `... and x_box_position > -1`)

Умови відносно висоти об'єкта на зображенні:

![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/y1h5.png)

`box_height_default` - значення, що встановлюється вручну
`free_gap_y` - h5 (значення, що встановлюється вручну)

```
elif box_height > box_height_default + free_gap_y:
        MoveBackward()
elif box_height < box_height_default - free_gap_y and box_height > -1:
        MoveForward()
```

Якщо жодна з умов не виконана - зупинка:

```
else:
    Stop()
```

[main.py](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/main.py)
