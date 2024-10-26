# lambda_function_v2.py
def lambda_handler(event, context):
    recommendations = [
        {"hotel": "Sunrise Resort", "rating": 4.5},
        {"hotel": "OceanView Hotel", "rating": 4.7},
        {"hotel": "Mountain Retreat", "rating": 4.3}
    ]
    return {
        'statusCode': 200,
        'body': {
            'message': 'Updated hotel recommendations',
            'recommendations': recommendations
        }
    }
