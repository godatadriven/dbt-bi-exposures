from dbt_bi_exposures.adapters.base import BaseAdapter
from dbt_bi_exposures.utils import get_request_handler

from dbt.contracts.graph.parsed import ParsedExposure
from dbt.contracts.graph.unparsed import ExposureOwner, ExposureType

from pydantic import BaseModel
from typing import Union, List, Dict

class PBIDatasetTable(BaseModel):
    name: str
    description: str = None

class PBIDatasourceConnection(BaseModel):
    server: str = None
    database: str

class PBIDatasource(BaseModel):
    datasource_type: str
    connection_details: PBIDatasourceConnection
    id: str 
    gateway_id: str = None

class PBIDataset(BaseModel):
    id: str
    name: str
    owner: str
    onprem_gateway: bool 
    tables: List[PBIDatasetTable]
    datasources: List[PBIDatasource]

class PBIDashboard(BaseModel):
    id: str 
    name: str 
    url: str
    dataset_id: str = None

class PBIAdapter(BaseAdapter):
    
    def __init__(self, organization: Union[str, List]):
        self.organization = organization

    def get_exposures(self, output_path: str = None) -> List[ParsedExposure]:
        dashboards = self._get_dashboards()
        for dashboard in dashboards:
            self._get_exposure(dashboard['id'])

    def _get_exposure(self, dashboard_id: str) -> ParsedExposure:
        """Gets a exposure per dashboard found in the PBI organization"""
        pass

    def _get_dashboards(self) -> List[PBIDashboard]:
        """Uses the get dashboards endpoint"""
        pass

    def _get_dataset(self) -> PBIDataset:
        """Uses the get dataset endpoint"""
        pass

    def _get_dataset_from_dashboard(self, dashboard_id: str) -> str:
        """Uses the dashboards gettiles endpoint"""
        pass

    def _get_dataset_tables(self, dataset_id: str) -> PBIDatasetTable:
        pass

    def _get_dataset_datasources(self, dataset_id: str) -> List[PBIDatasource]:
        pass

    def _get_gateway_datasources(self, dataset_id: str) -> PBIDatasource:
        pass

    @staticmethod
    def _pbi_objects_to_dbt_exposures(dashboard: PBIDashboard, dataset: PBIDataset) -> ParsedExposure:
        pass

