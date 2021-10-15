import json
import config
import seeker
import csv

BEARER_TOKEN = config.bearer_token

tweet_retriever = seeker.Seeker()
def retrieve_tweets():
    result = tweet_retriever.get_user_tweets('drfahrettinkoca')
    return result

def manipulate_public_metrics(json):
    for data in json:
        for key,value in list(data.items()):
            if(key == 'public_metrics'):
                for key,value in value.items():
                     data[key] = value
                del data['public_metrics']

    return json

def write_to_csv(json):
    data_file = open('data_file.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(data_file, delimiter=',')

    count = 0
    for data in json:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(data.values())
    
    data_file.close()

def save_json(json):
    json_object = json.dumps(json, indent = 4)
    with open('data.json', 'w') as f:
        f.write(json_object)   


def main(*args, **kwargs):
    result = retrieve_tweets()    
    result = result['data']
    result = manipulate_public_metrics(result)
    write_to_csv(result)


main()

