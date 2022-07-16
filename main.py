# using a basic function
# def display_message():
#     print("I know how to make functions")

# display_message()

# using a basic function using one parameter
# def favorite_book(title):
#     print(f"One of my favorite book is {title}")
#
#
# name = input("what is one of your favorite book")
# favorite_book(name)


# def make_shirt(size='Large', text='I love python'):
#     print(f"The size of the Tshirt will be: {size}\nThe text message would say: {text}")
#
#
# make_shirt('small', 'crazy people do crazy things')  # positional argument
#
# make_shirt(size='small', text='crazy people do crazy things')  # keyword argument
# make_shirt()
#

# def city_country(city, country):
#     formatted = f"{city}, {country} "
#     return formatted.title()
#
#
# cityCountry = city_country('santiago', 'chile')
# print(cityCountry)

#
# def make_album(artist_name, album_title, num_of_song=None):
#
#     music_album = {artist_name.title(): album_title.title()}
#     if num_of_song:
#         music_album['num_of_song'] = num_of_song
#     return music_album
#
#
# active = True
# while active:
#     name = input("enter the name of the artist\n press (q) to quit:")
#     if name == 'q':
#         break
#     title = input("enter the name of the album\n press (q) to quit:")
#     if title == 'q':
#         break
#     music_album_info = make_album(name, title)
#
#     print(music_album_info)

# def show_messages(messages , sent_message):
#
#     for message in messages:
#         print(f"showing message:{message}")
#     for sent_messages in sent_message:
#         print(f"showing sent message:{sent_messages}")
#
#
# def send_messages(messages, sent_message):
#     while messages:
#         current_message = messages.pop()
#         sent_message.append(current_message)
#
# messages = ['lol', 'wyd', 'ttly', 'omw']
# sent_message = []
# send_messages(messages[:], sent_message)
# show_messages(messages, sent_message)
#
# def get_sandwiches(*sandwiches):
#     print("making the following sandwiches: ")
#     for sandwich in sandwiches:
#         print(f"-{sandwich}")
#
#
# get_sandwiches('ham sandwich', 'green sandwich', 'turkey sandwich')
#
# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)
#
# def make_car(manufacturer, model, **car_info):
#     car_info['manufacturer'] = manufacturer
#     car_info['model'] = model
#     return car_info
#
#
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)


