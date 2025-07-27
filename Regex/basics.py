import re

print(re.findall(r'\d+','abc123def456'))
print(re.search(r'a','apple art ball ant axe'))

re.findall(r'\W+', 'This is 2024')  # ['This', 'is', '2024']
print(re.findall(r'\d{2}', 'Year2025'))   # ['20', '25']
print(re.findall(r'(raj|kumar)','Raj and kumarRaj Kumar'))
