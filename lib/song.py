import sqlite3

CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = ''' 
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
            );
        '''

        CURSOR.execute(sql)
        CONN.commit()



    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
    
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

    @classmethod
    def close_connection(cls):
        CURSOR.close()
        CONN.close()
    
    

        

# Create the table in the new database
Song.create_table()



hello = Song("Hello", "25")
hello.save()

despacito = Song("Despacito", "Vida")
despacito.save()


highrise = Song("miondoko", "alaar")
# Close the connection when you're done
Song.close_connection()