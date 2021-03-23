import json
import random
import datetime
import boto3

def lambda_handler(event, context):
    # TODO implement
    color=[
        "red",
        "orange",
        "chocalate",
        "brown",
        "pink",
        "blue",
        "Yellow",
        "Green",
        "Black",
        "White",
        "Lavender",
        "Khaki"
    ]


    dt = datetime.datetime.utcnow()
    time_string = dt.strftime("%Y%m%d-%H%M%S")   #converting timestap into given form
    filename=time_string + '.json'
    session = boto3.session.Session() #in local used profile_name=DA
    s3 = session.resource('s3')
    s3_filename_raw = "jatin-mehrotra/blog_demo/" + filename
    bucket_name = 'query-external-data-with-redshift'
    random_number=random.randint(1,50)
    colour_value = random.choice(color)
    object={'colour':colour_value,'number':random_number}
    object = json.dumps(object, ensure_ascii=False)
    obj = s3.Object(bucket_name,s3_filename_raw)
    r = obj.put(Body = object)

