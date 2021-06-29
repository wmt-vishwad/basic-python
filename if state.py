is_female = True
is_tall = True
if is_female or is_tall:
    print("you are female or tall or both")
elif is_female and not (is_tall):
    print("you are a short female")

elif not(is_female) and is_tall:
    print("you are not a female but are tall")
else:
    print("you not female or tall")
