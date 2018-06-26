import random

# a list of playlists I have on Amazon Music. This list will be updated as more playlists are added.
playlists = [
			"Kiera's Grandmaster Billy Joel Playlist for Instant Life Improvement",
			"The Definite Essential Mainstream Music of Billy Joel",
			"The Essential and Most Genius David Bowie, Culled by Me, Kiera Kiera Allen",
			"Tormey Tunes",
			"Love Beatles",
			"Oakland Coffee",
			"Green Day and more",
			"Other"
			]

# a list of "other" music.
other = [
		# amalgamation playlists
		"Artistic Amalgamation",
		"Davie Mercury",
		# specific artists
		"Green Day",
		"The Beatles",
		"Imagine Dragons",
		"Billy Joel",
		# all songs
		"Arjun Plays"
		]

playlist_choice = random.choice(playlists)


print("\nToday you will be listening to: " + playlist_choice)

if playlist_choice == "Other":
	other_choice = random.choice(other)
	print("Among the other choices, you will be shuffling through: " + other_choice)

print("Enjoy your listening!")

# Next line included in order to not close the program directly
# in case playlist.py is directly opened with Python 
# instead of through the command line.
input()
