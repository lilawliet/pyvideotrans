'''
import requests
from PySide6.QtCore import QSettings

from videotrans.configure import config

url=QSettings("Jameson", "VideoTranslate").value("clone_api", "")
print(f'{url=}')
if not url:
    print(config.transobj['bixutianxiecloneapi'])
else:
    try:
        url = url.strip().rstrip('/') + "/init"
        res = requests.get('http://' + url.replace('http://', ''))
        if res.status_code == 200:
            print(res.json)
            print("\nOK\n")
        else:
            raise Exception(f"code={res.status_code},{config.transobj['You must deploy and start the clone-voice service']}")
    except Exception as e:
        print(f'[error]:clone-voice:{str(e)}')


input("Press Enter for quit")
'''

# from videotrans.separate import st
# try:
#     gr = st.uvr(model_name="HP2", save_root="./", inp_path=r'C:/Users/c1/Videos/240.wav')
#     print(next(gr))
#     print(next(gr))
# except Exception as e:
#     msg=f"separate vocal and background music:{str(e)}"
#     #set_process(msg)
#     print(msg)


## 获取识别文字
# import os
# from faster_whisper import WhisperModel
# model = WhisperModel("base", device="cpu",
#                              download_root="./models",
#                              local_files_only=True)
# data=[]
#
# for i in range(0,24):
#     name=f'output0{str(i).zfill(2)}.wav'
#     if not os.path.exists(f'c:/users/c1/videos/_video_out/{name}'):
#         continue
#     segments, info = model.transcribe(f'c:/users/c1/videos/_video_out/{name}',
#                                           beam_size=1,
#                                           best_of=1,
#                                           condition_on_previous_text=False,language="zh")
#     res=[]
#     for segment in segments:
#         res.append(segment.text.strip())
#     data.append(f"wavs/{name}|{'.'.join(res)}|coqui")
#
# with open("./metadata_train.csv","w",encoding='utf-8') as f:
#     f.write("\n".join(data))

# import requests
# lang=["zh-hans","zh-hant","en","fr","de","ja","ko","ru","es","th","it","pt","vi","ar","tr","hi","hu"]
#
# auth=requests.get('https://edge.microsoft.com/translate/auth')
#
# for it in lang:
#     url=f'https://api-edge.cognitive.microsofttranslator.com/translate?from=&to={it}&api-version=3.0&includeSentenceLength=true'
#     res=requests.post(url,json=[{"Text":"hello,my friend\nI am from China"}],headers={"Authorization":f"Bearer {auth.text}"})
#     print(res.json())


# from videotrans.util import tools
#
# cmd=["-y",'-ss', '0', '-to', '00:00:01.300', '-i', 'C:/Users/c1/Videos/pyvideotrans/renamemp4/_video_out/31-副本/novoice.mp4', '-vf', 'setpts=1.96*PTS', '-c:v', 'libx264', '-crf', '13', 'F:/python/pyvideo/tmp/31-副本/novoice_tmp.mp4']
#
# tools.runffmpeg(cmd)
# import time

# a="有新的版本哦，快去升级吧"
# length=len(a)
# while 1:
#     for i in range(length):
#         if i==0:
#             print(a)
#         elif i==length-1:
#             print(a[i]+a[:i])
#         else:
#             print(a[i:]+a[:i])
#         time.sleep(0.1)
#     time.sleep(5)


# from videotrans.util import tools


# tools.get_subtitle_from_srt(r'C:\Users\c1\Videos\dev\0001.srt',is_file=True)


# import re
#
# def format_time(s_time="",separate=','):
#     if not s_time.strip():
#         return f'00:00:00.000'
#     hou,min,sec="00","00","00.000"
#     tmp=s_time.split(':')
#     if len(tmp)>=3:
#         hou=tmp[-3]
#         min=tmp[-2]
#         sec=tmp[-1]
#     elif len(tmp)==2:
#         min=tmp[0]
#         sec=tmp[1]
#     elif len(tmp)==1:
#         sec=tmp[0]
#
#     if re.search(r',|\.',str(sec)):
#         sec,ms=re.split(r',|\.',str(sec))
#     else:
#         ms='000'
#     hou=hou if hou!="" else "00"
#     if len(hou)<2:
#         hou=f'0{hou}'
#     hou=hou[-2:]
#
#     min=min if min!="" else "00"
#     if len(min)<2:
#         min=f'0{min}'
#     min=min[-2:]
#
#     sec=sec if sec!="" else "00"
#     if len(sec)<2:
#         sec=f'0{sec}'
#     sec=sec[-2:]
#
#     ms_len=len(ms)
#     if ms_len<3:
#         for i in range(3-ms_len):
#             ms=f'0{ms}'
#     ms=ms[-3:]
#     return f"{hou}:{min}:{sec}{separate}{ms}"
#
# print(format_time('',','))


#
# import httpx, json,requests
#
# deeplx_api = "https://service-2rlyleme-1259515617.gz.tencentapigw.com.cn/translate"
#
# data = {
#     "text": "你好我的朋友",
#     "source_lang": "auto",
#     "target_lang": "en"
# }
# res=requests.post(url=deeplx_api, json=data)
# print(res.json())


