from tmdbsdk import tv

popular = tv.TV.popular()

for number, show in enumerate(popular, start=1):
  print("{num}, {name}, {pop}".format(num=number,
                                       name=show['name'],
                                       pop=show['popularity']))