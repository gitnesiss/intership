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

## 1.3 Установка PyInstaller для создания исполняемого файла

Почитать подробнее можно [тут](https://habr.com/ru/companies/slurm/articles/746622/).

```
# Для Windows
pip install pyinstaller
```

Далее необходимо открыть командную строку и перейти в каталог со скриптом. Затем нужно выполнить команду:

```
pyinstaller hello.py

# Создать однофайловый исполняемый файл
pyinstaller --onefile hello.py

# Создать однофайловый исполняемый файл не выводя консоль
pyinstaller --noconsole --onefile hello.py
```




## 1.4 Установка PyQt6

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

## 1.5 Установка библиотеки pyqt-tools для установки дополнительных инструметов и плагинов для Python

```
pip install pyqt6-tools
```

## 1.6 Установка библиотеки pymavlink для работы с протоколом MAVLink 

```
# Для Windows
pip install pymavlink
```

## 1.7 Установка библиотеки для работы с Serial port'ом в Python

Про установку библиотеки можно прочитать [тут](https://musbench.com/all/com-port-python-arduino/).

```
# Для Windows
pip install pyserial

# Для UNIX и RaspberryPi
pip3 install pyserial
```

При установке в UNIX системах, нужно добавить каталог содержащий эту библиотеку в переменную $PATH. Почитать [тут](https://ip-calculator.ru/blog/ask/kak-dobavit-katalog-v-path-v-linux/).

# 2 Сборка QtCreator из исходников на Ubuntu

```
sudo apt-get update -y
sudo apt-get upgrade -y

python3 --version
sudo apt-get install python3

sudo apt-get install python3-pip
pip install -U pip

sudo apt install cmake -y

sudo apt install ninja-build -y

# Устанавливаем Perl
sudo apt-get install perl -y
# Устанавливаем модуль для установки модулей через CPAN:
sudo apt-get install build-essential
# Обновляем модуль
sudo perl -MCPAN -e 'install Bundle::CPAN'
# Интерфейс для работы с базами данных
sudo apt-get install libdbi-perl
# Драйвер для работы с базами данных
sudo apt-get install libdbd-sqlite3-perl -y

sudo apt install clang-15 libclang-15-dev llvm-15 -y

sudo apt install libgl-dev, libegl-dev -y

sudo apt install libfontconfig1-dev libinput-dev libfreetype-dev libx11-dev libx11-xcb-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev libxcb1-dev libxcb-cursor-dev libxcb-glx0-dev libxcb-keysyms1-dev libxcb-image0-dev libxcb-shm0-dev libxcb-icccm4-dev libxcb-sync-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-randr0-dev libxcb-render-util0-dev libxcb-util-dev libxcb-xinerama0-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev -y

sudo apt install libatspi2.0-dev -y

git clone git://code.qt.io/qt/qt5.git qt6

cd qt6 
git switch dev

cd

cd qt6
perl init-repository

cd

mkdir qt6-build 
cd qt6-build 
../qt6/configure -prefix /path/to/install 
cmake --build . --parallel 4 
cmake --install.
```

# 3 Сборка QtCreator из исходников на Windows

## 3.1 Установка CMake

```
pacman -S cmake
```

## 3.2 Установка python3

```
pacman -S python3
```

## 3.3 Сборка QtCreator из исходников

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


# 4 Установка QT в Windows с помощью MSYS2

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