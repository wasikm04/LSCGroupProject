from app.algorithm.roundRobinAlgorithm import RoundRobinAlgorithm
from app.algorithm.loadBalancingAlgorithm import LoadBalancingAlgorithm
import configparser


class AlgorithmManager:

    CONFIG_PATH = 'config.ini'

    def __init__(self, machines):
        self.algorithm = self.loadAlgorithmModeFromConfigFile(machines)

    def assignMachineForTask(self):
        return self.algorithm.assignNewMachineForTask()


    def loadAlgorithmModeFromConfigFile(self, machines):
        config = configparser.ConfigParser()
        config.read(AlgorithmManager.CONFIG_PATH)
        mode = config['scheduler']['algorithm']
        healthCheck = True if config['scheduler']['healthCheck'] == 'ON' else False
        if mode == 'RR':
            return RoundRobinAlgorithm(machines, healthCheck)
        if mode == 'LB':
            return LoadBalancingAlgorithm(machines, healthCheck)
        raise Exception('No algorithm defined for {} abbreviation'.format(mode))
