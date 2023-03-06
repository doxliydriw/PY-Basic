import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        # html_file = open("draft.html", "r", encoding='utf-8')
        line = ''
        cleanlist = []
        for text in file:
            line += text
            start_tag_count = line.count('<')
            end_tag_count = line.count('>')
            if start_tag_count == end_tag_count:
                ix = 1
                while ix <= start_tag_count:
                    a = line[(line.find('<')):(line.find('>')) + 1]
                    line = line.replace(a, '')
                    ix += 1
                cleanlist.append(line)
                line = ''
        clean_cell = 0
        cleanlist1 = []
        while clean_cell < len(cleanlist):
            qw = cleanlist[clean_cell]
            qw = qw.replace(' ', '').replace('\n', '')
            if len(qw) != 0:
                cleanlist1.append(cleanlist[clean_cell])
            clean_cell += 1
        qw = cleanlist1.pop()
        qw = qw.replace('\n', '')
        cleanlist1.append(qw)
        clean1 = open(result_file, "a", encoding='utf-8')
        clean1.writelines(cleanlist1)
        # html_file.close()
        clean1.close()
        open(result_file)


delete_html_tags('draft.html')