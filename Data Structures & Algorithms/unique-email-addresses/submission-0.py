class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local, domain = email.split("@")
            temp = ""
            for i in range(len(local)):
                if local[i] == ".":
                    continue
                elif local[i] == "+":
                    break
                temp += local[i]
            fixed = temp + "@" + domain
            res.add(fixed)
        return len(res)