from dbt_bi_exposures.adapters.base import BaseAdapter
from dbt.contracts.graph.parsed import ParsedExposure
from dbt.contracts.graph.unparsed import ExposureOwner, ExposureType

class PBIAdapter(BaseAdapter):
    def __init__(self, workspace: str):
        self.workspace = workspace

    def get_exposures(self) -> ParsedExposure:
        print("Not implemented yet")