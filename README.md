# Threat Intelligence and CTI Analysis Pipeline with NLP/LLMs

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)]()

This project implements a comprehensive pipeline for analyzing Cyber Threat Intelligence (CTI) reports using Natural Language Processing (NLP) and Large Language Models (LLMs). The pipeline automatically extracts indicators of compromise (IOCs), tags MITRE ATT&CK techniques, builds knowledge graphs from unstructured CTI reports, and provides an API for integration with security tools.

**Developed by: Shinde Pankaj**

## 🚀 Features

- **Automated IOC Extraction**: Extracts IPs, domains, email addresses, file hashes (MD5/SHA1/SHA256), CVEs, malware names, and threat actors
- **MITRE ATT&CK Mapping**: Automatically tags reports with ATT&CK tactics and techniques using pattern matching and semantic analysis
- **Relation Extraction**: Identifies relationships between threat entities (e.g., "APT29 uses Backdoor.X")
- **Knowledge Graph Construction**: Builds a queryable graph representation of threat intelligence with confidence scoring
- **RESTful API**: Provides endpoints for processing CTI reports and querying threat intelligence
- **Cross-Platform Compatibility**: Runs on Windows, macOS, and Linux
- **Extensible Architecture**: Modular design allows for easy customization and extension

## 📁 Project Structure

```
.
├── src/                    # Source code
│   ├── models/            # NLP models for entity and relation extraction
│   ├── kg/                # Knowledge graph construction and management
│   ├── pipelines/         # Main analysis pipeline
│   ├── api/               # REST API interface
│   ├── llm/               # LLM integration framework
│   ├── utils/             # Utility functions
│   └── tests/             # Unit tests
├── data/                  # Sample data and datasets
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── run_pipeline.py        # Cross-platform launcher
├── run_pipeline.sh        # Unix shell script
├── run_pipeline.bat       # Windows batch script
└── README.md              # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Setup

1. **Clone the repository**:
```bash
git clone <repository-url>
cd threat-intelligence-cti-analysis
```

2. **Install required packages**:
```bash
pip install -r requirements.txt
```

3. **Install core dependencies**:
```bash
python install_core_deps.py
```

4. **Download spaCy language model** (optional, for enhanced NLP):
```bash
python -m spacy download en_core_web_sm
```

### Docker Installation (Alternative)

Build and run using Docker:
```bash
docker build -t cti-pipeline .
docker run -p 5000:5000 cti-pipeline
```

## 🚀 Usage

### Cross-Platform Launcher

The project includes cross-platform launch scripts:
- `run_pipeline.py` - Universal Python launcher
- `run_pipeline.sh` - Unix shell script (macOS/Linux)
- `run_pipeline.bat` - Windows batch script

### Command Line Interface

**Run the demo**:
```bash
python run_pipeline.py demo
# or
python src/main.py --mode demo
```

**Start the API server**:
```bash
python run_pipeline.py api
# or
python src/main.py --mode api
```

**Process a CTI report file**:
```bash
python run_pipeline.py process path/to/report.txt
# or
python src/main.py --mode process --input path/to/report.txt --output results.json
```

**Run unit tests**:
```bash
python run_pipeline.py test
# or
python -m unittest src/tests/test_pipeline.py
```

### API Endpoints

Start the API server and access the following endpoints:

- `GET /health` - Health check endpoint
- `POST /analyze` - Analyze a single CTI report
- `POST /analyze_batch` - Analyze multiple CTI reports
- `GET /threat_actor/<actor_name>` - Get information about a threat actor
- `POST /knowledge_graph/query` - Query the knowledge graph
- `GET /knowledge_graph/statistics` - Get knowledge graph statistics
- `GET /knowledge_graph/brief` - Get threat intelligence brief
- `POST /knowledge_graph/save` - Save the knowledge graph to a file

**Example API request**:
```bash
# Analyze a CTI report
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "report_text": "APT29 uses Backdoor.X to target the energy sector",
    "report_id": "report_001"
  }'

