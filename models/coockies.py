from pydantic import BaseModel

class Coockies(BaseModel):
    session_id: int
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

    model_config = {
        'extra': 'forbid'
    }