import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        begin = html.count('<')
        while begin != 0:
            start = html.find('<')
            end = html.find('>') + 1
            html = html.replace(html[start:end], '')
            begin = html.count('<')
    with codecs.open(result_file, 'w', 'utf-8') as clean:
        clean.write(html)


delete_html_tags('draft.html')
