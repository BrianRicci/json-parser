from datetime import datetime


def parse_json(initial_data: dict) -> list:
    data_list = initial_data.get('history')
    result_data = list()

    for operation in data_list:
        result_data.append(
            {
                'at': datetime.fromisoformat(operation.get('at')).strftime("%d-%m-%Y %H:%M:%S"),
                'amount': operation.get('amount'),
                'operationName': operation.get('operationName'),
            }
        )

    return result_data


if __name__ == '__main__':
    data = {
        "history": [
            {
                "at": "2025-03-09T23:59:59+03:00",
                "amount": -1000,
                "operation": "OPERATION_EXPIRED",
                "operationName": "Списание по истечении срока",
                "OPERATION_EXPIRED": {}
            },
            {
                "at": "2025-03-06T00:50:35+03:00",
                "amount": 1000,
                "operation": "OPERATION_RECEIVED",
                "operationName": "Начисление по акции",
                "OPERATION_RECEIVED": {
                    "actionName": "Начисление в рассылке"
                }
            },
            {
                "at": "2025-01-25T23:59:59+03:00",
                "amount": -1000,
                "operation": "OPERATION_EXPIRED",
                "operationName": "Списание по истечении срока",
                "OPERATION_EXPIRED": {}
            },
            {
                "at": "2025-01-24T23:59:59+03:00",
                "amount": -1000,
                "operation": "OPERATION_EXPIRED",
                "operationName": "Списание по истечении срока",
                "OPERATION_EXPIRED": {}
            },
            {
                "at": "2025-01-23T23:59:59+03:00",
                "amount": -1000,
                "operation": "OPERATION_EXPIRED",
                "operationName": "Списание по истечении срока",
                "OPERATION_EXPIRED": {}
            },
            {
                "at": "2025-01-22T23:59:59+03:00",
                "amount": -1000,
                "operation": "OPERATION_EXPIRED",
                "operationName": "Списание по истечении срока",
                "OPERATION_EXPIRED": {}
            },
            {
                "at": "2025-01-21T23:59:59+03:00",
                "amount": -1000,
                "operation": "OPERATION_EXPIRED",
                "operationName": "Списание по истечении срока",
                "OPERATION_EXPIRED": {}
            },
            {
                "at": "2025-01-21T18:00:02+03:00",
                "amount": 1000,
                "operation": "OPERATION_RECEIVED",
                "operationName": "Начисление по акции",
                "OPERATION_RECEIVED": {
                    "actionName": "Начисление в рассылке"
                }
            },
            {
                "at": "2025-01-20T23:59:59+03:00",
                "amount": -1000,
                "operation": "OPERATION_EXPIRED",
                "operationName": "Списание по истечении срока",
                "OPERATION_EXPIRED": {}
            },
            {
                "at": "2025-01-20T18:00:02+03:00",
                "amount": 1000,
                "operation": "OPERATION_RECEIVED",
                "operationName": "Начисление по акции",
                "OPERATION_RECEIVED": {
                    "actionName": "Начисление в рассылке"
                }
            }
        ],
        "pagination": {
            "total": 121
        }
    }

    for obj in parse_json(data):
        print(obj)
