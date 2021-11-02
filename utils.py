from dataclasses import dataclass
import uuid
import enum
from typing import List, Literal
import arrow


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
    
class IDTechnology(str, enum.Enum):
    ''' A enum to hold ID technologies for an operation '''
    Network = 'network'
    Broadcast = 'broadcast'
    
     
    
@dataclass
class FlightAuthorizationPartialPayload:
    '''A clas to hold information about Flight Authorization Test'''
    uas_serial_number: str
    operation_mode: Literal[OperationCategory.Vlos,OperationCategory.Bvlos]
    operation_category:  str
    uas_class: Literal[UASClass.C0,UASClass.C1,UASClass.C2,UASClass.C3,UASClass.C4,]
    identification_technologies:Literal[IDTechnology.Network, IDTechnology.Broadcast]
    connectivity_methods: List[str]
    endurance_minutes: int
    emergency_procedure_url: str
    operator_id: str
