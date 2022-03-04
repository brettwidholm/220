def encode(message, key):
    final_message = ''
    for i in message:
        encryption = ord(i) + key
        final_message = final_message + (chr(encryption))

    return final_message

def encode_better(message, key):
    message_list = []
    key_list = []
    final_message = ''

    for i in message:
        message_list.append(ord(i)-65)

    for j in key:
        key_list.append(ord(j)-65)

    for k in range(len(message)):
        encryption = (message_list[k] + key_list[k % (len(key))]) % 58
        new_message = chr(encryption + 65)
        final_message = final_message + new_message

    return final_message