import re


def delete_html_tags(html_file: object, result_file: object = 'cleaned.txt')  -> object:
    with open(html_file, 'r', encoding='utf-8') as file :
        html = file.read()

    cleaned_text = re.sub(r'<[^>]+>', '', html)

    with open(result_file, 'w', encoding='utf-8') as file :
        file.write(cleaned_text)
        delete_html_tags('draft.html', 'cleaned.txt')

