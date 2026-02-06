from abc import ABC, abstractmethod
from typing import Any, Dict

class AgentSkill(ABC):
    """
    Base class for all Agent Skills.
    Enforces inputs/outputs.
    """
    
    @abstractmethod
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        pass