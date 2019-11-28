import socket
import ipaddress
import argparse

VERSION="0.0.2"
MESSAGE="IPyCrawl Version 0.0.2\n\n"

def save_file(name_file, info):
    try:
        f=open(name_file,"a+")
        f.write(info+"\n")
        f.close()
    except OSError as err:
        print("OS error: {0}".format(err))

def lookup_host(start_ip,end_ip,name_file=None,output=False):
    print("[.] Starting Check in range of hosts from {} to {} \n" .format(ipaddress.IPv4Address(start_ip),ipaddress.IPv4Address(end_ip)))

    for ip_int in range(int(start_ip), int(end_ip)+1):
        try:
            hostName = socket.gethostbyaddr(str(ip_int))
            strResult = "[+] Host Name for the IP address {} is {}".format(ipaddress.IPv4Address(ip_int), hostName)
            print(strResult)
            if(output==True):
                save_file(name_file,strResult)
        except OSError:
            strResultError = "[-] Error trying to lookup host: %s" % ipaddress.IPv4Address(ip_int)
            print(strResultError)
            if(output==True):
                save_file(name_file,strResultError)
    print("\n[x] Process finished.")

def lookup_single_host(start_ip):
    print("[.] Starting Check in a single host\n")
    try:
        hostName = socket.gethostbyaddr(str(start_ip))
        strResult = "[+] Host Name for the IP address {} is {}".format(ipaddress.IPv4Address(start_ip), hostName)
        print(strResult)
    except OSError:
        strResultError = "[-] Error trying to lookup host: %s" % ipaddress.IPv4Address(start_ip)
        print(strResultError)
    print("\n[x] Process finished.")

def main():
    parser = argparse.ArgumentParser(prog='IPyCrawler', formatter_class=argparse.RawDescriptionHelpFormatter,
    description='''
___________      _____                    _           
|_   _| ___ \    /  __ \                  | |          
  | | | |_/ /   _| /  \/_ __ __ ___      _| | ___ _ __ 
  | | |  __/ | | | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
 _| |_| |  | |_| | \__/\ | | (_| |\ V  V /| |  __/ |   
 \___/\_|   \__, |\____/_|  \__,_| \_/\_/ |_|\___|_|   
             __/ |                                     
            |___/                                    

Version 0.0.2 
Script for Lookup Hostname from Hosts

''')
    parser.add_argument('-s', '--startip',  nargs='?', required=True, help='Start IP')
    parser.add_argument('-e', '--endip', nargs='?', help='End IP')
    parser.add_argument('-o', '--output',  nargs='?', help='Output results to a file e.g results.txt')
    parser.add_argument('--version', action='version', version='%(prog)s 0.0.2')
    args = parser.parse_args()

    if (args.startip and args.endip and args.output):
        start_ip = ipaddress.IPv4Address(args.startip)
        end_ip = ipaddress.IPv4Address(args.endip)
        name_file = args.output
        try:
            f=open(name_file,"w+")
        except OSError as err:
            print("OS error: {0}".format(err))
        
        print(parser.description)
        lookup_host(start_ip,end_ip,name_file,True)
    
    if (args.startip and args.endip and not args.output):
        start_ip = ipaddress.IPv4Address(args.startip)
        end_ip = ipaddress.IPv4Address(args.endip)
        print(parser.description)
        lookup_host(start_ip,end_ip,None,False)

    if (args.startip and not args.endip and not args.output):
        start_ip = ipaddress.IPv4Address(args.startip)
        print(parser.description)
        lookup_single_host(start_ip)

if __name__ == '__main__':
    main()


