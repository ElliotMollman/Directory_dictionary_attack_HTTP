import requests
import argparse


def banner():
    font = """
    ______ _       _ _        _  ______            _       
    |  _  (_)     (_) |      | | | ___ \          | |      
    | | | |_  __ _ _| |_ __ _| | | |_/ /_ __ _   _| |_ ___ 
    | | | | |/ _` | | __/ _` | | | ___ \ '__| | | | __/ _ |
    | |/ /| | (_| | | || (_| | | | |_/ / |  | |_| | ||  __/
    |___/ |_|\__, |_|\__\__,_|_| \____/|_|   \__,_|\__\___|
            __/ |                                        
            |___/
                                            By Elliot Mollman
    _________________________________________________________

    """
    print(font)

def HTTP_brute_force(url, wordlist):
    with open(wordlist, "r") as file:
        wordlist = file.read().splitlines()
    for directory in wordlist:
        directory_url = url + "/" + directory
        response = requests.get(directory_url)
        if response.status_code == 200:
            print("[+] Directory Found:", directory_url)
        elif response.status_code != 200:
            print(f"[-] {directory_url} Not Found")

if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(prog="Directory_dictionary_attack_HTTP",description="A toolkit for attacking HTTP servers via dictionaries ")
    parser.add_argument("-u", "--url", type=str, metavar="", help="The url to be brute forced", required=True)
    parser.add_argument("-w", "--wordlist", type=str, metavar="", help="The FULL path of the wordlist. Do not add / at the end of the possible directories", required=True)
    args = parser.parse_args()
    HTTP_brute_force(args.url, args.wordlist)


