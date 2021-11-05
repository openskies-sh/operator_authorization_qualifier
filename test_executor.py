import json
import random
import dataclasses
from utils import TestPayload, PartialOperatorDataPayload, TestResult, OperatorFlightDataTestConfiguration, Report, Setup
from operator_data_generator import OperatorFlightDataGenerator

class TestBuilder() :
    ''' A class to setup the test data and create the objects ready to be submitted to the test harness '''

    def coin_flip(self) -> bool:
        return random.choice([0,1])
    
    def build_test_payload(self) -> TestPayload:
        ''' A method to build test payload ready to submit in the test harness '''
        my_operator_flight_data_generator = OperatorFlightDataGenerator()
        all_coin_flips =[]
        
        serial_number = my_operator_flight_data_generator.generate_serial_number()       

        should_fail = self.coin_flip() # check if the test should pass or fail, if the test should pass then no changes should be made to the serial number / registration number shoould not be tampered
        all_coin_flips.append(should_fail)
        if should_fail: # 0
            # take a valid serial_number and make it invalid
            serial_number = my_operator_flight_data_generator.generate_incorrect_serial_number(valid_serial_number=serial_number)

        operator_registration_number = my_operator_flight_data_generator.generate_registration_number()
        should_fail = self.coin_flip() # check if the test should pass or fail, if the test should pass then no changes should be made to the serial number / registration number shoould not be tampered
        all_coin_flips.append(should_fail)        
        if should_fail:
            operator_registration_number = my_operator_flight_data_generator.generate_incorrect_registration_number(valid_registration_number=operator_registration_number)

        
        operator_data_payload = PartialOperatorDataPayload(uas_serial_number = serial_number, operation_category='u-space', operation_mode = 'vlos',uas_class='C0', identification_technologies = 'vlos', connectivity_methods = [], endurance_minutes = [] , emergency_procedure_url = "https://uav.com/emergency", operator_id = operator_registration_number)

        expected_test_result = 'fail' if (len(set(all_coin_flips)) ==2) else 'pass'

        expected_test_result = TestResult(result = expected_test_result)

        test_payload = TestPayload(operator_data=operator_data_payload,result=expected_test_result)
        test_payload = dataclasses.asdict(test_payload)
        
        return test_payload


def main(test_configuration: OperatorFlightDataTestConfiguration,
        auth_spec: str = None) -> Report:
    my_test_builder = TestBuilder()
    test_payload = my_test_builder.build_test_payload()
    report = Report(setup=Setup(configuration= test_configuration, finding=test_payload.result)
    )

if __name__ == '__main__':
    ''' This module generates a JSON that can be used to test '''
    my_test_builder = TestBuilder()
    test_payload = my_test_builder.build_test_payload()