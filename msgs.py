from clr import splv

splv = splv()

class Messages:
    def error(message):
        print(f"[{splv.CRED}ERROR{splv.CEND}] {splv.CRED}{message}{splv.CEND}")
    def success(message):
        print(f"[{splv.CGREEN}OK{splv.CEND}] {splv.CGREEN}{message}{splv.CEND}")
    def att(message):
        print(f"[{splv.CBLUE2}Attacking{splv.CEND}] {message}", end="\r")