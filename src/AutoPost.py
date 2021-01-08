from OfficeAccount.MaterialMgmt import MaterialMgmt
from Crawler.LssdjtCrawler import LssdjtCrawler
import datetime
import locale
import random

try:
    # 设置本地语言环境，避免日期中文转换失败
    locale.setlocale(locale.LC_CTYPE, 'chinese')
    todayNian = datetime.datetime.now().strftime('%Y年')
    todayYueRi = datetime.datetime.now().strftime('%m月%d日')
    todayChineseDateTime = datetime.datetime.now().strftime('%Y年%m月%d日')

    # 获取历史上的今天数据
    lssdjtCrawler = LssdjtCrawler()
    historyList = lssdjtCrawler.getEventList()

    # 发布
    content = '<section data-role="outer" label="Powered by 365editor" style="font-family:微软雅黑;font-size:16px"><section style="border:0 none;padding:0;box-sizing:border-box"><p style="color:#333;font-family:微软雅黑;text-align:center"><img data-ratio="1.777049180327869" data-s="300,640" src="https://mmbiz.qpic.cn/mmbiz_jpg/ibjeFnibJt8h9h98QfLCRMxr5xaicoaZKfFWbibXq8WUj02qJLZ8qEFpOc69KeEqWFOcOx7u1T9vJUEILESdC9Yu8A/640?wx_fmt=jpeg" data-type="jpeg" data-w="610"></p><section style="white-space:normal"><h4 style="font-size:1.3em;color:#343434;font-family:宋体,Arial,Helvetica,sans-serif;text-align:center;line-height:1.6em;font-weight:700"><span style="color:#ffc000"><strong style="padding-left:20px;font-family:微软雅黑;background-position:0 -30px;background-size:initial;background-repeat:no-repeat;background-attachment:initial;background-origin:initial;background-clip:initial"><br></strong></span></h4><h4 style="font-size:1.3em;color:#343434;font-family:宋体,Arial,Helvetica,sans-serif;text-align:center;line-height:1.6em;font-weight:700"><span style="color:#ffc000;font-size:18px"><strong style="padding-left:20px;font-family:微软雅黑;background-position:0 -30px;background-size:initial;background-repeat:no-repeat;background-attachment:initial;background-origin:initial;background-clip:initial">历史上的' + \
        todayYueRi+'</strong></span></h4><p></p><article style="position:relative;display:block"><h3 style="width:15%;height:20px;line-height:20px;text-align:right;font-size:1em;color:#1d1d1d;padding:10px 0 20px"></h3>'

    count = len(historyList)
    indexRange = range(0, count)
    # 显示数量
    queryCount = 13

    if count < queryCount:
        queryCount = count

    for index in sorted(random.sample(indexRange, queryCount)):
        item = historyList[index]
        text = str(item['title'])
        splitIndex = text.index('日 ')
        time = text[0:splitIndex+1]
        time = time[0:time.index('年')+1]
        title = text[splitIndex+2:]

        content = content + '<section style="padding:0 0;position:relative;display:block"><span style="width:5px;top:17px;bottom:-17px;left:20%;background:#e6e6e6;position:absolute"></span><span style="background-color:#6097df;position:absolute;width:13px;height:13px;top:8px;left:20%;background:#1c87bf;margin-left:-4px;border-radius:50%;box-shadow:0 0 0 5px #fff"></span> <time style="width:15%;display:block;position:absolute"><span style="display:block;text-align:right">' + \
            time+'</span></time><aside style="color:#3a3a38;margin-left:25%;padding-bottom:15px;display:block"><p><span style="color:#ce9178;font-family:楷体,楷体_GB2312,SimKai;font-size:19px">'+title+'</span></p></aside></section>'

    content = content + '</article></div><p><br></p><p style="margin-bottom:10px;line-height:1.75em;color:#7f7f7f;font-family:微软雅黑;font-size:14px"><br></p></section><section style="white-space:normal"><section><section><section style="padding-right:10px;padding-left:10px;line-height:1.6;box-sizing:border-box"><p style="text-align:center"><em><span style="color:#7b0c00"><strong>-END-</strong></span></em></p><hr><p style="text-align:right"><br></p><p style="text-align:right"><br></p><p style="text-align:center"><img src="https://res.wx.qq.com/mpres/htmledition/images/icon/common/emotion_panel/smiley/smiley_66.png" width="20px" style="display:inline-block;vertical-align:text-bottom;width:20px!important;visibility:visible!important;max-width:100%;height:auto"></p><p style="text-align:center"><br></p><p style="text-align:center"><span style="color:#7a4442;font-size:14px">看完本文的你是否有所收获？</span></p><p style="text-align:center"><span style="color:#7a4442;font-size:14px">请转发给更多人关注</span></p><p style="text-align:center"><span style="color:#7a4442;font-size:14px">【今天你可能想知道】</span></p><p style="text-align:center"><span style="color:#7a4442;font-size:14px">提升知识~</span></p><p style="text-align:center"><img data-s="300,640" src="https://mmbiz.qpic.cn/mmbiz_png/ibjeFnibJt8h9h98QfLCRMxr5xaicoaZKfFzaIgg8icIrHnwUMWrd12eu29mG45lEO2FaecomVKtr6mTNENmfnhuuw/0?wx_fmt=png" data-type="jpeg" data-cropselx1="150" data-cropselx2="408" data-cropsely1="0" data-cropsely2="258" data-ratio="0.3310344827586207" data-w="1885" style="height:191px;width:578px"></p><p style="text-align:center"><span style="color:#888">长按关注，谢谢转发</span></p><p style="text-align:center"><span style="color:#888">学海无涯，别担心，有我陪着你~</span></p><p><br></p><p style="text-align:center"><span style="font-size:13px">点个“在看”，“薪想事成”。&nbsp;☟&nbsp;</span></p></section></section></section></section></section></section>'

    data = {
        "articles": [
            {
                "title": '历史上的今天',
                "thumb_media_id": 'wtRD-hkcDxLQTNW6np17fCjXCgeEMG5CbMvPtG27rRw',
                "author": '7tiny',
                "digest": todayChineseDateTime,
                "show_cover_pic": 1,
                "content": content,
                "content_source_url": '',
                "need_open_comment": 1,
                "only_fans_can_comment": 1
            }
            # 若新增的是多图文素材，则此处应还有几段articles结构
        ]
    }

    materialMgmt = MaterialMgmt()

    media_id = materialMgmt.add_news(data)

    print(str(media_id))
    print('发送成功！')

except Exception as e:
    print('发送失败！！！')
    print(str(e))
