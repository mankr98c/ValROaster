import random

duelist_insults = [
    "You insta-lock Jett and play like Sage with stage fright.",
    "Your Reyna has the ego of Radiant and the stats of Iron.",
    "You use Raze satchels for movement... straight to the grave.",
    "You're a Phoenix main. The self-flash is part of your identity.",
    "Your Yoru teleports like he’s rage quitting in slow motion.",
    "Neon mains think they’re fast. Turns out they’re just first to die.",
    "You got first blood—on yourself.",
    "You ulted. No one asked. No one benefited.",
    "Your K/D ratio should stand for *Kills? Doubtful.*",
    "You peek like you’re legally blind and emotionally unavailable.",
]

sentinel_insults = [
    "Your KJ turret sees more action than you do.",
    "You place Cypher trips like you're trying to decorate, not defend.",
    "Sage wall. Enemy boosted. Round lost. Rinse. Repeat.",
    "You revive the bottom frag first every time. Bold choice.",
    "You're a Chamber main who forgot to shoot. Again.",
    "Your lockdown is always used post-post-plant. Revolutionary.",
    "You anchor site like you're protecting it from happiness.",
    "You play support but emotionally damage the team anyway.",
    "Your trap setup is more confusing than helpful.",
    "You're not a sentinel, you're just... there."
]

initiator_insults = [
    "You flash the team like it’s a party trick.",
    "Your Breach concussed us into next round loss.",
    "Fade ult? More like ‘muffled panic’ at this point.",
    "You silenced the enemy... and your entire team’s will to play.",
    "You shoot recon darts like you’re aiming for the moon.",
    "Skye’s dog had more map control than you.",
    "You're farming assist stats and still missing everything.",
    "You used Wingman to plant and then alt-tabbed.",
    "You're the only Sova with drone kills but no frags.",
    "You flashed, pushed, and vanished. Like your win rate."
]

controller_insults = [
    "Your smokes are late. Just like your game sense.",
    "Brim molly? Into a corner. Enemy untouched. Bravo.",
    "You placed Viper wall backwards. Artful.",
    "Astra stars placed with love, used with shame.",
    "Your Omen TP is more panic than plan.",
    "You Harbor walled your own team. Again.",
    "You smoked heaven... while they came from garage.",
    "You're holding smokes like you're scared of commitment.",
    "Your Brim stim beacon gave speed... to the enemy.",
    "You're not controlling the map, you’re decorating it."
]

def get_role_roast(role):
    role = role.lower()
    if role == "duelist":
        return random.choice(duelist_insults)
    elif role == "sentinel":
        return random.choice(sentinel_insults)
    elif role == "initiator":
        return random.choice(initiator_insults)
    elif role == "controller":
        return random.choice(controller_insults)
    else:
        return "That’s not even a real role. Are you trying to play spectator?"
