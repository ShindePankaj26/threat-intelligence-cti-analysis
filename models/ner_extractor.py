import re


class CTINERExtractor:
    """
    Simple CTI Named Entity Recognition Extractor
    """

    def __init__(self):
        print("CTI NER Extractor Initialized")

    def extract_entities(self, text):

        entities = {
            "ip_addresses": [],
            "domains": [],
            "hashes": [],
            "malware": [],
            "threat_actors": []
        }

        # Extract IP addresses
        ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        entities["ip_addresses"] = re.findall(ip_pattern, text)

        # Extract domains
        domain_pattern = r'\b[a-zA-Z0-9.-]+\.(com|net|org|io|ru|cn)\b'
        domains = re.findall(domain_pattern, text)

        entities["domains"] = list(set(domains))

        # Malware keywords
        malware_keywords = [
            "ransomware",
            "trojan",
            "worm",
            "botnet",
            "malware"
        ]

        for keyword in malware_keywords:
            if keyword in text.lower():
                entities["malware"].append(keyword)

        return entities

    def extract_all_entities(self, text):
        """
        Wrapper method expected by complete_demo.py
        """

        return self.extract_entities(text)
