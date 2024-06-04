# Робототехнічна система на основі мікроконтролера Micro:bit
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/rob1.png)
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/rob2.png)

# Завдання: Запрограмувати мікроконтролер на вирішення задачі слідування робоплатформи за цільовим об’єктом, дані про який зчитує відеодатчик.

# Принцип роботи алгоритму
Завданням є задіювати мотори так, аби цільовий об'єкт залишався на зображенні, що зчитує відеодатчик

#* `Вид збоку`
Якщо цільовий об'єкт на зображенні, що зчитав відеодатчик, не знаходиться в області, що утворює кут А
- 
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/side.png)


#* `Вид зверху`
Якщо цільовий об'єкт на зображенні, що зчитав відеодатчик, не знаходиться в області, що утворює кут B, необхідно задіяти мотор, протилежний стороні в якій знаходиться цільовий об'єкт (відносно області, що утворює кут B). Якщо цільовий об'єкт на зображенні зліва, необхідно задіяти правий мотор і робоплатформа разом з відеодатчиком здійснить рух так, аби розмістити об'єкт на зображені в допустимій області кута B.
![alt text](https://github.com/lnterestingToTry/microbit-huskylens-maqueen/blob/main/img/top.png)

