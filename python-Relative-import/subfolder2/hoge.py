from subfolder import huga

def func_hello_hoge():
    print('Hello from hoge')
    huga.func_hello_huga_from_hoge()

if __name__ == '__main__':
    func_hello_hoge()