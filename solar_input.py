# coding: utf-8
# license: GPLv3
import numpy as np
import matplotlib.pyplot as plt


from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    Type,r,color,m,x,y,Vx,Vy = map(str, line.split())
    star.R=float(r)
    star.color=color
    star.m=float(m)
    star.x=float(x)
    star.y=float(y)
    star.Vx=float(Vx)
    star.Vy=float(Vy)


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    Type, r, color, m, x, y, Vx, Vy = map(str, line.split())
    planet.R = float(r)
    planet.color = color
    planet.m =float(m)
    planet.x = float(x)
    planet.y = float(y)
    planet.Vx = float(Vx)
    planet.Vy = float(Vy)



def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            #print(out_file, "%s %d %s %f" % ('1', 2, '3', 4.5))
            out_file.write(str(obj.type)+' '+str(obj.R)+str(obj.color)+str(obj.m)+' '+str(obj.x)+' '+str(obj.y)+str(obj.Vx)+str(obj.Vy)+'\n')
        out_file.close()
def write_space_objects_data_to_file_stats(output_filename_stats, space_objects, T):
    """Сохраняет данные о космических объектах в файл статистики.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename_stats, 'a') as out_file:
        if T % 10 == 0:
            for obj in space_objects:
                out_file.write(obj.type + ' ' + str(obj.R) + ' ' + str(obj.color) + ' ' + str(obj.m)
                               + ' ' + str(obj.x) + ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(
                    obj.Vy) + ' ' + str(T)
                               + '\n')
            # FIXME: should store real values
        out_file.close()
def build_graph(filename_stats):
    """Строит график
    """

    T = []
    V = []
    X = []
    Y = []
    R = []
    with open(filename_stats) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":
                X.append(round(float(line.split()[4].lower())))
                Y.append(round(float(line.split()[5].lower())))
            elif object_type == "planet":
                T.append(float(line.split()[8].lower()))
                V.append(((float(line.split()[6].lower())) ** 2 + (float(line.split()[7].lower())) ** 2) ** 0.5)
                R.append(((X[-1] - round(float(line.split()[4].lower()))) ** 2 + (
                            Y[-1] - round(float(line.split()[5].lower()))) ** 2) ** 0.5)

        data_t = np.array(T)
        data_vx = np.array(V)
        data_r = np.array(R)



        sp1 = plt.subplot(221)
        sp1.plot(data_t, data_vx)
        sp1.set_title('V OT t', fontsize=8, fontweight="bold")
        sp1.grid(True)
        xax = sp1.get_xaxis()
        xlabels = xax.get_ticklabels()
        for label in xlabels:
            # размер шрифта подписей делений оси OX
            label.set_fontsize(8)


        sp2 = plt.subplot(222)
        sp2.plot(data_t, data_r)
        sp2.set_title('R OT t', fontsize=8, fontweight="bold")
        sp2.grid(True)
        xax = sp2.get_xaxis()
        xlabels = xax.get_ticklabels()
        for label in xlabels:
            # размер шрифта подписей делений оси OX
            label.set_fontsize(8)

        sp3 = plt.subplot(223)
        sp3.plot(data_r, data_vx)
        sp3.set_title('V(R)', fontsize=8, fontweight="bold")
        sp3.grid(True)
        xax = sp3.get_xaxis()
        xlabels = xax.get_ticklabels()
        for label in xlabels:
            # поворот подписей деленений оси OX
            label.set_rotation(45)
            # размер шрифта подписей делений оси OX
            label.set_fontsize(14)

        plt.show()

def clear_file_stats(filename_stats):
    file_stats = open(filename_stats, 'w')
    file_stats.write('')
    file_stats.close()


# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
