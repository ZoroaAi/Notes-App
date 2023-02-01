from flask import Blueprint ,render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        # Gets note from HTML
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short', category ='Error')
        else:
            # Generate schema for the note
            new_note = Note(data = note, user_id = current_user.id)
            # Add Note to Database
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added', category='Success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    # Expecting a JSON from index.js file
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})
