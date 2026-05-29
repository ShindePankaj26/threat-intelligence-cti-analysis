class AttackTagger:
    """
    Simple MITRE ATT&CK Tagger
    """

    def __init__(self):
        print("Attack Tagger Initialized")

    def tag_attack_techniques(self, text):

        techniques = {}

        keywords = {
            "phishing": ("T1566", "Phishing"),
            "powershell": ("T1059", "Command and Scripting Interpreter"),
            "credential": ("T1003", "Credential Dumping"),
            "malware": ("T1105", "Ingress Tool Transfer"),
            "ransomware": ("T1486", "Data Encrypted for Impact"),
            "command and control": ("T1071", "Application Layer Protocol"),
            "persistence": ("T1053", "Scheduled Task")
        }

        text = text.lower()

        for keyword, (tech_id, tech_name) in keywords.items():

            if keyword in text:

                techniques[tech_id] = tech_name

        return techniques

    def tag_report(self, text):

        techniques = self.tag_attack_techniques(text)

        tactics = [
            "Initial Access",
            "Execution",
            "Persistence",
            "Command and Control"
        ]

        return {
            "techniques": techniques,
            "tactics": tactics
        }
