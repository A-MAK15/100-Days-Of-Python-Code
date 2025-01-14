import art
print(art.logo)
# TODO-1: Ask the user for input
user_name = input("What is your name : ")
user_bid = float(input("How much are you bidding? : "))
# TODO-2: Save data into dictionary {name: price}
auction_bids = {user_name : user_bid}
# print(auction_bids)
# TODO-3: Whether if new bids need to be added
more_bidders = input("Are there any more bidders ?, 'Yes' or 'No'").lower()
while more_bidders == "yes":
    print("\n" * 100)
    user_name = input("What is your name : ")
    user_bid = float(input("How much are you bidding? : "))
    auction_bids = {user_name: user_bid}
    more_bidders = input("Are there any more bidders ?, Type 'Yes' or 'No'").lower()
# TODO-4: Compare bids in dictionary
highest_bid = -9999
for bid in auction_bids:
    if auction_bids[bid] > highest_bid:
        highest_bid = auction_bids[bid]
    else:
        highest_bid = highest_bid
    print(f"Highest bidder is {bid} with ${highest_bid}")
