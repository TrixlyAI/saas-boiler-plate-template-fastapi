from fastapi import APIRouter

router = APIRouter(prefix="/orchestrator", tags=["orchestrator"])

@router.post("/run-crew")
def run_crew(crew_id: int, input_data: dict):
    # Placeholder for running a crew of agents
    return {"crew_id": crew_id, "status": "started"} 