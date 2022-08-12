"""
Job Enum
"""

from enum import Enum


class Job(str, Enum):
    """
    Job Enum
    """
    # Tanks
    PALADIN = 'PLD'
    WARRIOR = 'WAR'
    DARK_KNIGHT = 'DRK'
    GUN_BREAKER = 'GNB'
    # Healer
    WHITE_MAGE = 'WHM'
    SCHOLAR = 'SCH'
    ASTROLOGIAN = 'AST'
    SAGE = 'SGE'
    # Melee DPS
    MONK = 'MNK'
    DRAGOON = 'DRG'
    NINJA = 'NIN'
    SAMURAI = 'SAM'
    REAPER = 'RPR'
    # Physical Ranged DPS
    BARD = 'BRD'
    MACHINIST = 'MCH'
    DANCER = 'DNC'
    # Magical Ranged DPS
    BLACK_MAGE = 'BLM'
    SUMMONER = 'SMN'
    RED_MAGE = 'RDM'
    BLUE_MAGE = 'BLU'
    # Domain of the Hand
    CARPENTER = 'CRP'
    BLACKSMITH = 'BSM'
    ARMORER = 'ARM'
    GOLDSMITH = 'GSM'
    LEATHERWORKER = 'LTW'
    WEAVER = 'WVR'
    ALCHEMIST = 'ALC'
    CULINARIAN = 'CUL'
    # Domain of the Land
    MINER = 'MIN'
    BOTANIST = 'BTN'
    FISHER = 'FSH'

    def __str__(self):
        """
        Returns the three letter abbreviation of the job
        """
        return self.value

    def get_abbreviation(self):
        """
        Returns the three letter abbreviation of the job
        """
        return self.value
