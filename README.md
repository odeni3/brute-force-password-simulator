# Brute Force Password Simulator

## Overview

The Brute Force Password Simulator is a simple Python application that simulates a brute force attack to guess a password entered by the user. It consists of three components:

- **Server**: Listens for incoming password requests from clients.
- **Client**: Allows the user to input a password and sends it to the server.
- **Attacker**: Simulates a brute force attack to guess the password received from the client.

## How It Works

1. Run the `server.py` script on the machine where you want to listen for password requests.
2. Run the `client.py` script on another machine and enter the password you want to test.
3. The client sends the password to the server.
4. The attacker component, running on the server machine, simulates a brute force attack to guess the password.
5. If the attacker successfully guesses the password, it is displayed.

## Usage

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `server.py` script: `python server.py`.
4. On another machine, run the `client.py` script: `python client.py`.
5. Enter the password you want to test in the client prompt.
6. Wait for the attacker to guess the password.

## Notes

- This project is for educational purposes only. Do not use it for any malicious purposes.
- Use strong, unique passwords to protect your accounts from brute force attacks.

