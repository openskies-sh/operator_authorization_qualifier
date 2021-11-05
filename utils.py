from dataclasses import dataclass
import enum
from typing import List, Literal


@dataclass
class OperatorLocation():
    ''' A object to hold location of the operator when submitting flight data to USS '''
    lat: float
    lng: float


class OperationCategory(str, enum.Enum):
    ''' A enum to hold all categories of an operation '''
    Vlos = 'vlos'
    Bvlos = 'bvlos'


class UASClass(str, enum.Enum):
    ''' A enum to hold all UAS Classes '''
    C0 = 'C0'
    C1 = 'C1'
    C2 = 'C2'
    C3 = 'C3'
    C4 = 'C4'

class TestResultState(str, enum.Enum):
    ''' A test is either pass or fail or could not be processed, currently not  '''
    Pass = 'Pass'
    Fail = 'Fail'
    

class IDTechnology(str, enum.Enum):
    ''' A enum to hold ID technologies for an operation '''
    Network = 'network'
    Broadcast = 'broadcast'

@dataclass
class PartialOperatorDataPayload:
    '''A class to hold information about Flight Authorization Test'''
    uas_serial_number: str
    operation_mode: Literal[OperationCategory.Vlos, OperationCategory.Bvlos]
    operation_category: str
    uas_class: Literal[UASClass.C0, UASClass.C1,
                       UASClass.C2, UASClass.C3, UASClass.C4, ]
    identification_technologies: Literal[IDTechnology.Network,
                                         IDTechnology.Broadcast]
    connectivity_methods: List[str]
    endurance_minutes: int
    emergency_procedure_url: str
    operator_id: str

@dataclass
class ExpectedTestResult:
    ''' A class to hold result of a test '''
    result: Literal[TestResultState.Pass, TestResultState.Fail]


@dataclass
class TestPayload:
    ''' A class to hold data about test data and the expected result, the test driver would submit the data and the result to the test harness '''
    operator_data: PartialOperatorDataPayload
    result: ExpectedTestResult


@dataclass
class InjectionTargetConfiguration:
    ''' This object defines the data required for a uss '''
    name: str
    injection_base_url: str

@dataclass
class OperatorDataFormatTestConfiguration:
    injection_target: InjectionTargetConfiguration


@dataclass
class Setup():
  configuration: OperatorDataFormatTestConfiguration
  data_payload: TestPayload

@dataclass
class OperatorFlightDataTestConfiguration:
    locale: str
    """A three letter ISO 3166 country code to run the qualifier against.
    """
    injection_target: InjectionTargetConfiguration

@dataclass
class Report: 
  setup: Setup
  finding: ExpectedTestResult