from urllib import request
from flask import Flask, render_template, redirect, url_for,g, request
from database import connect_to_database, getDatabase

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/home')
# def index():
#     return render_template('home.html')
    

@app.route('/newcontact', methods=["POST","GET"])
def newcontact():
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        contact = request.form['contact']

        db = getDatabase()
        db.execute("INSERT INTO users (firstname, lastname, number) VALUES (?,?,?) ", [firstname, lastname, contact] )
        db.commit()
        return redirect( url_for('newcontact'))

    return render_template('newcontact.html')  

@app.route('/search')    
def search():  
    return render_template('search.html')



@app.route('/getname', methods=["POST","GET"])
def getname():
    db = getDatabase()
    if request.method == "POST":
        searchcolumn = request.form['searchcolumn'].lower()
        searchfor = request.form['searchfor'].lower()
        if searchcolumn == "first":
            searchfor_cursor = db.execute("select * from users where firstname = ? COLLATE NOCASE ",[searchfor])
            name_for = searchfor_cursor.fetchall()
            return render_template('display.html', name_for=name_for)
        elif searchcolumn == "last":
            searchfor_cursor = db.execute("select * from users where lastname = ? COLLATE NOCASE ",[searchfor])
            name_for = searchfor_cursor.fetchall()   
            return render_template('display.html', name_for=name_for)
        else:
            searchfor_cursor = db.execute("select * from users where lasttname = ? COLLATE NOCASE ",[searchfor])
            name_for = searchfor_cursor.fetchall()
            return render_template('display.html', name_for=name_for)
    return "bhaltach challai!"    


@app.route('/updatecontact/<int:id>', methods=["POST","GET"])
def updatecontact(id):
    db = getDatabase()
    if request.method == "POST":
        fname= request.form['fname']
        lname= request.form['lname']
        contact= request.form['contact']
        update_cursor = db.execute("select * from users where id = ?",[id])
        update_row = update_cursor.fetchone()
        # db.execute("UPDATE (firstname,lastname,number) SET (?,?,?) WHERE id = ?" [fname,lname,contact],[id])
        db.execute("update users set firstname=?,lastname=?,number=? where id= ?",(fname,lname,contact,id))
        db.commit()
        return redirect('/search')  
    update_cursor = db.execute("select * from users where id = ?",[id])
    update_row = update_cursor.fetchone()
    return render_template("update.html", update_row = update_row)       
    
 

@app.route('/deletecontact/<int:id>')
def deletecontact(id):
    db = getDatabase()
    db.execute("delete from users where id = ?",[id])
    db.commit()
    return redirect('/search')  




if __name__ == "__main__":
    app.run(debug=True)

