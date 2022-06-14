from dbt_bi_exposures.adapters.base import BaseAdapter
from dbt_bi_exposures.utils import get_request_handler

from dbt.contracts.graph.parsed import ParsedExposure
from dbt.contracts.graph.unparsed import ExposureOwner, ExposureType

from pydantic import BaseModel
from typing import List

class MetabaseAdapter(BaseAdapter):
    
    def get_exposures(self, output_path: str = None) -> List[ParsedExposure]:
        pass