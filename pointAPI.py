import logging
import boto3
 
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
DYNAMO = boto3.resource('dynamodb') #dbname
 
def lambda_handler(event, context):
    try:
        table_name = "pointID"#table_name
    
        table = DYNAMO.Table(table_name)
        res = table.scan()

        total = res['Count'] + 1#要素名
        with table.batch_writer() as batch:
                batch.put_item(
                    Item={
                        'point_id': '00'+ str(total),#項目名
                        'point': str(total) + 'day',#項目名
                    }
                )
        LOGGER.info("Completed registration")
        return "end"#HTMLの表示名
    except Exception as error:
        LOGGER.error(error)
        raise error
