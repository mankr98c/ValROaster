import random

insults = [
    "Your aim is so inconsistent, even your crosshair has trust issues.",
    "You bought a Guardian on full buy. You are the danger.",
    "Your smokes delay the enemy… and your team.",
    "If ‘panic spray’ was a rank, you’d be Radiant.",
    "Your flank timing is so bad it might be strategic—it's not.",
    "Why do you play Jett like she's Sage with asthma?",
    "You main Reyna but have the entry confidence of a scared intern.",
    "Your Sage walls give the enemy more mobility than your team.",
    "You planted for long. On B site. On Split.",
    "Your ult usage is so bad Brimstone called in an airstrike on you.",
    "You dry peek like you're allergic to flashes—and life.",
    "Your map awareness is so bad, I'm convinced you're blindfolded.",
    "Your KDA is sponsored by pity revives.",
    "Your post-plant lineup was so early, I thought it was a pregame ritual.",
    "You're the only Yoru who gets outplayed by his own clone.",
    "You're not lurking. You're lost.",
    "I've seen AFKs with more impact than your Chamber.",
    "Your Omen smokes are like horoscopes—vague and unhelpful.",
    "You think you’re clutching. You're just wasting time.",
    "That was the most passive Raze ult I’ve ever seen. Did you try to high-five them?",
    "You bought an Ares in overtime. Are you okay?",
    "You can’t top frag but somehow still top flame.",
    "You're the only KAY/O who ults and still gets silenced emotionally.",
    "You blind more teammates than enemies. Consider glasses.",
    "I analyzed your match history. It’s just therapy with bullets.",
    "Your Spike carries you. Literally. It’s the only useful thing you touch.",
    "You play Astra like a controller with commitment issues.",
    "Your movement is so predictable I pre-fired you in another game.",
    "Your comms are great. Too bad your aim was coded in Python.",
    "Your ACS is suspiciously close to your IQ."
]


def get_random_insult():
    return random.choice(insults)
