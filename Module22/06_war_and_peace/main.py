# TODO здесь писать код
import collections
import zipfile


def unzip(archive):
    with zipfile.ZipFile(archive, 'r') as zfile:
        for i_file_name in zfile.namelist():
            zfile.extract(i_file_name)


def collect_stats(file_name_collect):
    rezult = {}
    if file_name_collect.endswith('.zip'):
        unzip(file_name_collect)
        file_name_collect = ''.join((file_name_collect[:-3], 'txt'))
    with open(file_name_collect, 'r', encoding='UTF-8') as text_file:
        for i_line in text_file:
            for j_char in i_line:
                if j_char.isalpha():
                    if j_char not in rezult:
                        rezult[j_char] = 0
                    rezult[j_char] += 1
    return rezult


def print_stats(stats_print):
    print("+{:-^19}+".format('+'))
    print("|{: ^9}|{: ^9}|".format('буква', "частота"))
    print("+{:-^19}+".format('+'))
    for char, count in stats_print.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format('+'))


def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]
    return sorted_dict


file_name = 'voyna-i-mir.zip'
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)
