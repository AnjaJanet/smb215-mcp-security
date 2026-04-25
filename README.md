# Sécurité MCP - Projet SMB215

Ce projet contient des démonstrations de vulnérabilités de sécurité dans les serveurs MCP (Model Context Protocol). Il est organisé en deux parties principales : des exemples en environnement de développement (Non-production) et des exemples en environnement de production.

## Structure du projet

### Dossier Non-production/
Ce dossier contient des exemples de vulnérabilités utilisant FastMCP avec une calculatrice simple.

- `fastmcp_calculator.py` : Calculatrice sécurisée exposant des opérations de base (multiplication, addition, soustraction, division) en tant qu'outils MCP.
- `fastmcp_calculator_prompt_injection.py` : Version de la calculatrice avec une charge utile d'injection de prompt dans la docstring, pour tester la sécurité des agents et des politiques.
- `fastmcp_calculator_tool_abuse.py` : Version de la calculatrice avec une charge utile d'abus d'outil dans la docstring, pour tester les garde-fous.

### Dossier Production/
Ce dossier contient des exemples de vulnérabilités dans un environnement simulant la production, utilisant un serveur MCP pour git et everything. 

#### Server MCP Git
Dans ce cas, dans le dossier MCP officiel il suffit de remplacer le contenu de servers/src/git/src/mcp_server_git/server.py avec l'une des versions suivantes.
- `server_command_injection.py` : Démonstration d'injection de commande dans le serveur git MCP.
- `server_data_extraction.py` : Démonstration d'extraction de données sensibles via le serveur git MCP.
- `server_name_typosquatting.py` : Démonstration de typosquatting sur les noms de serveurs MCP.

### Server MCP everything
// à venir

## Prérequis

- Python 3.11+ (3.12 recommandé)
- Dépendances : `fastmcp`, `mcp` et autres listées dans `requirements.txt`

## Installation

Installez les dépendances avec :

```bash
pip install -r requirements.txt
```

## Utilisation

Pour exécuter un serveur de démonstration (transport STDIO) :

```bash
python fastmcp_calculator.py
```

Envoyez ensuite des messages JSON via stdin/stdout selon le protocole MCP, ou utilisez une bibliothèque cliente compatible MCP.

### Exemple simple

```bash
echo '{"query":"multiply", "args":{"a":5,"b":7}}' | python fastmcp_calculator.py
```

## Note sur l'évaluation de sécurité

Les variantes `*_prompt_injection.py` et `*_tool_abuse.py` sont intentionnellement conçues pour tester le comportement des agents et des défenses contre les injections. **Ne les utilisez pas en production.** Ces exemples sont uniquement à des fins éducatives pour comprendre et prévenir les vulnérabilités de sécurité dans les serveurs MCP.
