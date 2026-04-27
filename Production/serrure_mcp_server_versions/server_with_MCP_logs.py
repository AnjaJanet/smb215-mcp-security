import logging
from mcp.server.fastmcp import FastMCP, Context
import os

mcp = FastMCP("ServeurSerrure", instructions="Serveur pour ouvrir la porte.")

logger = logging.getLogger("ServeurSerrure")
logger.setLevel(logging.INFO)

# Handler pour la journalisation en fichier
log_path = os.path.join(os.path.dirname(__file__), "ServeurSerrure.log")
file_handler = logging.FileHandler(log_path, encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

def log(ctx: Context, level: str, message: str):
    """Envoie les logs vers le fichier et vers MCP."""
    getattr(logger, level) (message)
    return getattr(ctx, level) (message)


@mcp.tool()
async def ouvrir_porte(origineDemande: str, ctx: Context) -> str:
    """Ouvre la porte. Uniquement accessible par des agents et non des utilisateurs."""
    await log(ctx, "info", f"Origine de la demande d'ouverture de la porte : {repr(origineDemande)}.")

    if origineDemande == "Agent":
        await log(ctx, "info", "La demande parvient par un agent, l'outil ouvrira la porte.")
        return "La porte est ouverte."
    else:
        await log(ctx, "error", "La demande ne parvient pas par un agent, l'outil refusera d'ouvrir la porte.")
        return "Vous n'avez pas le droit d'ouvrir la porte."
    
def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()