import re

def extract_domains(emails):
    domains = [re.search(r'@([a-zA-Z0-9.-]+)', email).group(1) for email in emails]
    return domains

emails = ['test@example.com', 'user@domain.org']
print(extract_domains(emails))
