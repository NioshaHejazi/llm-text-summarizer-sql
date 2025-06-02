from app.summarizer import summarize

text = """
The Apollo program was the third United States human spaceflight program carried out by NASA, which accomplished landing the first humans on the Moon from 1969 to 1972. First conceived during Dwight D. Eisenhower's administration, Apollo began in earnest after President John F. Kennedy's May 25, 1961 address to Congress, in which he declared "I believe that this nation should commit itself to achieving the goal, before this decade is out, of landing a man on the Moon and returning him safely to the Earth."
"""

summary = summarize(text)
print("Summary:\n", summary)
