[Вернуться в файл Стажировки](intership.md)

Установка вспомогательных програм:
1. Установка CMake

```
pacman -S cmake
```

2. Установка python3

```
pacman -S python3
```

3. Сборка QtCreator из исходников

```
$ sudo apt install cmake
$ sudo apt install qt5-default qtdeclarative5-dev qtscript5-dev
$ sudo apt install clang-10 # собственно clang, llvm
$ sudo apt install libclang-10-dev # не понял пока зачем, но конфигуратор qmake его хочет
$ sudo apt install llvm # нужно для получения утилиты llvm-config
```

```
$ qmake -r
$ make
$ sudo make install INSTALL_ROOT=[директория, в которую хотите установить. Например, /opt/QtCreator]
```



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

[Вернуться в файл Стажировки](intership.md)