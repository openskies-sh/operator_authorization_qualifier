from dataclasses import dataclass
import enum
from typing import List, Literal

class OperationMode(str, enum.Enum):
    ''' A enum to hold all modes of an operation '''
    Undeclared = 'Undeclared'
    Vlos = 'Vlos'
    Bvlos = 'Bvlos'

class OperationCategory(str, enum.Enum):
    ''' A enum to hold all categories for an operation '''
    Open = 'Open'
    Specific = 'Specific'
    Certified = 'Certified'


class UASClass(str, enum.Enum):
    ''' A enum to hold all UAS Classes '''
    Other = 'Other'
    C0 = 'C0'
    C1 = 'C1'
    C2 = 'C2'
    C3 = 'C3'
    C4 = 'C4'
    C5 = 'C5'
    C6 = 'C6'

class TestResultState(str, enum.Enum):
    ''' A test is either pass or fail or could not be processed, currently not  '''
    Pass = 'Pass'
    Fail = 'Fail'
    

class IDTechnology(str, enum.Enum):
    ''' A enum to hold ID technologies for an operation '''
    Network = 'network'
    Broadcast = 'broadcast'

@dataclass
class FlightAuthorizationData:
    '''A class to hold information about Flight Authorization Test'''
    uas_serial_number: str
    operation_mode: Literal[OperationMode.Undeclared, OperationMode.Vlos, OperationMode.Bvlos]
    operation_category: Literal[OperationCategory.Open, OperationCategory.Specific, OperationCategory.Certified]
    uas_class: Literal[UASClass.Other,UASClass.C0, UASClass.C1,
                       UASClass.C2, UASClass.C3, UASClass.C4,UASClass.C5, UASClass.C6  ]
    identification_technologies: List[str]
    uas_type_certificate: str
    connectivity_methods: List[str]
    endurance_minutes: int
    emergency_procedure_url: str
    operator_id: str
    uas_id: str

@dataclass
class ExpectedTestResult:
    ''' A class to hold result of a test '''
    result: Literal[TestResultState.Pass, TestResultState.Fail]


@dataclass
class TestPayload:
    ''' A class to hold data about test data and the expected result, the test driver would submit the data and the result to the test harness '''
    operator_data: FlightAuthorizationData
    expected_result: ExpectedTestResult


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
  error: str