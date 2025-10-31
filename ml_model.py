import sys
,
with open(sys.argv[1], "rn") as f:
   components = f.read().splitlines()

malicious_keywords = ["malicious", "keylogger", "ransomware", "trojan", ".exe"]

malicioius_found = False

for comp in components:
    for keyword in malicious_keywords:
         print(f" ML classifier: Detected malicious pattern in: {comp}")
         malicious_found = true

if malicious_found:
     exit(1)
else:
   print("ML classifier: File appears clean")
   exit(0)
