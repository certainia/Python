current_users = ['john','mary','yokie','kangkang','lary']
new_users = ['Joe','john','Kangkang','lary','roam']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("please try to use others.")
    else:
        print("no use,you can use it.")
        