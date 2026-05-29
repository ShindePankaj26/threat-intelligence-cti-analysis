class CTIRelationExtractor:
    """
    Simple CTI Relation Extractor
    """

    def __init__(self):
        print("CTI Relation Extractor Initialized")

    def extract_relations(self, entities):
        """
        Dummy relation extraction
        """

        relations = []

        domains = entities.get("domains", [])

        for domain in domains:
            relations.append({
                "source": "threat_actor",
                "target": domain,
                "relationship": "uses"
            })

        return relations
