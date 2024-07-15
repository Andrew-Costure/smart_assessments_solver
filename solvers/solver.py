from . import ollama_solver, openai_solver
from scraper.utils import logger_setup

SUPPORTED_SOLVERS = ["openai", "ollama"]

logger = logger_setup(__name__)

def solve(question: str, solver_id: str, model: str):
    if solver_id not in SUPPORTED_SOLVERS:
        raise ValueError("Solver not supported: %s" % solver_id)

    if solver_id == "openai":
        answer = openai_solver.solve(question, model)
    elif solver_id == "ollama":
        answer = ollama_solver.solve(question, model)

    logger.debug("Question: %s\nAnswer: %s", question, answer)
    return answer
    