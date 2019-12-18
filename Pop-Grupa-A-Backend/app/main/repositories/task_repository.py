from app.main import db
from app.main.model.ComputationTask import ComputationTask
from app.main.model.ComputationStatus import ComputationStatus


def get_tasks_for_user(userId):
    return ComputationTask.query.filter_by(user_id=userId).order_by(ComputationTask.id).all()

def get_task_for_task_id(id=id):
    return ComputationTask.query.filter_by(id=id).first()

def get_status(task_id):
    return ComputationTask.query.filter_by(task_id=task_id).first()['status']

def add_new_task(new_task):
    save_changes(new_task)

def change_task_status(task_id, newStatus):
    try:
        task = get_task_for_task_id(task_id)
        task.status = newStatus
        save_changes(task)
    except:
        raise Exception

def save_changes(data):
    db.session.add(data)
    db.session.commit()
