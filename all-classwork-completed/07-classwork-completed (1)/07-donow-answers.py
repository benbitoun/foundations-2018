# 1) Find all of the songs that are the first track of an album.
df[df.track_num == 1]
df[df['track_num'] == 1]

# 2) Find all of albums named "Change".

# EXACT MATCH
df[df.album == 'Change']

# 3) Find all of the songs with 'Change' in the album's name.

# Column contains the string
# but doesn't have to be exact
df[df.album.str.contains('Change')]

df[df.album.str.contains('Change', na=False)]

df[df.album.str.contains('Change') == True]

df.dropna(subset=['album'], inplace=True)
df[df.album.str.contains('Change')]

True
False
NaN -> False
False
False
True


# 4) Count the number of songs with "Auto" in their name. 

len(df[df.title.str.contains("Auto")])
df[df.title.str.contains("Auto")].shape
df.title.str.contains("Auto").value_counts()


# 5) Find all of the songs on the Strike Anywhere album Change is a Sound.

df.album == 'Change is a Sound'
df.artist == 'Strike Anywhere'


# and
df[(df.album == 'Change is a Sound') & (df.artist == 'Strike Anywhere')]

# or
df[(df.album == 'Change is a Sound') | (df.artist == 'Strike Anywhere')]

# fancy technique

is_strike_anywhere = df.artist == 'Strike Anywhere'
is_change = df.album == 'Change is a Sound'
df[is_strike_anywhere & is_change]


# 6) Find every song by Koufax that is the first track on an album.  

df[(df.track_num == 1) & (df.artist == 'Koufax')]

# 6a) Find every song that's the first track on an album and has "Auto" in the title

df[df.title.str.contains('Auto') & (df.track_num == 1)]

# 7) Find every song by Braid, Koufax, SDRE, or The Bouncing Souls.

df[df.artist.isin(['Braid', 'Koufax', 'SDRE', 'The Bouncing Souls'])]

# 8) If any band has a "The" in their name, get rid of it. For example, "The Bouncing Souls" would become just become "Bouncing Souls."

# The best way to get rid of things is to replace them with nothing
df['artist'] = df.artist.str.replace("The ", "")

# .str.replace is different than .replace
df.artist.replace("The Bouncing Souls", "Bouncing Souls", inplace=True)

# 9) Find every song that has a title like I love ____ burgers. For example, "I love hamburgers" or "I love cheeseburgers" or "I love black bean and quinoa burgers" all match.

"burgers are a thing I love"


# Order is important
df[df.title.str.contains("I love .* burgers")]

# Order is not important
df[df.title.str.contains('I love') & df.title.str.contains('burgers')]


