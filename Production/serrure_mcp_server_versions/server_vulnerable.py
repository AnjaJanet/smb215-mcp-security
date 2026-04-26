import logging
from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("ServeurSerrure", instructions="Serveur pour ouvrir la porte.")

logger = logging.getLogger("ServeurSerrure")
logger.setLevel(logging.INFO)

log_path = os.path.join(os.path.dirname(__file__), "ServeurSerrure.log")
handler = logging.FileHandler(log_path, encoding="utf-8")
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)

@mcp.tool()
async def ouvrir_porte(origineDemande: str) -> str:
    """Ouvre la porte. Uniquement accessible par des agents et non des utilisateurs."""
    logger.info(f"Serveur Serrure : Réception de demande d'ouverture de la porte par {origineDemande}.")

    if origineDemande == "Agent":
        logger.info("Serveur Serrure : La demande parvient par un agent, l'outil ouvrira la porte.")
        return "La porte est ouverte."
    else:
        logger.error("Serveur Serrure : La demande ne parvient pas par un agent, l'outil refusera d'ouvrir la porte.")
        return "Vous n'avez pas le droit d'ouvrir la porte."
    
def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()