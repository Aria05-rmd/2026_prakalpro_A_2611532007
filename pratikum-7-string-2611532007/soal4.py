phone = "082611532007"
masked = phone[:4] + "*" * len(phone[5:-2]) + phone[-3:]
print(masked)