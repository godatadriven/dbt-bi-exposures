from abc import ABC, abstractmethod
from dbt.contracts.graph.parsed import ParsedExposure

class BaseAdapter(ABC):

    @abstractmethod
    def get_exposures(self, output_path: str = None) -> ParsedExposure:
        """
        Get exposures either in a string-yaml style or in a file
        Params
        ------
        output_path : str
            If provided, the yaml file will be placed in this output_path
        """
        pass