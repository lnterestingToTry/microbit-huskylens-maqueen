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
Програмування мікроконтролера Micro:bit відбується за допомогою сервісу MakeCode
У випадку з даним проектом буде використано мову Python. MakeCode також підтримує програмування на JavaScript або Блоками. Використовуючи будь-який із способів, код буде конвертовано в TypeScript і потім завантажено на мікроконтролер.
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

```
if x_box_position > width_center + free_gap_x:
        MoveRight()
    elif width_center - free_gap_x > x_box_position and x_box_position > -1:
        MoveLeft()
    elif box_height > box_height_default + free_gap_y:
            MoveBackward()
    elif box_height < box_height_default - free_gap_y and box_height > -1:
            MoveForward()
    else:
        Stop()
```



```
def on_forever():
    if x_box_position > width_center + free_gap_x:
        MoveRight()
    elif width_center - free_gap_x > x_box_position and x_box_position > -1:
        MoveLeft()
    elif box_height > box_height_default + free_gap_y:
            MoveBackward()
    elif box_height < box_height_default - free_gap_y and box_height > -1:
            MoveForward()
    else:
        Stop()
```





`y_box_position`= 0
`x_box_position` = 0
`y_box_position` = 0
`x_box_position` = 0

`box_height_default` = 65

`screen_width` = 320
`screen_hight` = 240

`width_center` = screen_width / 2
`hight_center` = screen_hight / 2

`free_gap_x` = 30
`free_gap_y` = 10

`speed` = 35

