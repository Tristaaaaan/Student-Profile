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

        if category == 'Sports':
            """Create an item for sports"""
            self.sportsCursor.execute(
                "INSERT INTO sports(title, description) VALUES(?, ?)", (title, description,))
            self.sportsConnection.commit()

        elif category == 'Arts':
            """Create an item for arts"""
            self.artsCursor.execute(
                "INSERT INTO arts(title, description) VALUES(?, ?)", (title, description,))
            self.artsConnection.commit()

        elif category == 'Clubs':
            """Create an item for clubs"""
            self.clubsCursor.execute(
                "INSERT INTO clubs(title, description) VALUES(?, ?)", (title, description,))
            self.clubsConnection.commit()
        
        elif category == 'Community Service':
            """Create an item for community service"""
            self.communityServiceCursor.execute(
                "INSERT INTO community_service(title, description) VALUES(?, ?)", (title, description,))
            self.communityServiceConnection.commit()

        elif category == 'Achievements':
            """Create an item for achievements"""
            self.achievementsCursor.execute(
                "INSERT INTO achievements(title, description) VALUES(?, ?)", (title, description,))
            self.achievementsConnection.commit()

        else:
            """Create an item for classes"""
            self.classesCursor.execute(
                "INSERT INTO classes(title, description) VALUES(?, ?)", (title, description,))
            self.classesConnection.commit()

    def obtainItems(self, category):

        """Get items from the sports category"""
        if category == 'Sports':

            sportsItems = self.sportsCursor.execute(
                "SELECT id, title, description FROM sports").fetchall()

            return sportsItems

            """Get items from the arts category"""
        elif category == 'Arts':

            artsItems = self.artsCursor.execute(
                "SELECT id, title, description FROM arts").fetchall()

            return artsItems   

            """Get items from the arts clubs"""
        elif category == 'Clubs':

            clubItems = self.clubsCursor.execute(
                "SELECT id, title, description FROM clubs").fetchall()

            return clubItems   


            """Get items from the arts community service"""
        elif category == 'Community Service':

            communityServiceItems = self.communityServiceCursor.execute(
                "SELECT id, title, description FROM community_service").fetchall()

            return communityServiceItems   


            """Get items from the arts achievements"""
        elif category == 'Achievements':

            achievementsItems = self.achievementsCursor.execute(
                "SELECT id, title, description FROM achievements").fetchall()

            return achievementsItems   
        

            """Get items from the arts classes"""
        else:

            classItems = self.classesCursor.execute(
                "SELECT id, title, description FROM classes").fetchall()

            return classItems   
        
    def deleteItems(self, prim_key, category):

        if category == 'Sports':
            """Delete a sports item"""
            self.sportsCursor.execute("DELETE FROM sports WHERE id=?", (prim_key,))

            self.sportsConnection.commit()

        elif category == 'Arts':
            """Delete a arts item"""
            self.artsCursor.execute("DELETE FROM arts WHERE id=?", (prim_key,))

            self.artsConnection.commit()

        elif category == 'Clubs':
            """Delete a clubs item"""
            self.clubsCursor.execute("DELETE FROM clubs WHERE id=?", (prim_key,))

            self.clubsConnection.commit()
        
        elif category == 'Community Service':
            """Delete a community service item"""
            self.communityServiceCursor.execute("DELETE FROM community_service WHERE id=?", (prim_key,))

            self.communityServiceConnection.commit()

        elif category == 'Achievements':
            """Delete a achievements item"""
            self.achievementsCursor.execute("DELETE FROM achievements WHERE id=?", (prim_key,))

            self.achievementsConnection.commit()

        else:
            """Delete a class item"""
            self.classesCursor.execute("DELETE FROM classes WHERE id=?", (prim_key,))

            self.classesConnection.commit()

    def updateItems(self, title, description, category, prim_key):

        if category == 'Sports':
            """Update a sports item"""
            self.sportsCursor.execute("UPDATE sports SET title=?, description=? WHERE id=?", (title, description, prim_key))

            self.sportsConnection.commit()

        elif category == 'Arts':
            """Update a arts item"""
            self.artsCursor.execute("UPDATE arts SET title=?, description=? WHERE id=?", (title, description, prim_key))

            self.artsConnection.commit()

        elif category == 'Clubs':
            """Update a clubs item"""
            self.clubsCursor.execute("UPDATE clubs SET title=?, description=? WHERE id=?", (title, description, prim_key))

            self.clubsConnection.commit()
        
        elif category == 'Community Service':
            """Update a community service item"""
            self.communityServiceCursor.execute("UPDATE community_service SET title=?, description=? WHERE id=?", (title, description, prim_key))

            self.communityServiceConnection.commit()

        elif category == 'Achievements':
            """Update a achievements item"""
            self.achievementsCursor.execute("UPDATE achievements SET title=?, description=? WHERE id=?", (title, description, prim_key))

            self.achievementsConnection.commit()

        else:
            """Update a class item"""
            self.classesCursor.execute("UPDATE classes SET title=?, description=? WHERE id=?", (title, description, prim_key))

            self.classesConnection.commit()

    def close_db_connection(self):

        self.sportsConnection.close()

        self.artsConnection.close()

        self.clubsConnection.close()

        self.communityServiceConnection.close()

        self.achievementsConnection.close()

        self.classesConnection.close()

        self.userConnection.close()
