import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# CREATE ANNOUNCEMENT
def add_announcement(conn, announcement_data):
    try:
        with conn:
            cursor = conn.cursor()

            query = """
                INSERT INTO ANNOUNCEMENTS
                (
                    announcement_id,
                    title,
                    message,
                    date_posted
                )
                VALUES (?, ?, ?, ?)
            """

            cursor.execute(query, announcement_data)
            conn.commit()

            print("Announcement added!")

    except sqlite3.Error as e:
        print("Error:", e)

# READ ANNOUNCEMENTS
def get_announcements(conn):
    try:
        with conn:
            cursor = conn.cursor()

            query = """
                SELECT * FROM ANNOUNCEMENTS
            """

            cursor.execute(query)

            results = cursor.fetchall()

            return results

    except sqlite3.Error as e:
        print("Error:", e)

# UPDATE ANNOUNCEMENT
def update_announcement(conn, announcement_id, data: dict):
    try:
        with conn:
            cursor = conn.cursor()

            fields = ", ".join([f"{key} = ?" for key in data.keys()])
            values = list(data.values())

            values.append(announcement_id)

            query = f"""
                UPDATE ANNOUNCEMENTS
                SET {fields}
                WHERE announcement_id = ?
            """

            cursor.execute(query, values)
            conn.commit()

            print("Announcement updated!")

    except sqlite3.Error as e:
        print("Error:", e)

# DELETE ANNOUNCEMENT
def delete_announcement(conn, announcement_id):
    try:
        with conn:
            cursor = conn.cursor()

            query = """
                DELETE FROM ANNOUNCEMENTS
                WHERE announcement_id = ?
            """

            cursor.execute(query, (announcement_id,))
            conn.commit()

            print("Announcement deleted!")

    except sqlite3.Error as e:
        print("Error:", e)
