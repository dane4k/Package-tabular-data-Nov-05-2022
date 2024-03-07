# Собственный пакет модулей по манипулированию табличными данными

__my_package является пакетом модулей, предназначенных для обработки табличных данных и совершения над ними различных операций__


## Функционал:

__1. Функция save table для сохранения табличных данных во внутреннее представление модуля файлов форматов .csv, .pickle, .txt__

__2. Функция load_table для загрузки табличных данных во внутреннее представление модуля файлов форматов .csv, .pickle, .txt__

__3. Функция get_rows_by_number для получения части таблицы по заданным индексам (start_index -> stop_index)__

__4. Функция get_rows_by_index для получения части таблицы по заданным значениям поля id__

__5. Функция get_column_types для получения типа данных, содержащихся в каждом из столбцов заданной таблицы__

__6. Функция set_column_types для задания значениям в таблице определенных типов данных__

__7. Функция get_values для получения списка значений (типизированных согласно типу столбца) таблицы из столбца или по номеру столбца__

__8. Функция get_value для получения типа данных в определенном столбце__

__9. Функция set_values для задания списка значений values для столбца таблицы (типизированных согласно типу столбца) либо по номеру столбца__

__10. Функция set_value для представления таблицы с одной строкой, устанавливающая одно значение__

__11. Функция print_table() для вывода содержимого таблицы__

__12. Функция abolishing_date для добавления столбца с данными типа "дата время"__

__13. Функции add, sub, mul, div для совершения арифметических операций (+, -, *, /) над ячейками в столбцах с типами данных int, float, bool__


