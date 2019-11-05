'''
@Author: Caspar
@Date: 2019-11-05 12:16:43
@LastEditors: Caspar
@LastEditTime: 2019-11-05 17:40:29
@Description: file content
'''
#%%
import nerer
#%%
tagger = nerer.HttpNER(host='localhost', port=8080, location='/ner')
#%%
tagger.get_entities("University of California is located in California, United States")
#%%
tagger.json_entities("Alice went to the Museum of Natural History.")



# %%
