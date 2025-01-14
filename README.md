#Программа для обработки банковских данных
## Инструкция по установке

1. Выполнить клонирование репозитория Homework_10.2 себе на компьютер
2. В терминале, находясь в корневой папке проекта, активировать виртуальное окружение через poetry
3. В случае отсутствия менеджера проектов _poetry_, выполнить установку пакетов через _pip_ из списка зависимостей в
4. файле __pyproject.toml_   в файле

## Запуск приложения  
python main.py - из корня репозитория проекта
python <_path_>main.py - из другой папки  
<_path_> - путь к файлу main.py проекта Home_work_module_2

## Тестирование
код протестирован pytest
Чтобы установить pytest, используйте команды: poetry add --group dev pytest

## Включения и генераторы
Генераторные выражения — способ создания итераторов в Python, с помощью которого можно:
генерировать элементы последовательности без хранения их всех в памяти; работать с большими объемами данных;
снижать использование памяти и ускорять выполнение программы.
Функция 
filter()  используется для фильтрации элементов в конвейере. Функция 
map()  в сочетании с функцией 
chain()  из модуля 
itertools  используется для размножения элементов в конвейере.

## Декораторы
Декоратор — это функция, которая принимает другую функцию в качестве аргумента и изменяет ее поведение без изменения
самой функции.

## Библиотека logging
Логирование в Python — это процесс записи информации о том, что происходит в программе во время ее работы.
На основе серьезности сообщений выделяется пять уровней логирования :
DEBUG — сообщения для отладки приложения.
INFO — информационные сообщения.
WARNING — предупреждения.
ERROR — сообщения об ошибках.
CRITICAL — критические сообщения.

## Библиотеки csv и pandas
Библиотека csv в Python — предоставляет удобные средства для работы с файлами в формате CSV.
Для установки библиотеки pandas с помощью poetry необходимо выполнить следующую команду:
poetry add pandas