def km_to_miles():
    conv_frac= 0.621371
    kilometer=int(input("enter kilometer in number to calculate miles: "))
    miles=kilometer*conv_frac
    print(f"{kilometer} kilometer  is equal to {miles} miles")
km_to_miles()