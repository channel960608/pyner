'''
@Author: Caspar
@Date: 2019-11-05 12:16:43
@LastEditors: Caspar
@LastEditTime: 2019-11-05 15:59:14
@Description: file content
'''
#%%
import ner
#%%
tagger = ner.HttpNER(host='localhost', port=8080, location='/ner')
#%%
tagger.get_entities("University of California is located in California, United States")
#%%
tagger.json_entities("Alice went to the Museum of Natural History.")

