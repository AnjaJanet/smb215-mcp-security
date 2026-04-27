# Serveurs MCP Serrure - Démonstrations de Vulnérabilités

Ceci est un serveur de démonstration. Il simule l'ouverture d'une porte d'entrée.

## Fichiers

- `server_vulnerable.py` : C'est la version sans sécurisation de ce serveur. Il est volontairement vulnérable en n'implementant pas de DCR (Dynamic Client Registration). N'importe qui peut utiliser le paramètre origineDemande="Agent" pour ouvrir la porte.

- `server_with_MCP_logs.py` : Cette version, toujous sans sécurisation, implémente la journalisation côté protocole MCP.


## Installation et exécution

### 1. Ajuster l'emplacement des journaux
Toutes les versions implémentent la jounalisation locale. Vous pouvez adapter l'emplacement indiqué au FileHandler pour qu'il enregistre les journaux dans votre emplacement souhaité.

### 2. Installation du framework FastMCP
Utilisez votre terminal pour exécuter une des commandes suivantes :
* uv add fastmcp (recommandée par FastMCP)
* pip install fastmcp