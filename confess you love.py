import pyautogui as auto
import time
time.sleep(3)

lover_synonyms_extended = [
    "Admirer", "Beau", "Beloved","Girlfriend", 
    "Companion", "Crush", "Darling", "Date", "Devotee", 
    "Flame", "Heartthrob", "Inamorata", "Inamorato", "Paramour", 
    "Partner", "Significant other", "Soulmate", "Sweetheart", 
    "Swain", "Worshipper", "Fiancé(e)", "Amour", "Beloved one", 
    "Better half", "Charming one", "Confidant", "Consort", "Dear", 
    "Dearest", "Heart's desire", "Honey", "Lovebird", "Mate", 
    "Muse", "Partner in crime", "Precious", "Romeo/Juliet", 
    "Snuggle buddy", "Steady", "Suitor", "True love", "Valentine", 
    "Wooer", "Yoke-mate", "Heartbreaker", "Squeeze", "My other half", 
    "Constant", "Treasure", "Cherished one", "Beloved partner"
]
while True:
    for item in lover_synonyms_extended:
        auto.typewrite('you are my ')
        auto.typewrite(item)
        auto.press('enter')