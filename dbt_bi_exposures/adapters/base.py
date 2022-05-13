from abc import ABC, abstractmethod
from dbt.contracts.graph.parsed import ParsedExposure

class BaseAdapter(ABC):
    @abstractmethod
    def get_exposures(self) -> ParsedExposure:
        pass