# import requests
#
# data={
#     "refer_wav_path": "wavs/mayun.wav",
#     "prompt_text": "我记得我大学一年级的时候，我自，我从小自学的英文，我的英文是在西湖边上抓老外。",
#     "prompt_language": "zh",
#     "text": """GPT Sovits 是一个非常棒的少样本中文声音克隆项目，之前有一篇文章详细介绍过如何部署和训练自己的模型，并使用该模型在 web 界面中合成声音，可惜它自带的 api 在调用方面支持比较差，比如不能中英混合、无法按标点切分句子等，因此对原版 api 做了修改，详细使用说明如下。
#
# 和官方原版 api 一样都不支持动态模型切换，也不建议这样做，因为动态启动加载模型很慢，而且在失败时也不方便处理。
#
# 解决方法是:一个模型起一个 api 服务器，绑定不同的端口，在启动 api 时，指定当前服务所要使用的模型和绑定的端口。
#
# 比如起2个服务，一个使用默认模型，绑定 9880 端口，一个绑定自己训练的模型，绑定 9881 端口，命令如下。""",
#     "text_language": "zh"
# }
#
# response=requests.post("http://127.0.0.1:9881",json=data)
#
# if response.status_code==400:
#     raise Exception(f"请求GPTSoVITS出现错误:{response.message}")
#
#
# # 如果是WAV音频流，获取原始音频数据
# with open("success.wav", 'wb') as f:
#     f.write(response.content)
import os,sys
import subprocess


import requests
import json

'''
# 设置请求的URL
url = "https://kimi.moonshot.cn/api/chat/cnsrbdmcp7fdtb87sm1g/segment/scroll"

# 设置请求头
headers = {
    "authority": "kimi.moonshot.cn",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6,ja;q=0.5",
    "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcxMDg2NTIzMiwiaWF0IjoxNzEwODY0MzMyLCJqdGkiOiJjbnNyZmowM3IwNzA2OGExOXMxZyIsInR5cCI6ImFjY2VzcyIsInN1YiI6ImNuc3I2YTgzcjA3MDY4OXZhbDcwIiwic3BhY2VfaWQiOiJjbnNyNmE4M3IwNzA2ODl2YWw2ZyIsImFic3RyYWN0X3VzZXJfaWQiOiJjbnNyNmE4M3IwNzA2ODl2YWw2MCJ9.zHZ0k13YxFxWLWHchMIWmL4nhLLFQ9-wFIfQQXG9CnjSWUKJU1ATbDT8JK-bMKoRpDh-a0AfbsFQXUwyoErG3g",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "Hm_lvt_358cae4815e85d48f7e8ab7f3680a74b=1710732371; _ga=GA1.1.187473429.1710862969; _ga_YXD8W70SZP=GS1.1.1710862969.1.1.1710863668.0.0.0; Hm_lpvt_358cae4815e85d48f7e8ab7f3680a74b=1710863939",
    "dnt": "1",
    "origin": "https://kimi.moonshot.cn",
    "pragma": "no-cache",
    "r-timezone": "Asia/Shanghai",
    "referer": "https://kimi.moonshot.cn/chat/cnsrbdmcp7fdtb87sm1g",
    "sec-ch-ua": "^\"Chromium^\";v=^\"122^\",^\"Not(A:Brand^\";v=^\"24^\",^\"Google Chrome^\";v=^\"122^\"^",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\"Windows^\"^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 设置请求的数据
data = {
    "segment_ids": ["cnsrflalnl9af3pojoug", "cnsrflalnl9af3pojov0"]
}

# 发送POST请求
response = requests.post(url, headers=headers, json=data)

# 打印响应内容
print(response.text)

'''

# 设置请求的URL
url = "https://kimi.moonshot.cn/api/chat/cnsrbdmcp7fdtb87sm1g/completion/stream"

# 设置请求头
headers = {
    "authority": "kimi.moonshot.cn",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6,ja;q=0.5",
    "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ1c2VyLWNlbnRlciIsImV4cCI6MTcxMDg2NTIzMiwiaWF0IjoxNzEwODY0MzMyLCJqdGkiOiJjbnNyZmowM3IwNzA2OGExOXMxZyIsInR5cCI6ImFjY2VzcyIsInN1YiI6ImNuc3I2YTgzcjA3MDY4OXZhbDcwIiwic3BhY2VfaWQiOiJjbnNyNmE4M3IwNzA2ODl2YWw2ZyIsImFic3RyYWN0X3VzZXJfaWQiOiJjbnNyNmE4M3IwNzA2ODl2YWw2MCJ9.zHZ0k13YxFxWLWHchMIWmL4nhLLFQ9-wFIfQQXG9CnjSWUKJU1ATbDT8JK-bMKoRpDh-a0AfbsFQXUwyoErG3g",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "Hm_lvt_358cae4815e85d48f7e8ab7f3680a74b=1710732371; _ga=GA1.1.187473429.1710862969; _ga_YXD8W70SZP=GS1.1.1710862969.1.1.1710863668.0.0.0; Hm_lpvt_358cae4815e85d48f7e8ab7f3680a74b=1710863939",
    "dnt": "1",
    "origin": "https://kimi.moonshot.cn",
    "pragma": "no-cache",
    "r-timezone": "Asia/Shanghai",
    "referer": "https://kimi.moonshot.cn/chat/cnsrbdmcp7fdtb87sm1g",
    "sec-ch-ua": "^\"Chromium^\";v=^\"122^\",^\"Not(A:Brand^\";v=^\"24^\",^\"Google Chrome^\";v=^\"122^\"^",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\"Windows^\"^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 设置请求的数据
data = {
    "messages": [
        {
            "role": "user",
            "content": "将下一行的内容都翻译为英文\n我是中国人，你呢我的朋友"
        }
    ],
    "refs": [],
    "use_search": False
}

# 发送POST请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 打印响应内容
print(response.text)
