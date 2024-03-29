# A. A+B (пробная задача)

|                                |                   |
| ------------------------------ | ----------------- |
| ограничение по времени на тест | 1 секунда         |
| ограничение по памяти на тест  | 256 мегабайт      |
| ввод                           | стандартный ввод  |
| вывод                          | стандартный вывод |

Заданы два целых числа $a$ и $b$. Выведите $a + b$.

## Входные данные
В первой строке записано целое число $t$ ( $1 \leq t \leq 10^4$ ) — количество наборов входных данных в тесте. 
Далее следуют $t$ наборов входных данных.

Каждый набор задан одной строкой, которая содержит два целых числа $a$, $b$ ( $−1000 \leq a, b \leq 1000$ ).

## Выходные данные
Выведите $t$ целых чисел — искомые суммы $a + b$ для каждого набора входных данных.

### Пример
входные данные
```
4
1 5
314 15
-99 99
123 987
```
выходные данные
```
6
329
0
1110
```

### Примечание
Запрещается использовать стандартные сортировки.




# B. Излишне простая сортировка

|                                |                   |
| ------------------------------ | ----------------- |
| ограничение по времени на тест | 2 секунды         |
| ограничение по памяти на тест  | 64 мегабайта      |
| ввод                           | стандартный ввод  |
| вывод                          | стандартный вывод |

Дан небольшой массив целых чисел. Ваша задача — отсортировать его в порядке неубывания. Напишите любую квадратичную сортировку.

## Входные данные
В первой строке входного файла содержится число $n$ ( $1 \leq n \leq 1000$ ) — количество элементов в массиве. 
Во второй строке находятся n целых чисел, по модулю не превосходящих $10^9$.

## Выходные данные
В выходной файл надо вывести этот же массив в порядке неубывания, между любыми двумя числами должен стоять ровно один пробел.

### Пример
входные данные
```
10
1 8 2 1 4 7 3 2 3 6
```
выходные данные
```
1 1 2 2 3 3 4 6 7 8 
```

### Примечание
Запрещается использовать стандартные сортировки.




# C. Простая сортировка

|                                |                   |
| ------------------------------ | ----------------- |
| ограничение по времени на тест | 2 секунды         |
| ограничение по памяти на тест  | 64 мегабайта      |
| ввод                           | стандартный ввод  |
| вывод                          | стандартный вывод |

Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания. Напишите сортировку слиянием.

## Входные данные
В первой строке входного файла содержится число $N$ ( $1 \leq N \leq 100000$ ) — количество элементов в массиве. 
Во второй строке находятся $N$ целых чисел, по модулю не превосходящих $10^9$.

## Выходные данные
В выходной файл надо вывести этот же массив в порядке неубывания, между любыми двумя числами должен стоять ровно один пробел.

### Пример
входные данные
```
10
1 8 2 1 4 7 3 2 3 6
```
выходные данные
```
1 1 2 2 3 3 4 6 7 8 
```

### Примечание
Запрещается использовать стандартные сортировки.




# D. Количество инверсий

|                                |                   |
| ------------------------------ | ----------------- |
| ограничение по времени на тест | 5 секунд          |
| ограничение по памяти на тест  | 256 мегабайт      |
| ввод                           | стандартный ввод  |
| вывод                          | стандартный вывод |

Напишите программу, которая для заданного массива  $A = \langle a_1, a_2, \dots, a_n \rangle$ находит количество пар ( $i$, $j$ ) таких, что $i < j$ и $a_i > a_j$.

## Входные данные
Первая строка входного файла содержит натуральное число $n$ ( $1 \leq n \leq 500000$ ) — количество элементов массива. 
Вторая строка содержит $n$ попарно различных элементов массива $A$ ( $0 \leq a_i \leq 10^6$ ).

## Выходные данные
В выходной файл выведите одно число — ответ на задачу.

### Примеры
входные данные
```
4
1 2 4 5
```
выходные данные
```
0
```

входные данные
```
4
5 4 2 1
```
выходные данные
```
6
```

### Примечание
С помощью сортировки слиянием, можно находить число инверсий в массиве.




# E. Простая сортировка

