url = 'https://rezka.ag/films/action/47246-bystree-puli-2022.html'

article_id = url.split('/')[-1]
article_id = article_id[:-5]
print(article_id)

# import json

# with open("film_dict.json") as file:
#         film_dict = json.load(file)
        
# id = '53552-vsevidyaschee-oko-2022'

# if id in film_dict:
#     print("ok")
# else:
#     print("add")