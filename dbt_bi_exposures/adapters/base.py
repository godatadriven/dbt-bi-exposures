from abc import ABC, abstractmethod
from dbt.contracts.graph.parsed import ParsedExposure
from typing import List

class BaseAdapter(ABC):

    @abstractmethod
    def get_exposures(self, manifest_path: str, output_path: str = None) -> List[ParsedExposure]:
        """
        Get exposures either in a string-yaml style or in a file
        Params
        ------
        manifest_path : str
            Path to the dbt manifest.json of your dbt project
        output_path : str
            If provided, the yaml file will be placed in this output_path
        """
        pass