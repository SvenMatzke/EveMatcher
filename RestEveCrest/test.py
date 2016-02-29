import requests
import json
# http://eveonline-third-party-documentation.readthedocs.org/en/latest/sso/intro/
# https://eveonline-third-party-documentation.readthedocs.org/en/latest/crest/authentication/#authenticated-crest
# https://wiki.eveonline.com/en/wiki/CREST_Getting_Started
response = requests.get("https://public-crest.eveonline.com/characterLocationRead/",
                        )
dump = response.json()
print(dump)
with open("E:\PyProject\EveMatcher\RestEveCrest\\auth.json", "w+") as du:
    json.dump(dump, du, indent=True)
