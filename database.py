import sqlite3


class Database:
    def __init__(self):

         # User Database
        self.userConnection = sqlite3.connect('users.db')
        self.userCursor = self.userConnection.cursor()

        # Sports Database
        self.sportsConnection = sqlite3.connect('sports.db')
        self.sportsCursor = self.sportsConnection.cursor()

        # Arts Database
        self.artsConnection = sqlite3.connect('arts.db')
        self.artsCursor = self.artsConnection.cursor()

        # Clubs Database
        self.clubsConnection = sqlite3.connect('clubs.db')
        self.clubsCursor = self.clubsConnection.cursor()

        # Community Service Database
        self.communityServiceConnection = sqlite3.connect('communityservice.db')
        self.communityServiceCursor = self.communityServiceConnection.cursor()

        # Achievements Database
        self.achievementsConnection = sqlite3.connect('achievement.db')
        self.achievementsCursor = self.achievementsConnection.cursor()

        # Classes Database
        self.classesConnection = sqlite3.connect('classes.db')
        self.classesCursor = self.classesConnection.cursor()

        self.create_database()

    def create_database(self):

        """Create users table"""

        self.userCursor.execute(
            "CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, name varchar(55) NOT NULL, grade varchar(55) NOT NULL, classname varchar(55) NOT NULL, school varchar(55) NOT NULL, image BLOB, facebook text NULL, twitter text NULL, instagram text NULL)"
            )

        self.userConnection.commit()

        """Create sports table"""

        self.sportsCursor.execute(
            "CREATE TABLE IF NOT EXISTS sports(id integer PRIMARY KEY AUTOINCREMENT, title varchar(55) NOT NULL, description varchar(255) NOT NULL)"
            )

        self.sportsConnection.commit()

        """Create arts table"""

        self.artsCursor.execute(
            "CREATE TABLE IF NOT EXISTS arts(id integer PRIMARY KEY AUTOINCREMENT, title varchar(55) NOT NULL, description varchar(255) NOT NULL)"
            )

        self.artsConnection.commit()

        """Create clubs table"""

        self.clubsCursor.execute(
            "CREATE TABLE IF NOT EXISTS clubs(id integer PRIMARY KEY AUTOINCREMENT, title varchar(55) NOT NULL, description varchar(255) NOT NULL)"
            )

        self.clubsConnection.commit()

        """Create community service table"""

        self.communityServiceCursor.execute(
            "CREATE TABLE IF NOT EXISTS community_service(id integer PRIMARY KEY AUTOINCREMENT, title varchar(55) NOT NULL, description varchar(255) NOT NULL)"
            )

        self.communityServiceConnection.commit()

        """Create achievements table"""

        self.achievementsCursor.execute(
            "CREATE TABLE IF NOT EXISTS achievements(id integer PRIMARY KEY AUTOINCREMENT, title varchar(55) NOT NULL, description varchar(255) NOT NULL)"
            )

        self.achievementsConnection.commit()

        """Create classes table"""

        self.classesCursor.execute(
            "CREATE TABLE IF NOT EXISTS classes(id integer PRIMARY KEY AUTOINCREMENT, title varchar(55) NOT NULL, description varchar(255) NOT NULL)"
            )

        self.classesConnection.commit()

    def addUser(self, name, grade, classname, school, image, facebook, twitter, instagram):
        self.userCursor.execute(
            "INSERT INTO users(name, grade, classname, school, image, facebook, twitter, instagram) VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (name, grade, classname, school, sqlite3.Binary(image), facebook, twitter, instagram))
        self.userConnection.commit()
        print(name, grade, classname, school, image)

    def updateUser(self, name, grade, classname, school, image, facebook, twitter, instagram, prim_key):
        """Update user item"""
        self.userCursor.execute("UPDATE users SET name=?, grade=?, classname=?, school=?, image=?, facebook=?, twitter=?, instagram=? WHERE id=?", (name, grade, classname, school, sqlite3.Binary(image), facebook, twitter, instagram, prim_key))

        self.userConnection.commit()
    
    def obtainUser(self):
        userData = self.userCursor.execute("SELECT id, name, grade, classname, school, image, facebook, twitter, instagram FROM users").fetchall()

        return userData

    def createItem(self, title, description, category):
        cursor_map = {
            'Sports': (self.sportsCursor, self.sportsConnection),
            'Arts': (self.artsCursor, self.artsConnection),
            'Clubs': (self.clubsCursor, self.clubsConnection),
            'Community Service': (self.communityServiceCursor, self.communityServiceConnection),
            'Achievements': (self.achievementsCursor, self.achievementsConnection),
            'Classes': (self.classesCursor, self.classesConnection)
        }

        cursor, connection = cursor_map.get(category, (self.classesCursor, self.classesConnection))
        cursor.execute("INSERT INTO {}(title, description) VALUES(?, ?)".format(category.lower().replace(" ", "_")), (title, description))
        connection.commit()

    def obtainItems(self, category):
        cursor_map = {
            'Sports': self.sportsCursor,
            'Arts': self.artsCursor,
            'Clubs': self.clubsCursor,
            'Community Service': self.communityServiceCursor,
            'Achievements': self.achievementsCursor,
            'Classes': self.classesCursor
        }

        cursor = cursor_map.get(category, self.classesCursor)
        items = cursor.execute("SELECT id, title, description FROM {}".format(category.lower().replace(" ", "_"))).fetchall()
        return items
        
    def deleteItems(self, prim_key, category):
        cursor_map = {
            'Sports': (self.sportsCursor, self.sportsConnection),
            'Arts': (self.artsCursor, self.artsConnection),
            'Clubs': (self.clubsCursor, self.clubsConnection),
            'Community Service': (self.communityServiceCursor, self.communityServiceConnection),
            'Achievements': (self.achievementsCursor, self.achievementsConnection),
            'Classes': (self.classesCursor, self.classesConnection)
        }

        cursor, connection = cursor_map.get(category, (self.classesCursor, self.classesConnection))
        cursor.execute("DELETE FROM {} WHERE id=?".format(category.lower().replace(" ", "_")), (prim_key,))
        connection.commit()

    def updateItems(self, title, description, category, prim_key):

        cursor_map = {
            'Sports': (self.sportsCursor, self.sportsConnection),
            'Arts': (self.artsCursor, self.artsConnection),
            'Clubs': (self.clubsCursor, self.clubsConnection),
            'Community Service': (self.communityServiceCursor, self.communityServiceConnection),
            'Achievements': (self.achievementsCursor, self.achievementsConnection),
            'Classes': (self.classesCursor, self.classesConnection)
        }

        cursor, connection = cursor_map[category]
        cursor.execute("UPDATE {} SET title=?, description=? WHERE id=?".format(category.lower().replace(" ", "_")), (title, description, prim_key))
        connection.commit()



    def close_db_connection(self):

        self.sportsConnection.close()

        self.artsConnection.close()

        self.clubsConnection.close()

        self.communityServiceConnection.close()

        self.achievementsConnection.close()

        self.classesConnection.close()

        self.userConnection.close()
