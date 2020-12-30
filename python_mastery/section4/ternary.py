# ternary operator

# condition_if_true if condition else condition_if_false

is_friend = True
say_hi = "hello!" if is_friend else "i don't know you"

print(say_hi)

# short circuiting
# more efficient using OR

is_magician = False
is_expert = True

if is_magician and is_expert:
    print("youu are a master magician")
elif is_magician and not is_expert:
    print("at least you're getting there")
elif not is_magician:
    print("you need magic powers")
