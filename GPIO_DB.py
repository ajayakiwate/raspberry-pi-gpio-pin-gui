import sqlite3
import json

#con = sqlite3.connect('rpi_GPIO_GUI_01.db')
#cur=con.cursor()
#
#cur.execute("CREATE TABLE IF NOT EXISTS gpio(pin INTEGER PRIMARY KEY, status INTEGER)")
#
#cur.execute("""
#            INSERT INTO gpio(pin, status) VALUES
#            (1,0),
#            (2,0),
#            (3,0),
#            (4,0),
#            (5,0),
#            (6,0),
#            (7,0),
#            (8,0),
#            (9,0),
#            (10,0),
#            (11,0),
#            (12,0),
#            (13,0),
#            (14,0),
#            (15,0),
#            (16,0),
#            (17,0),
#            (18,0),
#            (19,0),
#            (20,0),
#            (21,0),
#            (22,0),
#            (23,0),
#            (24,0),
#            (25,0),
#            (26,0)
#            """)
#con.commit()

try:
    con = sqlite3.connect('rpi_GPIO_GUI_01.db')
    cur=con.cursor()
    
    cur.execute("SELECT * FROM gpio")
    
    data = cur.fetchall()
    con.commit()
    
    d={}
    for x in data:
        d[x[0]]=x[1]
        
    print(d)

    m={'success':True, 'message': d}
    print(m)

    json_object = json.dumps(m)

    print(json_object)
   
except:
    m={'success':False}
    json_object = json.dumps(m)
    print(json_object)

    