# date_of_birth

### Требования
[python 3.7+](https://www.python.org/)<br/>
pip install --user -r requirements.txt

### Описание
Простая программа с графическим интерфейсом, для тех, кто забывает дни рождения друзей или близких, но часто пользуется компьютером.

### create_date.py (для добавления даты рождения)
![alt tag](https://github.com/iterweb/date_of_birth/blob/master/image/create_date.png "iterweb")​<br/>
При первом запуске скрипта будет создана база данных sqlite3, в открывшемся окне можно добавить дату и имя (уникально). Присутствует проверка на коректность вводимых данных(число, месяц, год).

### check_date.py (проверка и оповищение)
![alt tag](https://github.com/iterweb/date_of_birth/blob/master/image/check_date.png "iterweb")​<br/>
Важно, добавить данный файл в автозагрузку (я не стал этого делать програмно),что бы при вкл. компьютера все даты из БД были сопоставлены. Этот скрипт проверяет все даты которые вы дабавите в БД, с текущей датой на ПК. если даты совпадут, вы будете оповещены об этом, плюс к этому, на рабочем столе будет создан файл birthday.tхt, в котором содержится информация о возрасте и имени человека. При желании дату можно удалить из БД.

### Компиляция
pip install pyinstaller<br/>
pyinstaller -w file.py
