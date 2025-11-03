"""
Configuration file for CTI Analysis Pipeline
"""
import os

# Paths
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
MODELS_DIR = os.path.join(PROJECT_ROOT, 'models')
KG_DIR = os.path.join(PROJECT_ROOT, 'kg')

# Model settings
SPACY_MODEL = "en_core_web_sm"

# API settings
API_HOST = "0.0.0.0"
API_PORT = 5000
API_DEBUG = True

# Knowledge graph settings
KG_MAX_NODES_VISUALIZATION = 50

# Confidence thresholds
NER_CONFIDENCE_THRESHOLD = 0.8
RELATION_CONFIDENCE_THRESHOLD = 0.7

# File extensions
SUPPORTED_FILE_EXTENSIONS = ['.txt', '.md', '.json']

# Default entity types
ENTITY_TYPES = [
    'IP_ADDRESS',
    'DOMAIN',
    'EMAIL',
    'MD5_HASH',
    'SHA1_HASH',
    'SHA256_HASH',
    'CVE',
    'MALWARE',
    'THREAT_ACTOR'
]

# ATT&CK tactics
ATTACK_TACTICS = {
    'TA0001': 'Initial Access',
    'TA0002': 'Execution',
    'TA0003': 'Persistence',
    'TA0004': 'Privilege Escalation',
    'TA0005': 'Defense Evasion',
    'TA0006': 'Credential Access',
    'TA0007': 'Discovery',
    'TA0008': 'Lateral Movement',
    'TA0009': 'Collection',
    'TA0011': 'Command and Control',
    'TA0010': 'Exfiltration',
    'TA0040': 'Impact'
}

# Common ATT&CK techniques
ATTACK_TECHNIQUES = {
    'T1059': 'Command and Scripting Interpreter',
    'T1078': 'Valid Accounts',
    'T1190': 'Exploit Public-Facing Application',
    'T1595': 'Active Scanning',
    'T1057': 'Process Discovery',
    'T1036': 'Masquerading',
    'T1071': 'Application Layer Protocol',
    'T1041': 'Exfiltration Over C2 Channel',
    'T1566': 'Phishing',
    'T1204': 'User Execution',
    'T1055': 'Process Injection',
    'T1027': 'Obfuscated Files or Information'
}