|                                |                   |
| ------------------------------ | ----------------- |
| ограничение по времени на тест | 2 секунды         |
| ограничение по памяти на тест  | 64 мегабайта      |
| ввод                           | стандартный ввод  |
| вывод                          | стандартный вывод |

Дан массив целых чисел. Ваша задача — отсортировать его в порядке неубывания. Реализовать быструю сортировку.

## Входные данные
В первой строке входного файла содержится число $N$ ( $1 \leq N \leq 100000$ ) — количество элементов в массиве. 
Во второй строке находятся $N$ целых чисел, по модулю не превосходящих $10^9$.

## Выходные данные
В выходной файл надо вывести этот же массив в порядке неубывания, между любыми двумя числами должен стоять ровно один пробел.

### Пример
входные данные
```
10
1 8 2 1 4 7 3 2 3 6
```
выходные данные
```
1 1 2 2 3 3 4 6 7 8 
```

### Примечание
Запрещается использовать стандартные сортировки.




# F. Королевская сортировка

|                                |                   |
| ------------------------------ | ----------------- |
| ограничение по времени на тест | 1 секунда         |
| ограничение по памяти на тест  | 256 мегабайт      |
| ввод                           | стандартный ввод  |
| вывод                          | стандартный вывод |

У нерушимого города-государства Иннолэнд богатая история. Множество королей правило на этой земле в течение многих веков. 
Город гордится своими предводителями, поэтому его жители хотят выбить имя каждого из королей на особой плите в самом центре 
города (дабы заполнить хотьчем-то пустующий и безлюдный город).

У каждого короля Иннолэнда помимо имени имеется порядковый номер. Этот номер записан в римской системе счисления рядом 
с именем каждого короля великого города-государства. Например, Louis XIII был тринадцатым королем Иннолэнда, имеющим имя 
Louis (ох уж эти иннолэндовцы и их имена...).

Однако не все так просто устроено в этом городе. Жители Иннолэнда любят соблюдать порядок во всем, поэтому должен соблюдаться 
и порядок имен на плите. Важно, чтобы имена на плите были упорядочены в лексикографическом порядке. Однако некоторые короли 
могли иметь одно и то же имя, поэтому короли с одинаковым именем они должны быть отсортированы в соответствии с их порядковыми номерами. 
Например, славный король Louis IX должен быть указан на плите после доблестного короля Louis VIII.

Жители Иннолэнда пока ещё плохо ладят с упорядочиванием имен и уж тем более с компьютерами, поэтому они обратились за помощью к Вам — 
Вы-то уже давно хорошо знакомы с этими вещами. Они передали список имен всех королей, а Вы должны вернуть им тот же список, 
но имена в нем должны идти уже в нужном порядке: в желаемом списке раньше записаны те короли, у которых имя лексикографически меньше, 
а среди королей с одинаковым именем раньше идут те, у которых меньше порядковый номер.

## Входные данные
В первой строке записано число $n$ ( $1 \leq n \leq 50$ ) — количество королей.
В следующих $n$ строках записаны имена и порядковые номера королей. В каждой строке сначала записано имя короля, 
состоящее из не более чем 20 латинских букв (первая буква имени прописная, все последующие строчные), а затем через 
пробел записан его порядковый номер в виде римского числа от 1 до 50.

## Выходные данные
В $n$ строках должны быть записаны имена и порядковые числа королей, упорядоченные необходимым образом.

### Примеры
входные данные
```
2
Louis IX
Louis VIII
```
выходные данные
```
Louis VIII
Louis IX
```
входные данные
```
2
Louis IX
Philippe II
```
выходные данные
```
Louis IX
Philippe II
```
входные данные
```
2
Philippe II
Philip II
```
выходные данные
```
Philip II
Philippe II
```

### Примечания
- Числа от 1 до 10 обозначаются с помощью римских цифр как I, II, III, IV, V, VI, VII, VIII, IX и X соответственно.
- Числа 20, 30, 40 и 50 обозначаются как XX, XXX, XL и L соответственно.
- Остальные двузначные числа меньшие 50 в римской записи могут быть получены путем конкатенации римской записи 
- десятков и римской записи единиц этого числа. Например, `47 = 40 + 7 = XL + VII = XLVII`.
