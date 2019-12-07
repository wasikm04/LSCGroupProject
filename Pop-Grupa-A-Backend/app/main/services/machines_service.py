from app.main import db
from app.main.model.Machine import Machine
import app.main.repositories.machines_repository as machine_repository


def get_cluster_node_machine_list(cluster_node_id):
    machine_list = machine_repository.get_machines_for_cluster_node(cluster_node_id)
    if not machine_list:
        return {
                'status': 'failure',
                'message': 'Cluster node with id = {cluster_node_id} has no machines assigned'
                }, 204

    return machine_list, 200


def save_changes(data):
    db.session.add(data)
    db.session.commit()