[Вернуться в раздел Стажировки](intership.md)

# Содержанине раздела

[Установка Python в Windows](#1-установка-python-в-windows)

[Сборка QtCreator из исходников](#2-сборка-qtcreator-из-исходников)

[Установка QT в Windows с помощью MSYS2](#3-установка-qt-в-windows-с-помощью-msys2)


# 1 Установка Python в Windows

## 1.1 Проверяем наличие Python и устанавливаем его

```
# Для Windows
python --version

# Для UNIX
python3 --version
```

Если в терминале получен похожий ответ `Python 3.11.8`, то это означает, что  Python установлен.

Если ответ похож на `Python is not defined`, то скачиваем [установщик](https://www.python.org/downloads/).

```
# Устанавливаем Python на UNIX
sudo apt-get update -y
sudo apt-get install python3
```

## 1.2 Устаналвиваем PIP (предпочитаемый установщик программ) для Python и обновляем его

При версиях Python выше 3.4 `pip` должен устанавливаться с установкой самого Python. Если этого не произошло, то можно его установить с помощью

```
# Для UNIX и RaspberryPi
sudo apt-get install python3-pip
```

Обновить pip можно с помощью команд

```
# Для Windows
python -m pip install -U pip

# Для UNIX и RaspberryPi
pip install -U pip
```

## 1.3 Установка PyQt6

Для установки PyQt6 следует запустить следующую команду

```
# Для Windows
pip install PyQt6

# Для UNIX и RaspberryPi
pip3 install PyQt6
```

Для проверки правильности установки PyQt6 выполняем следующие действия

```
# Для Windows
python  # Запускаем интерпретатор Python
    import PyQt6  # далее в интерпретаторе вводим команду
    exit()  # выходим из интерпретатора в терминал


# Для UNIX и RaspberryPi
python3  # Запускаем интерпретатор Python
    import PyQt6  # далее в интерпретаторе вводим команду
    exit()  # выходим из интерпретатора в терминал
```

Если никаких ошибок не возникло, то установка прошла удачно. Если возникла ошибка, то нужно причины ошибки.

## 1.4 Установка библиотеки pymavlink для работы с протоколом MAVLink 

```
# Для Windows
pip install pymavlink
```

## 1.5 Установка библиотеки для работы с Serial port'ом в Python

Про установку библиотеки можно прочитать [тут](https://musbench.com/all/com-port-python-arduino/).

```
# Для Windows
pip install pyserial

# Для UNIX и RaspberryPi
pip3 install pyserial
```

При установке в UNIX системах, нужно добавить каталог содержащий эту библиотеку в переменную $PATH. Почитать [тут](https://ip-calculator.ru/blog/ask/kak-dobavit-katalog-v-path-v-linux/).

# 2 Сборка QtCreator из исходников

## 2.1 Установка CMake

```
pacman -S cmake
```

## 2.2 Установка python3

```
pacman -S python3
```

## 2.3 Сборка QtCreator из исходников

```
$ sudo apt install cmake
$ sudo apt install qt5-default qtdeclarative5-dev qtscript5-dev
$ sudo apt install clang-10 # собственно clang, llvm
$ sudo apt install libclang-10-dev # для работы конфигуратор qmake
$ sudo apt install llvm # нужно для получения утилиты llvm-config
```

```
$ qmake -r
$ make
$ sudo make install INSTALL_ROOT=[директория, в которую хотите установить. Например, /opt/QtCreator]
```

----


# 3 Установка QT в Windows с помощью MSYS2

Для установки QT Creator на Windows нужно выполнить следующие шаги:

1. Перейти на сайт [msys2](https://www.msys2.org/).
2. Скачать установочный файл `msys2-x86_64-20240507.exe`.
3. Установить файл `msys2-x86_64-20240507.exe`.
4. По завершению установки запустить файл `ucrt64.exe` находящийся по адресу `C:\msys64\` если был выбран путь установки по умолчанию.
5. В запущенном терминале вводим команду для установки инструментов компиляции:
```
pacman -S mingw-w64-ucrt-x86_64-gcc
```
При установке появится вопрос для продолжения установки - нажимаем "Enter".
6. Проверим установлен ли компилятор с помощью команды:
```
gcc --version
```
7. Обновляем все пакеты MSYS2:
```
pacman -Suy
```
При установке появится вопрос для продолжения установки - нажимаем "Enter".

В одном из вопросов при обновлении появится запрос на перезагрузку терминала, лучше перезагрузить и запустить снова терминал как в п.4. И снова ввести команду `pacman -Suy`.

8. Устаналвиваем QT Creator:
```
pacman -S base base-devel mingw-w64-x86_64-qt6 mingw-w64-x86_64-qt6-base mingw-w64-x86_64-toolchain mingw-w64-x86_64-qt-creator mingw-w64-x86_64-qt6-static mingw-w64-x86_64-cmake mingw-w64-x86_64-clang mingw-w64-x86_64-cc mingw-w64-x86_64-clang mingw-w64-x86_64-qt5-static  mingw-w64-x86_64-vulkan-headers mingw-w64-x86_64-python mingw-w64-x86_64-clang-tools-extra
```

[Вернуться в раздел Стажировки](intership.md)