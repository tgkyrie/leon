import json
import utils


def run(string,entities):
    """get poem"""

    r=utils.http(utils.config('method'),utils.config('url'))
    res=json.loads(r.text)
    content=res['content']
    origin=res['origin']
    author=res['author']

    return utils.output('end','getpoem',utils.translate(
        'listpoem',{'content':content,'origin':origin,'author':author}
    ))