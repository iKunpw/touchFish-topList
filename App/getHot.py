from lxml import etree
from flask import jsonify
from App import db
from App.models import *
import time
import datetime
import calendar
import requests

class get_hot():
    def get_zhihu(self):
        url = 'https://www.zhihu.com/hot'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
            'cookie':'SESSIONID=2V2HarNp4xD2IQKoiwauzRIlByd0bfqkliTVw4adbTY; JOID=VF0RC0NRQN5ZoxcBal8NyMYj0bR5JwmkFcV4VlcTFZwXmm1nWHDp5giuFQxme8fUHyLKTS5DBtjbkv-g9Ebzb6Q=; osd=VFkTBktRRNxUqxcFaFIFyMIh3Lx5IwupHcV8VFobFZgVl2VnXHLk7giqFwFue8PWEirKSSxODtjfkPKo9ELxYqw=; _zap=1e25848d-a5b7-4776-bb4b-1e9ff55f47e6; d_c0="AOBcrUnEChGPTi5Ut-f7vN4AM2w_q8NFFjo=|1585560320"; _ga=GA1.2.1500362301.1585560322; _xsrf=aR2U2PfGixhFD2aA6c3XhFvGXUegaLgs; z_c0="2|1:0|10:1588499487|4:z_c0|92:Mi4xcjd1V0NBQUFBQUFBNEZ5dFNjUUtFU1lBQUFCZ0FsVk5ILUtiWHdETkwxMzlGWFh4Y3JLWHR1YUlwNVg4VnV2aHJB|593ed7685abf764b231fcddd5bccda7e3d5b5ad2efe796e55b7ef6392f9a2e8c"; _gid=GA1.2.721420493.1592644658; tshl=; q_c1=0eaa44f3b5ad4d0b97e753f92d07a771|1596673325000|1588574072000; tst=h; KLBRSID=d1f07ca9b929274b65d830a00cbd719a|1597285410|1597283939; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1597283940,1597285283,1597285385,1597285411; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1597285411'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            html = response.text
        html = etree.HTML(html)
        items = html.xpath('//div[@class="HotList-list"]/section')
        count = 0
        update_time = calendar.timegm(time.gmtime())
        db.session.execute("truncate table t_zhihu_hot")
        for item in items:
            title = item.xpath('div[2]/a/h2/text()')[0]
            content = item.xpath('div[2]/a/p/text()')
            url = item.xpath('div[2]/a/@href')[0]
            print(title, url,content)
            add_Zhihu = t_zhihu_hot()
            add_Zhihu.url = url
            add_Zhihu.title = title
            # add_Zhihu.content = content[0:5]
            add_Zhihu.update_time = update_time
            # 将新创建的用户添加到数据库会话中
            db.session.add(add_Zhihu)
            # 将数据库会话中的变动提交到数据库中, 记住, 如果不 commit, 数据库中是没有变化的.
            db.session.commit()
        if add_Zhihu:
            data = {
                'code': 200,
                'message': "更新成功！"
            }
        return jsonify(data)