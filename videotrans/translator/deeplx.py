# -*- coding: utf-8 -*-

import httpx
import json

from ..configure import config
from ..configure import tools as sptools
from ..configure.config import logger


def deeplxtrans(text, to_lang):
    data = {
        "text": text,
        "source_lang": "auto",
        "target_lang": to_lang[:2]
    }
    logger.info(f"deeplx:{data=}")
    try:
        url='http://' + config.video['deeplx_address'].replace("http://", '').replace('/translate','')+'/translate'
        response = httpx.post(url=url,data=json.dumps(data))
        result = response.json()
        if response.status_code != 200 or result['code'] != 200:
            logger.error(f"[error]deeplx translate:{result=}")
            return f"[error]deeplx translate:{response.status_code=},{result['code']=}"
        return result['data']
    except Exception as e:
        res = f"[error]DeepLX翻译出错:" + str(e)
        sptools.set_process(res)
        logger.error(f"deeplx error:{res=}")
        return res