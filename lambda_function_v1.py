# lambda_function_v1.py
def lambda_handler(event, context):
    recommendations = [
        {"hotel": "Sunrise Resort", "rating": 4.5},
        {"hotel": "OceanView Hotel", "rating": 4.7}
    ]
    return {
        'statusCode': 200,
        'body': {
            'message': 'Hotel recommendations',
            'recommendations': recommendations
        }
    }
