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