# Query threat actor information
curl http://localhost:5000/threat_actor/APT29

# Get knowledge graph statistics
curl http://localhost:5000/knowledge_graph/statistics
```

## 🔧 Core Components

### Named Entity Recognition (NER)
Extracts cyber threat entities using regex patterns:
- **IP Addresses**: IPv4 and IPv6 addresses
- **Domains**: Domain names and URLs
- **Emails**: Email addresses
- **File Hashes**: MD5, SHA1, and SHA256 hashes
- **CVE Identifiers**: Common Vulnerabilities and Exposures
- **Malware Names**: Malware and backdoor names
- **Threat Actors**: APT groups and threat actor names
- **File Paths**: System file paths
- **Registry Keys**: Windows registry keys

### MITRE ATT&CK Tagger
Maps text to MITRE ATT&CK framework:
- **Techniques**: Over 100 ATT&CK techniques (T1059, T1566, etc.)
- **Tactics**: All ATT&CK tactics (TA0001, TA0002, etc.)
- **Pattern Matching**: Matches technique/tactic IDs and names
- **Extensible**: Easy to add new techniques and tactics

### Relation Extractor
Identifies relationships between threat entities:
- **Actor-Malware**: "APT29 uses Backdoor.X"
- **Actor-Target**: "APT29 targets energy sector"
- **Malware-C2**: "Backdoor.X communicates with 192.168.1.100"
- **Malware-Technique**: "Backdoor.X implements T1059"
- **Vulnerability-Exploitation**: "Exploits CVE-2023-12345"

### Knowledge Graph
Builds structured threat intelligence representation:
- **Nodes**: Threat entities with metadata
- **Edges**: Relationships with confidence scores
- **Querying**: Neighbor discovery, entity type filtering, path finding
- **Persistence**: JSON serialization for storage
- **Statistics**: Graph analytics and metrics

### LLM Integration
Interfaces with large language models for advanced analysis:
- **Summarization**: Automatic report summarization
- **Question Answering**: Interactive Q&A about threats
- **Intelligence Briefs**: Automated brief generation
- **Validation**: Information validation to reduce false positives

## 📊 Supported Datasets

The pipeline works with various CTI data sources:
- **CTI-HAL**: Real CTI incident reports with ATT&CK annotations
- **MISP Feeds**: IP/URL/hash blocklists and threat intelligence
- **Security Blogs**: Unstructured threat reports and analysis
- **MITRE ATT&CK**: Official ATT&CK framework data
- **Custom Formats**: JSON, CSV, and plain text reports

## 🎯 Use Cases

- **Security Operations Centers (SOCs)**: Automate threat report analysis
- **Threat Intelligence Platforms**: Enrich CTI with structured data
- **Incident Response**: Quickly extract IOCs from incident reports
- **Threat Hunting**: Identify patterns across multiple reports
- **Research**: Analyze threat actor behaviors and TTPs

## 🔒 Security Considerations

- **Data Privacy**: Process CTI locally without sending data to external services
- **Validation**: Built-in validation to reduce false positives
- **Auditing**: Track source reports for extracted intelligence
- **Confidence Scoring**: Rate confidence in extracted relationships

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m unittest discover src/tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- MITRE ATT&CK framework for threat intelligence standardization
- spaCy for NLP capabilities
- NetworkX for graph analysis
- Flask for API framework
- OpenAI for LLM integration framework

## 📞 Support

For issues, questions, or feedback, please:
1. Check existing issues on GitHub
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 🔄 Future Enhancements

- **Machine Learning Integration**: Fine-tuned transformer models for NER and classification
- **Advanced Graph Analytics**: Link prediction and community detection
- **Real-time Processing**: Streaming CTI feed ingestion
- **Visualization**: Interactive graph visualization dashboard
- **Multi-language Support**: NLP for non-English CTI reports
- **STIX/TAXII Integration**: Standardized threat intelligence sharing# threat-intelligence-cti-analysis
