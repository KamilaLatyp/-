# используется для сортировки
# Выполнила: Латыпова К.Н. ИУ5-53Б

from operator import itemgetter


class Disk:
    """CD-диск"""
    def __init__(self, id, name, size, library_id):
        self.id = id
        self.name = name
        self.size = size
        self.library_id = library_id

class Library:
    """Библиотка CD-дисков"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DiskLibrary():
    """Для реализации связи многие-ко-многим"""
    def __init__(self, library_id, disk_id ):
        self.library_id = library_id
        self.disk_id = disk_id


libraries = [
    Library(1, 'Музыка'),
    Library(2, 'Аудиокниги'),
    Library(3, 'Музыка (другое)'),
    Library(4, 'Аудиокниги (другое)'),
]
disks = [
    Disk(1, 'Антонио Вивальди. Летняя гроза', 650, 1),
    Disk(2, 'Иоганн Себастьян Бах. Шутка', 800, 2),
    Disk(3, 'Дэнни Элфман и «Крупная рыба»', 700, 3),
    Disk(4, 'Физика', 700, 4),
    Disk(5, 'Аналитическая геометрия', 700, 2),
    Disk(6, 'Кэсс Морган. Сотня', 800, 1),

]
disks_libraries = [
    DiskLibrary(1, 1),
    DiskLibrary(1, 2),
    DiskLibrary(1, 3),
    DiskLibrary(2, 4),
    DiskLibrary(2, 5),
    DiskLibrary(2, 6),
    DiskLibrary(3, 1),
    DiskLibrary(3, 2),
    DiskLibrary(3, 3),
    DiskLibrary(4, 4),
    DiskLibrary(4, 5),
    DiskLibrary(4, 6),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(e.name, e.size, d.name)
                   for d in libraries
                   for e in disks
                   if e.library_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_tdisk = [(d.name, ed.library_id, ed.disk_id)
                          for d in libraries
                          for ed in disks_libraries
                          if d.id == ed.library_id]

    many_to_many = [(e.name, e.size, library_name)
                    for library_name, library_id, disk_id in many_to_many_tdisk
                    for e in disks if e.id == disk_id]

    print('РК1 Выполнила Латыпова К.Н. ИУ5-53Б')
    print()
    print('Задание B1')
    res_b1 = []
    for i in one_to_many:
        if i[0][0] == "А":
            res_b1.append((i[0], i[2]))
    print(res_b1)

    print()
    print('Задание B2')
    res_b2_unsorted = []
    for d in libraries:
        d_disks = list(filter(lambda i: i[2] == d.name, one_to_many))
    if len(d_disks) > 0:
        d_size = [size for _, size, _ in d_disks]
        d_size_min = min(d_size)
        res_b2_unsorted.append((d.name, d_size_min))
    res_b2 = sorted(res_b2_unsorted, key=itemgetter(1), reverse=False)
    print(res_b2)

    print()
    print('Задание B3')
    res_b3 = []
    for i in one_to_many:
        res_b3.append((i[0], i[2]))
    res_b3_sorted = sorted(res_b3, key=itemgetter(0))
    print(res_b3_sorted)


if __name__ == '__main__':
    main()