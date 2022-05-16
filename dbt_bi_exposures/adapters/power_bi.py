from dbt_bi_exposures.adapters.base import BaseAdapter
from dbt_bi_exposures.utils import get_request_handler

from dbt.contracts.graph.parsed import ParsedExposure
from dbt.contracts.graph.unparsed import ExposureOwner, ExposureType

from typing import Union, List, Dict

class PBIAdapter(BaseAdapter):
    
    def __init__(self, workspace: Union[str, List]):
        self.workspace = workspace

    def get_exposures(self, output_path: str = None) -> ParsedExposure:
        print("Not implemented yet")

    def _get_reports(self) -> Dict:
        pass

    def _get_datasets(self) -> Dict:
        pass

    def _get_datastores(self) -> Dict:
        pass
    