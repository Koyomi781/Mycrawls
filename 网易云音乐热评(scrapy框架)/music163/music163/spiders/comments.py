import scrapy
import execjs
import json
import datetime
from ..items import Music163Item


class CommentsSpider(scrapy.Spider):
    name = "comments"
    page_num = 1


    def start_requests(self):
        cookies = {
            'NMTID': '00OL8Pdf5TdSqHTZk1Qg9Kp8Pv4ymkAAAGN04PoOw',
            '_iuqxldmzr_': '32',
            '_ntes_nnid': 'ee049b7fa2d0056b2fb8c8475faaa2b5,1708650654657',
            '_ntes_nuid': 'ee049b7fa2d0056b2fb8c8475faaa2b5',
            'WEVNSM': '1.0.0',
            'WNMCID': 'oxbmzd.1708650655278.01.0',
            'timing_user_id': 'time_ASzSM1f92B',
            '_ga': 'GA1.1.1584874827.1711532729',
            '_ga_C6TGHFPQ1H': 'GS1.1.1711543748.2.1.1711544278.0.0.0',
            'WM_TID': '02OP8woNRoRERAARQULRrI%2FjAsq3xV6Y',
            'sDeviceId': 'YD-t%2FfFB1E6ZQdFRhEURQPUvNviBs7jwOQ%2F',
            'ntes_utid': 'tid._.FyHwBAuuj3hEU1AABQeFvZr2Vo%252ByhORI._.0',
            'JSESSIONID-WYYY': 'ojSIzabHIDR9MyJiu5kprh8cAAMJFDpuqsnGkhJKstljj%2B3YVEvQOgUeMAMsjzW1qcoW%2BBxHWHF3jxFI5N04qaczQ8Ez7YwgxHdfBKqlXC2TOnqQjZe9eaElvbwGR4fEuaDS9euMGaQrwujjwiOUbrYA6jmP%5CYuTE%2F%2FqNM1JNN0%5CMTbX%3A1712647988402',
            'WM_NI': '4oRZ%2By3MVmL6YbnhPn3seNm87Kqz%2FiI2hQOTprEARuCjQ2OkUg1sLcUcBxU%2BI3OkxbUbrGqXoe6BIcAs4b4j5gdSG86e5WKiba5WzEHlqQGRVgTFXR%2BjCJ2Oc78X9RHBVWw%3D',
            'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeb6f3539cb58797d764aaef8eb6c14f928e9b83d17b899f989bc967b2bc8788ce2af0fea7c3b92af8b19ebbaa73f1939a8ecf3e9bbea289d366f1adabaff034f595bf9bae638beea8b2ce60b4ae8ba2d17f81b69fd3ce6197b9ff94cf6997bd8e99d8218bed818cfb6a97bebea8f454adbbfaa3cc6983adfc83b762f7b9acb4c634f6bbfbb8ca63a2bffbb8f94f8cb4bfb2c65a96b99ca7db5ae9b68dabb145a1e9f8b9bc5a8c9e9ab8f637e2a3',
        }
        params = {
            "rid": "A_PL_0_3778678",
            "threadId": "A_PL_0_3778678",
            "pageNo": '1',
            "pageSize": "20",
            "cursor": "-1",
            "offset": "0",
            "orderType": "1",
            "csrf_token": ""
        }
        js1 = open(r'D:\A\python\scrapyprojects\music163\music163\spiders\param.js', 'r', encoding='utf-8').read()
        datax = execjs.compile(js1).call('main', params)

        data = {
            'params': datax['encText'],
            'encSecKey': datax['encSecKey'],
        }
        print(f'##########正在爬取第1页##########')
        yield scrapy.FormRequest(
            url='https://music.163.com/weapi/comment/resource/comments/get',
            formdata=data,
            cookies=cookies,
            callback=self.next_parse,
        )
    # def parse(self, response, **kwargs):
    #     comment_list = json.loads(response.text)['data']['comments']
    #     cursor = comment_list[-1]['time']
    #     item = Music163Item()
    #     for comment in comment_list:
    #         item['nickname'] = comment['user']['nickname']
    #         t = comment['time']
    #         date_time = datetime.datetime.fromtimestamp(t / 1000)
    #         time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    #         item['time'] = time
    #         item['likedCount'] = comment['likedCount']
    #         item['ipLocation'] = comment['ipLocation']['location']
    #         item['content'] = comment['content']
    #         item['OS_TYPE'] = comment['extInfo']['endpoint']['OS_TYPE']
    #         yield item

    def next_parse(self, response, **kwargs):
        self.page_num += 1
        comment_list = json.loads(response.text)['data']['comments']
        cursor = comment_list[-1]['time']
        item = Music163Item()
        for comment in comment_list:
            item['nickname'] = comment['user']['nickname']
            t = comment['time']
            date_time = datetime.datetime.fromtimestamp(t / 1000)
            time = date_time.strftime('%Y-%m-%d %H:%M:%S')

            try:
                item['time'] = time
            except Exception as e:
                item['time'] = '未知'

            try:
                item['likedCount'] = comment['likedCount']
            except Exception as e:
                item['likedCount'] = '未知'

            try:
                item['ipLocation'] = comment['ipLocation']['location']
            except Exception as e:
                item['ipLocation'] = '未知'

            try:
                item['content'] = comment['content'].replace('\n', '')
            except Exception as e:
                item['content'] = '未知'

            try:
                item['OS_TYPE'] = comment['extInfo']['endpoint']['OS_TYPE']
            except Exception as e:
                item['OS_TYPE'] = '未知'

            yield item
        # 14007
        if self.page_num < 14007:
            cookies = {
                'NMTID': '00OL8Pdf5TdSqHTZk1Qg9Kp8Pv4ymkAAAGN04PoOw',
                '_iuqxldmzr_': '32',
                '_ntes_nnid': 'ee049b7fa2d0056b2fb8c8475faaa2b5,1708650654657',
                '_ntes_nuid': 'ee049b7fa2d0056b2fb8c8475faaa2b5',
                'WEVNSM': '1.0.0',
                'WNMCID': 'oxbmzd.1708650655278.01.0',
                'timing_user_id': 'time_ASzSM1f92B',
                '_ga': 'GA1.1.1584874827.1711532729',
                '_ga_C6TGHFPQ1H': 'GS1.1.1711543748.2.1.1711544278.0.0.0',
                'WM_TID': '02OP8woNRoRERAARQULRrI%2FjAsq3xV6Y',
                'sDeviceId': 'YD-t%2FfFB1E6ZQdFRhEURQPUvNviBs7jwOQ%2F',
                'ntes_utid': 'tid._.FyHwBAuuj3hEU1AABQeFvZr2Vo%252ByhORI._.0',
                'JSESSIONID-WYYY': 'ojSIzabHIDR9MyJiu5kprh8cAAMJFDpuqsnGkhJKstljj%2B3YVEvQOgUeMAMsjzW1qcoW%2BBxHWHF3jxFI5N04qaczQ8Ez7YwgxHdfBKqlXC2TOnqQjZe9eaElvbwGR4fEuaDS9euMGaQrwujjwiOUbrYA6jmP%5CYuTE%2F%2FqNM1JNN0%5CMTbX%3A1712647988402',
                'WM_NI': '4oRZ%2By3MVmL6YbnhPn3seNm87Kqz%2FiI2hQOTprEARuCjQ2OkUg1sLcUcBxU%2BI3OkxbUbrGqXoe6BIcAs4b4j5gdSG86e5WKiba5WzEHlqQGRVgTFXR%2BjCJ2Oc78X9RHBVWw%3D',
                'WM_NIKE': '9ca17ae2e6ffcda170e2e6eeb6f3539cb58797d764aaef8eb6c14f928e9b83d17b899f989bc967b2bc8788ce2af0fea7c3b92af8b19ebbaa73f1939a8ecf3e9bbea289d366f1adabaff034f595bf9bae638beea8b2ce60b4ae8ba2d17f81b69fd3ce6197b9ff94cf6997bd8e99d8218bed818cfb6a97bebea8f454adbbfaa3cc6983adfc83b762f7b9acb4c634f6bbfbb8ca63a2bffbb8f94f8cb4bfb2c65a96b99ca7db5ae9b68dabb145a1e9f8b9bc5a8c9e9ab8f637e2a3',
            }
            params = {
                "rid": "A_PL_0_3778678",
                "threadId": "A_PL_0_3778678",
                "pageNo": str(self.page_num),
                "pageSize": "20",
                "cursor": cursor,
                "offset": "0",
                "orderType": "1",
                "csrf_token": ""
            }
            print(f'##########正在爬取第{self.page_num}页##########')
            js1 = open(r'D:\A\python\scrapyprojects\music163\music163\spiders\param.js', 'r', encoding='utf-8').read()
            datax = execjs.compile(js1).call('main', params)

            data = {
                'params': datax['encText'],
                'encSecKey': datax['encSecKey'],
            }
            yield scrapy.FormRequest(
                url='https://music.163.com/weapi/comment/resource/comments/get',
                formdata=data,
                cookies=cookies,
                callback=self.next_parse,
            )





