class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # "testemail@leetcode.com"
        # ,"testemail@leetcode.com",
        # "testemail@lee.tcode.com"

        res = set()

        for e in emails:
            name, domain = e.split('@')

            local = name.split('+')[0].replace('.','') # test.email+alex -> after split: [test.email,alex] take the the first one [0] with replace '.',''
            # print(local)

            res.add(local+'@'+domain)

        return len(res)
