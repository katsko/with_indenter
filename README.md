# Использование оператора *with* (контекстный менеджер) для создания отступов в тексте

Версия python: 3.6+

Данный код является примером применения контекстного менеджера в python для форматирования текста.

Сам механизм реализован в классе Indenter (indenter.py).

## Использование:

Для создания отступа в тексте необходимо войти в блок оператора with и вызвать метод *print* экземпляра класса Indenter:

```python
with Indenter() as indent:
    indent.print('hi!')
```

Выведится:

```
    hi!
```

Вариант с вложенным *with*:


```python
with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
```

Выведится:

```
    hi!
        hello
```

При выходе из вложенного блока, отступ уменьшается:

```python
with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
    indent.print('bonjour')
```

Выведится:

```
    hi!
        hello
    bonjour
```

## Запуск:

```
python ./main.py
```

## Вывод программы:

```

    hi!
        hello

        hello friend
            bonjour les amis
    hey

```

## Тесты:

```
python ./test.py
```

или

```
python -m unittest test
```
