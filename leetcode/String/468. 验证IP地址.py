class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if not IP:
            return "Neither"

        if IP.count(":") == 7:
            return self.valid_IPv6(IP)
        elif IP.count(".") == 3:
            return self.valid_IPv4(IP)
        else:
            return "Neither"

    def valid_IPv4(self, ip):
        ip = ip.split(".")

        for chunk in ip:
            if len(chunk) == 0 or len(chunk) > 3:
                return "Neither"
            elif not chunk.isdigit() or chunk[0] == "0" and len(chunk) != 1:
                return "Neither"
            elif int(chunk) < 0 or int(chunk) > 255:
                return "Neither"
        return "IPv4"

    def valid_IPv6(self, ip):
        ip = ip.split(":")
        hexdigits = '0123456789abcdefABCDEF'

        for chunk in ip:
            if len(chunk) == 0 or len(chunk) > 4:
                return "Neither"

            judge = 0
            for c in chunk:
                if c in hexdigits: judge += 1

            if len(chunk) == 0 or len(chunk) > 4 or judge != len(chunk):
                return "Neither"

        return "IPv6"

"""
官方方法最后一种
对于 IPv4 地址，通过界定符 . 将地址分为四块；对于 IPv6 地址，通过界定符 : 将地址分为八块。

对于 IPv4 地址的每一块，检查它们是否在 0 - 255 内，且没有前置零。

对于 IPv6 地址的每一块，检查其长度是否为 1 - 4 位的十六进制数。

作者：LeetCode
链接：https://leetcode-cn.com/problems/validate-ip-address/solution/yan-zheng-ip-di-zhi-by-leetcode/
来源：力扣（LeetCode）
"""