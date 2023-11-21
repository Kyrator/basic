# TODO здесь писать код
class Stack:

    def __init__(self):
        self.__lst_task = []

    def push(self, task):
        self.__lst_task.append(task)

    def pop(self):
        if len(self.__lst_task) == 0:
            return None
        self.__lst_task.pop()

    def __str__(self):
        return "; ".join(self.__lst_task)


class TaskManager:

    def __init__(self):
        self.dct_task = dict()

    def new_task(self, task, key):
        if key not in self.dct_task:
            self.dct_task[key] = Stack()
        self.dct_task[key].push(task)

    def __str__(self):
        response = []
        if self.dct_task:
            for key in sorted(self.dct_task.keys()):
                response.append("{key} {value} \n".format(
                    key=key,
                    value=self.dct_task[key]
                )
                )
        return ''.join(response)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
