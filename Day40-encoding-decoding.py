import random
import string


decoded_str = 'hello my name is siddesh'
encoded_str = 'qGGiddeshsnQB si QQRamenede ym KCeellohUqm '


def gen_random_char(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(0,length))



def add_random_char(str, length):
    return ''.join([gen_random_char(length), str, gen_random_char(length) ])    


def encoding_decoding(str, type):
    out = ''
    if type == 'encoding':
        reversed_list =  list(reversed(str.split(' ')))

        for word in reversed_list:
            if len(word) >= 3:
                word = word[1:] + word[0] # remove first char and append to last
                out += add_random_char(word, 3) + ' '
            else:
                out += ''.join(reversed(list(word))) + ' '

    else:
        splitted_str = str.split(' ')
        for word in splitted_str:
            if len(word) >= 3:                
                word = word[3:len(word)-3] #splitted the 3 random chars prefix and suffix
                word = word[-1] + word[0:len(word)-1] # removed char from last and appended to first 
                out += word + ' '                
            else:
                out += ''.join(reversed(list(word))) + ' '

        out = ' '.join(reversed(out.split(' ')))

    return out


print(   
encoding_decoding(decoded_str, 'encoding')
)
print(

encoding_decoding(encoded_str, 'decoding')
)
