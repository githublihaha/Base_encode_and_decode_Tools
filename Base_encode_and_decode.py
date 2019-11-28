import base36
import base58
import base62
import base64
import base91
import base92





def encode(txt):
    print("[+]input is ", end="")
    print(txt)

    print("==============================================================================")
    #base16
    print("[+]base16 encode: ", end="")
    print(base64.b16encode(txt))

    #base32
    print("[+]base32 encode: ", end="")
    print(base64.b32encode(txt))


    #base36
    try:
        base36_m_str = bytes.decode(txt)
        base36_m_int = int(base36_m_str)

        base36_cipher = base36.dumps(base36_m_int)
        print("[+]base36 encode: ", end="")
        print(base36_cipher)
    except Exception as e:
        print("[-]base36 encode: ", end="")
        print(e)

    #base58
    print("[+]base58 encode: ", end="")
    print(base58.b58encode(txt))

    #base62
    print("[+]base62 encode: ", end="")
    print(base62.encodebytes(txt))

    #base64
    print("[+]base64 encode: ", end="")
    print(base64.b64encode(txt))

    #base85
    print("[+]base85 encode: ", end="")
    print(base64.b85encode(txt))

    #base91
    print("[+]base91 encode: ", end="")
    print(base91.encode(txt))

    #base92
    print("[-]base92 encode: ", end="")
    #print(b92encode(txt))
    print("Please run python27 , then import base92 , then ", end="")
    print("base92.encode(\'string\')")


def decode(txt):
    print("[+]input is ", end="")
    print(txt)
    print("==============================================================================")

    #base16
    try:
        base16_decode = base64.b16decode(txt)
        print("[+]base16 decode: ", end="")
        print(base16_decode)
    except Exception as e:
        print("[-]base16 decode: ", end="")
        print(e)


    #base32
    try:
        base32_decode = base64.b32decode(txt)
        print("[+]base32 decode: ", end="")
        print(base32_decode)
    except Exception as e:
        print("[-]base32 decode: ", end="")
        print(e)


    #base36
    try:
        base36_decode = base36.loads(txt)
        print("[+]base36 decode: ", end="")
        print(base36_decode)
    except Exception as e:
        print("[-]base36 decode: ", end="")
        print(e)


    #base58
    try:
        base58_decode = base58.b58decode(txt)
        print("[+]base58 decode: ", end="")
        print(base58_decode)
    except Exception as e:
        print("[-]base58 decode: ", end="")
        print(e)


    #base62
    try:
        base62_c_string = bytes.decode(txt)
        base62_decode = base62.decode(base62_c_string)
        print("[+]base62 decode: ", end="")
        print(base62_decode)
    except Exception as e:
        print("[-]base62 decode: ", end="")
        print(e)


    #base64
    try:
        base64_decode = base64.b64decode(txt)
        print("[+]base64 decode: ", end="")
        print(base64_decode)
    except Exception as e:
        print("[-]base64 decode: ", end="")
        print(e)


    #base85
    try:
        base85_decode = base64.b85decode(txt)
        print("[+]base85 decode: ", end="")
        print(base85_decode)
    except Exception as e:
        print("[-]base85 decode: ", end="")
        print(e)


    #base91
    base91_decode = base91.decode(bytes.decode(txt))
    if( base91_decode == b'' ):
        print("[-]base91 decode: not base91")
    else:
        print("[+]base91 decode: ", end="")
        print(base91_decode)



    #base92
    print("[-]base92 decode: ", end="")
    #print(b92encode(txt))
    print("Please run python27 , then import base92 , then ", end="")
    print("base92.decode(\'string\')")



if __name__ == '__main__':
    print("Welcome to base series encode and decode")
    txt = input("Please input your string ::: ")


    txt = str.encode(txt)
    flag = int(input("Please input encode(0) or decode(1) ::: "))

    if(flag == 0):
        encode(txt)
    else:
        decode(txt)
