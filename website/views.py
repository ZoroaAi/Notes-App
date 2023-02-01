from flask import Blueprint ,render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

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