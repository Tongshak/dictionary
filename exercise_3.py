contact_list={
    "kenneth" : 7773,
     "sam" : 7643,
      "paul" : 4356,
}
print(contact_list)
print(contact_list["sam"])
print(contact_list.get("sam"))
print(contact_list.keys())
contact_list.update({"kenneth": "7656"})
print(contact_list)
del contact_list["sam"]
print(contact_list)
#contact_list.pop("sam")
print(contact_list)
print(contact_list.items())
contact_list.popitem
print(contact_list.popitem())
print(contact_list.copy())
new=contact_list
new.popitem()
print(new)
