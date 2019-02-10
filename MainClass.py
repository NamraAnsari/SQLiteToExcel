import ManageEntry


class MainClass:

    @staticmethod
    def data_entry():
        name = input('Enter your name: ')
        pos = input('Enter your position: ')
        student1 = ManageEntry.ManageStudentEntry()
        student1.insert_entry(name, pos)
        student1.view_entry()


MainClass.data_entry()
