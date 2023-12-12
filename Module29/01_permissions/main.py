# TODO здесь писать код
import functools
from collections.abc import Callable


def check_permission(user: str):
    """
    Декоратор с имени пользователя
    """
    def check_permission_decorator(func: Callable) -> Callable:
        """
        Декоратор функции проверяет
        пользователя на доступ совершения действий
        """
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {func_name}'.format(
                    func_name=func.__name__))
        return wrapped
    return check_permission_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    """Функция удаление сайта"""
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    """Функция добавления комментария"""
    print('Добавляем комментарий')


delete_site()
add_comment()
