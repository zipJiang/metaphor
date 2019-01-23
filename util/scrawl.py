import requests
from bs4 import BeautifulSoup


def crawl_metaphor(website='http://www.cms9.com/zhidao/biyuju/'):
    upper_bound = 10
    host = 'http://www.cms9.com'
    bar_check = '比喻句'
    junk_set = set(['：', '，', ' ', '、', '。', '. ', '）', '.'])

    total_list = []

    # get a set of headers
    headers = {
        "Host": "www.cms9.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6,ja;q=0.5",
        "Accept-Encoding": "gzip, deflate"
    }

    for index in range(1, upper_bound + 1):
        main_url = website + str(index) + '/'

        main_link = requests.get(main_url, headers=headers)
        main_link.encoding = 'utf-8'

        assert main_link.status_code == 200

        frame_text = main_link.text
        frame_soup = BeautifulSoup(frame_text, 'html.parser')

        source_list = frame_soup.find_all('dt')

        for source in source_list:
            title = source.a.string
            suffix = source.a['href']
            link = host + suffix

            # Check if the title is valid
            if title[-3:] == bar_check:
                print (title)
                # visit the link
                single_source = requests.get(link, headers=headers)
                assert single_source.status_code == 200
                single_source.encoding = 'utf-8'
                corpus = single_source.text
                corpus_soup = BeautifulSoup(corpus, 'html.parser')
                main_corpus = corpus_soup.find(class_='content')

                entry_list = main_corpus.find_all('p')

                sentence_list = [e.text for e in entry_list]

                count = 1
                first = True
                for sentence in sentence_list:
                    if first:
                        first = False
                        count += 1
                        continue
                    # measure the count length
                    length = 1
                    if count >= 10:
                        length = 2
                    s = sentence[2+length:]
                    count += 1

                    # trimming up
                    throw = False
                    if len(s) < 10:
                        continue
                    while s[0] in junk_set:
                        if len(s) < 10:
                            throw = True
                            break
                        s = s[1:]

                    if len(s) < 10 or throw:
                        continue

                    total_list.append(s)

        # Write data to file

        collected = open('../data/auto_collected/metaphor.txt', 'w')
        for line in total_list:
            collected.write(line + '\n')

        collected.close()


if __name__ == '__main__':
    crawl_metaphor()
