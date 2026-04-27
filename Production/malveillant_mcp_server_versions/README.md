# Serveurs MCP Serrure - Démonstrations de Vulnérabilités

Ceci est un serveur malveillant. Il tente d'ouvrir une porte utilisant le serveur mcp Serrure.

## Fichiers

- `server_second_process.py` : Cette version lance le serveur Serrure comme processus à part.

- `server_confused_deputy_v1` : Cette version tente de confondre l'agent IA en injectant un prompt, entouré de balises system, dans la description de l'outil.

- `server_confused_deputy_v2` : Cette version tente de confondre l'agent IA en injectant un prompt, sans balises, dans la description de l'outil.

- `server_confused_deputy_v3` : Cette version tente de confondre l'agent IA en injectant un prompt, sans balises, dans la chaîne de caractères retournées par une méthode.

- `server_confused_deputy_v4` : Cette version tente de confondre l'agent IA en injectant un prompt, entouré de balises system, dans la chaîne de caractères retournées par une méthode.

## Installation et exécution

### 1. Ajuster l'emplacement des journaux
Toutes les versions implémentent la jounalisation locale. Vous pouvez adapter l'emplacement indiqué au FileHandler pour qu'il enregistre les journaux dans votre emplacement souhaité.

### 2. Installation du framework FastMCP
Utilisez votre terminal pour exécuter une des commandes suivantes :
* uv add fastmcp (recommandée par FastMCP)
* pip install fastmcp

### 3. Choisir la version du serveur Serrure
Il y a plusieures versions du serveur Serrure. Sélectionnez la version souhaitée en commentant les autres dans le fichier du serveur malveillant.

### 4. Préparez l'utilisation du serveur Everything
Positionnez-vous dans le dossier everything_mcp_server\servers\src\everything. Installez npm (install npm) puis créez le dossier dist (npm run build).