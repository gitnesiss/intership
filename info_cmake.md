Для работы с cmake, в корне проекта создаётся файл CMakeLists.txt с правилами и целями сборки.

Создадим HelloWorld.ccp:
```
#include <iostream>

int main() {
    std::cout << "Hello World!" << std::endl;
    return 0;
}
```

Базовое содержание CMakeLists.txt файла:
```
cmake_minimum_required(VERSION 2.8) # Проверка версии CMake.
									# Если версия установленой программы
									# старее указаной, произайдёт аварийный выход.

add_executable(main main.cpp)		# Создает исполняемый файл с именем main
									# из исходника main.cpp
```

Синтаксис CMake похож на синтаксис bash, всё что после символа "#" является комментарием и обрабатываться программой не будет.