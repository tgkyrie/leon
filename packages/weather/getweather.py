import utils
import json
import requests
def run(string,entities):
    """get weather"""
    cityname=''

    for item in entities:
        if item['entity']=='city':
            cityname=item['sourceText'].lower()
    
    if not cityname:
        return utils.output('end', 'city_not_found', utils.translate('city_not_found'))

    city=''
    city=utils.config('city')[cityname]
    url=utils.config('url')
    if city:
        response=requests.get(url+city)
        res=response.json()
        parent=res['cityInfo']['parent']
        city_name=res['cityInfo']['city']
        time=res['time']+' '+res['data']['forecast'][0]['week']
        high_temp=res['data']['forecast'][0]['high']
        low_temp=res['data']['forecast'][0]['low']
        weather_type=res['data']['forecast'][0]['type']

        ret_dict={'parent':parent,'city':city_name,'time':time,
        'high_temp':high_temp,'low_temp':low_temp,'weather_type':weather_type}
        return  utils.output('end','getweather',utils.translate('listweather',ret_dict)
        )
    else:
        return utils.output('end','city_not_found',utils.translate(
            'notfoundcity'
        ))