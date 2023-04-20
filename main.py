from avatar import Avatar
from scenes import Intro

# Start game introduction sequence
Intro().play()

# Initialize avatar and start avatar creator
avatar = Avatar()
avatar.create()

# Run your main story based script here