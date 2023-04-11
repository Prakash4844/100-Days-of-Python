import os
import Art

# HINT: You can call clear() to clear the output in the console.
# NOTE: For making it work in Pycharm do this go to RUN->Edit Configurations->Edit Configuration Templates...
#                                                   Select python from right pane-> Check 'Emulate Terminal
#                                                   in Output Console'
print(Art.logo)
bids = {}
highest_bidder = ""
highest_bid = 0


def clear():
    os.system("clear")


should_restart = True

while should_restart:
    usr_name = input("What is your name?: ")
    usr_bid = int(input("What's your bid?: $"))
    bids[usr_name] = usr_bid

    stop_bidding = int(input("Are there any other bidders? Press 1 for YES and 0 for NO: "))

    if stop_bidding:
        clear()
        pass
    else:
        break

for key in bids:
    if bids[key] > highest_bid:
        highest_bidder = key
        highest_bid = bids[key]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
