
from webapp.db import db

from webapp.magazine.models import Subj


def save_subject(subject):
    subj = Subj(subject=subject)
    db.session.add(subj)
    db.session.commit()


def hand_create_subject():
    for i in ['Информатика', 'Математика', 'Литература', 'История']:
        subject = i
        save_subject(subject=subject)
