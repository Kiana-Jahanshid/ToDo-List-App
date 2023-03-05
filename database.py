import sqlite3 

class Database :
    def __init__(self):
        self.con = sqlite3.connect("todolist.db")
        self.cursor = self.con.cursor()


    def get_tasks_from_db(self):
        tasks = self.cursor.execute("SELECT * FROM tasks").fetchall()
        return tasks 
    
    def add_new_task(self , new_title , new_description ,is_done ,priority ,  new_date , new_time):
        try:
            self.cursor.execute(f"INSERT INTO tasks(title , description , is_done ,priority, date , time) VALUES('{new_title}' , '{new_description}' , '{is_done}' ,'{priority}', '{new_date}', '{new_time}')")
            self.con.commit() 
            return True
        except:
            return False
        


    def remove_task(self , id):
        self.cursor.execute(f"DELETE FROM tasks WHERE ID={id}")
        self.con.commit()



    def task_done(self , task_title):
        self.cursor.execute(f"UPDATE tasks SET is_done ={1} WHERE title ='{task_title}' ")
        self.con.commit()
        

    def sort(self):
        sorted= self.cursor.execute(f"SELECT * FROM tasks ORDER BY is_done ASC").fetchall()
        return sorted