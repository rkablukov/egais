# ЕГАИС SDK для python

ЕГАИС SDK - это пакет, который содержит в себе набор классов и методов, которые позволяют преобразовывать xml документы ЕГАИС в структуры данных python и обратно. 

Модуль сгенерирован с помощью [generateDS.py](https://github.com/ricksladkey/generateDS) по схемам XSD ЕГАИС.

Протестирован на python3.

### Установка

Установка модуля простая с использованием инструмента pipenv.

```
$ pipenv install git+https://github.com/rkablukov/egais.git#egg=egais
```

### Генерация модуля

Для начала клонируем репозиторий

```
$ git clone https://github.com/rkablukov/egais.git
$ cd egais
```

Создадим виртуальное окружение и установим зависимости

```
$ pipenv --three install
```

Схемы находятся в папке xsd. При необходимости можно сопировать туда свежие схемы документов ЕГАИС.

Для генерации модуля выполните следующие команды

```
$ pipenv shell
$ generateDS.py -o egais/egais.py -s egais/egaissubs.py --use-old-simpletype-validators --external-encoding='utf-8' --silence ./xsd/WB_DOC_SINGLE_01.xsd
```

### Примеры использования

Парсинг документа и чтение реквизитов.

```
>>> import egais
>>> wb = egais.parse('WayBill_v3.xml')
>>> print(wb.Owner.FSRAR_ID)
010000000435
>>>
```

Создание документа и экспорт xml в файл.

```
>>> import egais
>>> 
>>> doc = egais.Documents()
>>> doc.Owner = egais.SenderInfo(FSRAR_ID='123456789012')
>>> doc.Document = egais.DocBody()
>>> 
>>> queryFormF2 = egais.QueryFormF1F2(FormRegId='FB-000000005664278')
>>> doc.Document.QueryFormF2 = queryFormF2
>>> 
>>> with open("QueryFormF1F2.xml", "w") as f:
>>>     doc.export(f, 0)
>>>
```
