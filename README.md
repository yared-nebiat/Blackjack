# Blackjack
A command-line based implementation of the popular card game, Blackjack, written in Python.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Python 3.x should be installed on your machine. You can download the latest version from the official Python website.

## Installation
Clone the repository to your local machine using the following command:
- go to your machine's terminal
- git clone https://github.com/yared-nebiat/blackjack.git
- Navigate to the project directory:
cd blackjack
- Run the game using the following command:
python blackjack.py
- Gameplay
- The game is played with one deck of standard playing cards (52 cards). The objective is to beat the dealer by having a hand value of 21 or closest to 21 without going over (busting).

## Rules
- Ace is worth 1 or 11 points, face cards (King, Queen, Jack) are worth 10 points, and all other cards are worth their face value.
- The player starts by placing a bet and is dealt two cards. The dealer also receives two cards, one face up and one face down.
- The player can choose to hit (take another card) or stand (keep their current hand). If the player busts (goes over 21), the dealer wins.
- After the player stands, the dealer reveals their face-down card and hits or stands based on a set of rules: if the dealer has 16 or less, they must hit, and if they have 17 or more, they must stand.
- If the dealer busts, the player wins. If both the player and dealer have the same hand value, the game is a push (tie) and the player's bet is returned.
The game continues until the player decides to quit or runs out of money.

### Author
Yared Nebiat
