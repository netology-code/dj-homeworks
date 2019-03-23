from django.template import Library


def create_grad(down_limit, up_limit, steps):
    """
    Создать набор интарвалов и соответствующих цветов градиента от зеленого к красному
        :param down_limit: нижний предел интервалов
        :param up_limit: верхний предел интервалов
        :param steps: количество интервалов
        :return список словарей, содержащих пределы интервалов и соответствующие цвета градиента
    """
    step_value = (up_limit - down_limit) / steps
    value_to_color_list = []
    for i in range(steps):
        value_to_color_list.append({
            'up-limit': down_limit + (i + 1) * step_value,
            'down_limit': down_limit + i * step_value,
            'color': f'#{int(255 if i > steps / 2 else 255 * i / (steps / 2)):02X}{int(255 if i <= steps / 2 else 255 - 255 * (i * 2 - steps) / steps):02X}44'
        })
    value_to_color_list[0]['down_limit'] = None
    value_to_color_list[-1]['up-limit'] = None
    return value_to_color_list

def create_color_getter(down_limit, up_limit, steps):
    """
    Создать функцию, выдающую цвет в зависимости от интервала, в котором находится полученное значение 
        :param down_limit: нижний предел интервалов
        :param up_limit: верхний предел интервалов
        :param steps: количество интервалов
        :return функция, выдающую цвет в зависимости от интервала, в котором находится полученное значение 
    """
    value_to_color_list = create_grad(down_limit, up_limit, steps)

    def get_cell_color(cell_value):
        """
        Получить цвет в зависимости от интервала, в котором находится переданное значение 
            :param cell_value: переданное значение
            :return цвет в формате "#FFFFFF", соответствующий интервалу, в котором находится переданное значение
        """
        try:

            cell_value = float(cell_value)

            for item in value_to_color_list:
                if (item['down_limit'] is None or item['down_limit'] <= cell_value) and (item['up-limit'] is None or cell_value < item['up-limit']):
                    return item['color']

        except ValueError:
            return ''

    return get_cell_color

register = Library()
register.filter(name='get_cell_color', filter_func=create_color_getter(-5, 5, 10))
