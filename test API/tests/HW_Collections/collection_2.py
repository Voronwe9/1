courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
            ['Никита', 'Лев', 'Яков', 'Александра', 'Анна', 'Владимир', 'София', 'Василий', 'Полина', 'Дмитрий', 'Яков', 'Александра', 'Александра'],
            ['Лев', 'Анна', 'Екатерина', 'Виктория', 'Яков', 'Мадина', 'Елисей', 'Дмитрий', 'Яков', 'Ксения', 'Александра'],
            ['Марк', 'Виктория', 'Александр', 'Егор','Александра', 'Андрей', 'Агата', 'Владислава', 'Александра', 'Денис', 'Лев', 'Алиса']
        ]

def top_of_names(mentors):
    all_list = []
    for m in mentors:
        all_list+=m

    all_names_list = []
    for mentor in all_list:
        name = str(mentor).split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)
    unique_names = sorted(list(unique_names))

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])
    popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = popular[0:3]

    top_str = []
    for name, count in top_3:
      top_str.append(name + ': ' + str(count))
    return f'{" раз(а), ".join(top_str)} раз(а)'
if __name__ == '__main__':

    res = str(top_of_names(mentors))
    print(res)

