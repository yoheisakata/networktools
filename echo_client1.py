# Echo Client Program

import socket 
import sys, getopt

def usage():
    print("use")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:p:", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    port = ''
    host = ''
    for o, a in opts:
        if o == "-p":
            port = a
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--destination"):
            host = a
        else:
            assert False, "unhandled option"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, int(port)))
        s.sendall(b'Hello, world')
        print('Sent all data')
#        s.shutdown(1)
#       s.close()
#        exit()
        while True:
            data = s.recv(4)
            print('Received', data)
            if not data:
                break
        print('DONE')
        

if __name__ == "__main__":
    main()







  
