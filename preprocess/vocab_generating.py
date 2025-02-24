import pickle

if __name__=="__main__":
    f_train = open("data/train_data", "r")
    user_dict = {}
    item_dict = {}
    cat_dict = {}
    
    print ("vocab generating...")
    for line in f_train:
        arr = line.strip("\n").split("\t")
        clk = arr[0]
        uid = arr[1]
        mid = arr[2]
        cat = arr[3]
        timestepnow = arr[4]
        mid_list = arr[5]
        cat_list = arr[6]
        timestep_list = arr[7]
        
        if uid not in user_dict:
            user_dict[uid] = 0
        user_dict[uid] += 1
        if mid not in item_dict:
            item_dict[mid] = 0
        item_dict[mid] += 1
        if cat not in cat_dict:
            cat_dict[cat] = 0
        cat_dict[cat] += 1
        if len(mid_list) == 0:
            continue
        for m in mid_list.split(""):
            if m not in item_dict:
                item_dict[m] = 0
            item_dict[m] += 1
        for c in cat_list.split(""):
            if c not in cat_dict:
                cat_dict[c] = 0
            cat_dict[c] += 1
    
    sorted_user_dict = sorted(user_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_item_dict = sorted(item_dict.items(), key=lambda x:x[1], reverse=True)
    sorted_cat_dict = sorted(cat_dict.items(), key=lambda x:x[1], reverse=True)
    
    uid_voc = {}
    index = 0
    for key, value in sorted_user_dict:
        uid_voc[key] = index
        index += 1
    
    mid_voc = {}
    mid_voc["default_mid"] = 0
    index = 1
    for key, value in sorted_item_dict:
        mid_voc[key] = index
        index += 1
    
    cat_voc = {}
    cat_voc["default_cat"] = 0
    index = 1
    for key, value in sorted_cat_dict:
        cat_voc[key] = index
        index += 1
    
    pickle.dump(uid_voc, open("data/user_vocab.pkl", "w"))
    pickle.dump(mid_voc, open("data/item_vocab.pkl", "w"))
    pickle.dump(cat_voc, open("data/category_vocab.pkl", "w"))
