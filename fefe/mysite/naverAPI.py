import json
import urllib.request
import re

class NaverAPI:




    def getHangul(self, string):
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자
        # hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')  # 위와 동일
        result = hangul.sub('', string)  # 한글과 띄어쓰기를 제외한 모든 부분을 제거
        return result


    # 참고 json url : http://pythonstudy.xyz/python/article/205-JSON-데이타

    def context(self, url):
        request = urllib.request.Request(url)
        self.setClientInfo(request)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            list = response_body.decode('utf-8')
        else:
            print("Error Code:" + rescode)
        return list

    def setClientInfo(self, request):
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)



    def getNaverBlogPost(self, postTitle):
        encText = urllib.parse.quote(postTitle)
        url = "https://openapi.naver.com/v1/search/blog?query=" + encText  # json 결과
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        list = self.context(url)
        list = json.loads(list)

        for h in list['items']:
            h['link'] = h['link'].replace('&amp;', '&')
            h['title'] = self.getHangul(h['title'])
            h['description'] = self.getHangul(h['description'])

        return list

    # json을 diction 형태로 바꾼 후 가지고 놀기
    # replace 는 네이버 api를 사용하다 안돼서 중간에redirect부분을 빼니까 잘 되더라~~ 개이득

    def outNaverBlogPost(self, list):
        list = json.loads(list)
        print(list)
        for h in list['items']:
            print(h['title'])
            print(h['link'].replace('Redirect=Log&amp;', '/'))


    def getNaverImage(self, imgTitle):
        encText = urllib.parse.quote(imgTitle)
        url = "https://openapi.naver.com/v1/search/image?query=" + encText  # json 결과
        list = self.context(url)
        list = json.loads(list)
        return list


    def outNaverImage(self, list):

        print(list)
        for h in list['items']:
            print(h['title'])
            print(h['link'])
