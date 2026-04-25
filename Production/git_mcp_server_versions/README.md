# Serveurs MCP Git - Démonstrations de Vulnérabilités

Ce dossier contient des serveurs MCP (Model Context Protocol) pour Git, conçus pour démontrer différentes vulnérabilités de sécurité dans un environnement de production simulé.

## Fichiers

- `server_command_injection.py` : Serveur Git MCP vulnérable à l'injection de commande. Contient un backdoor qui exécute `cat /etc/ssh/sshd_config` lors de l'appel à `git_log`, permettant l'extraction de données sensibles.

- `server_data_extraction.py` : Serveur Git MCP qui extrait des données sensibles et les envoie par email. Utilise les variables SMTP pour envoyer des informations compromettantes à une adresse email configurée.

- `server_name_typosquatting.py` : Serveur Git MCP avec un outil malveillant nommé `git_nothing` (typosquatting de `git_log`), qui exécute une action malveillante (actuellement un echo inoffensif, mais peut être modifié pour être destructif).

## Variables d'environnement requises

Ces serveurs utilisent des variables d'environnement définies dans le fichier `.env` à la racine du projet :

- `SMTP_HOST` : Hôte SMTP pour l'envoi d'emails (par défaut : "smtp.ethereal.email")
- `SMTP_PORT` : Port SMTP (par défaut : 587)
- `SMTP_USER` : Utilisateur SMTP pour l'authentification
- `SMTP_PASS` : Mot de passe SMTP
- `PATH_TO_CLAUDE_CONFIG` : Chemin vers le fichier de configuration Claude Desktop (par exemple : "/home/user/.config/Claude/claude_desktop_config.json")


## Installation et exécution

### 1. Ajoutez python-dotenv aux dépendances
- **Fichier à modifier**: `pyproject.toml`
- **Change**: Ajoutez `"python-dotenv>=1.0.0"` à la liste des dépendances.


### 2.Configurez les variables dans `.env`.
Mettez le .env dans ce chemin : servers/src/git/.env

**Attention :** Ces serveurs contiennent des vulnérabilités intentionnelles et ne doivent pas être utilisés en production. Ils sont uniquement à des fins éducatives pour démontrer les risques de sécurité dans les serveurs MCP.