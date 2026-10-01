# def add_tag(profile, tag):
#     updated = profile.copy()           #shallow copy - modification of list will touch original
#     updated['language'] = profile['language'].copy()    #deep copy - original is free of updated
#     updated['language'].append(tag)
#     updated['language'].extend(['go', 'rust'])
#     updated['language'].insert(1, 'C+')
#     return updated

# original = {'name': 'Ada', 'language': ['python']}
# changed = add_tag(original, 'javascript')
# print(original['language'])
# print()

def add_tag(profile, tag):
    updated = profile.copy()
    updated['tags'] = profile['tags'].copy()
    updated["tags"].append(tag)
    return updated
original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")
    #if you append another tag to returned list (all reflect before assertions)
print(original["tags"])
print(changed)
print(original)
print(changed is original)
print(changed == original)
print(changed["tags"] is original["tags"])
print()
#Write assertions showing that the original tags remain unchanged and the returned tags contain the new tag.  [6 marks]
assert original['tags'] == ['python'], 'Original tags didnt remain unchanged'
assert changed['tags'] == ['python', 'testing'], 'Returned tags dont contain new tag'
#Then append another tag to the returned list and assert that the original still has only its initial tag.
changed['tags'].append('vs code')
assert original['tags'] == ['python'], 'Original tag changed after 2nd append'

