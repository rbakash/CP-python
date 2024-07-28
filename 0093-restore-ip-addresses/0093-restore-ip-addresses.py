class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        
        self.validIps = []
        def backTrack(start, dot,ip):

            if dot == 4 and start == len(s):
                self.validIps.append(ip[:-1])
                return

            if dot > 4:
                return

            for i in range(start, min(start+3, len(s))):
                if int(s[start:i+1]) < 256 and (start == i or s[start] != "0"):
                    backTrack(i+1,dot + 1, ip + s[start:i+1] + ".")

            return

        backTrack(0, 0,"")
        return self.validIps
