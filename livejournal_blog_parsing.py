import requests  # для выполнения HTTP-запросов
from bs4 import BeautifulSoup  # для парсинга HTML

# открываем с указанием кодировки UTF-8 для корректной записи кириллицы:
with open('blog_content.txt', 'w', encoding='utf-8') as output:

    LINK = 'https://ailev.livejournal.com/?skip='  
    POSTS = 6445
    STEP = 20  # по количеству постов на странице


    def get_posts_text(url: str) -> str:
        # Функция для получения текста из тегов <div> с нужным атрибутом на одной странице

        posts_text = ''
        r = requests.get(url)
        all_page_text = r.text  # получаем текст страницы с автоматической обработкой кодировки
        bs = BeautifulSoup(all_page_text, 'html.parser')
        # получаем текст из всех тегов <div> с нужным атрибутом:
        div_left_text = [element.get_text() for element in bs.find_all(name='div', attrs={'style': 'text-align:left'})]
        posts_text = ' '.join(div_left_text)
        return posts_text


    def parse_all_pages(url: str, posts_number: int) -> str:
        # Функция для парсинга всех страниц блога

        all_pages_post_text = ''
        for page in range(0, posts_number, STEP):
            all_pages_post_text += get_posts_text(url + str(page))
            all_pages_post_text += '\r\n'  # добавляем для разделения страниц
        return all_pages_post_text


    info = parse_all_pages(LINK, POSTS)
    output.write(info)  # записываем в файл с кодировкой UTF-8
    
