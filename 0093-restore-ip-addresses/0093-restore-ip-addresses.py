class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.validIps=[]
        def isValidIp(ip:str)->bool:
            print(ip)
            subNets = ip.split(".")
            if len(subNets)!=4:
                return False
            for eachSubNet in subNets:
                if not eachSubNet.isdigit() or int(eachSubNet) < 0 or int(eachSubNet) > 255:
                    return False
                if len(eachSubNet) > 1 and eachSubNet[0] == '0':
                    return False
            return True
        def backTrack(prefix, suffix,dots):
            if dots> 3 or not suffix:
                return
            if dots ==3:
                if isValidIp(prefix+suffix):
                    self.validIps.append(prefix+suffix)
                return
            for index in range(1,(len(suffix))):
               
                backTrack(prefix + suffix[:index]+".",suffix[index:],dots+1)
               
            return
        backTrack("",s,0)
        return self.validIps