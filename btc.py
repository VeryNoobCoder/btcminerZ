import random
import time

# ASCII Art Font
def display_ascii_art():
    print("""
  ____ _______ _____ __  __ _____ _   _ ______ _____  
 |  _ \__   __/ ____|  \/  |_   _| \ | |  ____|  __ \ 
 | |_) | | | | |    | \  / | | | |  \| | |__  | |__) |
 |  _ <  | | | |    | |\/| | | | | . ` |  __| |  _  / 
 | |_) | | | | |____| |  | |_| |_| |\  | |____| | \ \ 
 |____/  |_|  \_____|_|  |_|_____|_| \_|______|_|  \_\

                                                      ~Created by @tjm.builds on IG and Snapchat
   """)

# Function to generate a random line of characters
def generate_random_line(length=60):
    """Generate a random string of lowercase letters and numbers."""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

# Dictionary of words for the seed phrase
seed_words = {
    "robot", "tree", "unicorn", "water", "elephant", "cactus", "mountain", "guitar",
    "alligator", "camera", "pencil", "marker", "dinosaur", "telephone", "mouse", 
    "computer", "rocket", "spaceship", "galaxy", "river", "forest", "tiger", "piano"
}

# Function to generate a random wallet address
def generate_wallet_address(length=42):
    """Generate a random wallet address consisting of lowercase letters and numbers."""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(chars) for _ in range(length))

# Function to generate a random seed phrase with unique words
def generate_seed_phrase():
    """Generate a random seed phrase with 12 unique words."""
    seed_words_list = list(seed_words)  # Convert the set to a list
    return ' '.join(random.sample(seed_words_list, 12))

# Function to simulate the Bitcoin mining process
def simulate_bitcoin_miner():
    # Display the ASCII art
    display_ascii_art()
    
    # Ask the user for their Bitcoin wallet address
    wallet = input("Enter your Bitcoin Wallet: ")
    print("Starting Bitcoin miner...\n")
    time.sleep(2)  # Simulate a brief pause

    while True:
        # Determine random stopping point between 2000 and 4000 lines
        max_lines = random.randint(2000, 4000)
        print(f"Mining in progress... (Will stop after {max_lines} attempts)\n")

        # Generate and display random lines of "code"
        used_seed_words = set()  # To track used words for seed phrases
        for i in range(max_lines):
            if i % 2 == 0:
                # Display random wallet address
                print(f"Attempting to crack wallet address: {generate_wallet_address()}")
            else:
                # Display random seed phrase
                while True:
                    phrase = generate_seed_phrase()
                    # Check if the seed phrase has unique words (no repetitions)
                    phrase_words = set(phrase.split())
                    if phrase_words not in used_seed_words:
                        used_seed_words.add(frozenset(phrase_words))  # Save the phrase as used
                        print(f"Attempting to crack seed phrase: {phrase}")
                        break
            time.sleep(0.01)  # Slight delay for realism

        # Randomly select a BTC amount between 0.3 and 1.4
        btc_amount = round(random.uniform(0.3, 1.4), 2)

        # Display success message in orange color (terminal color code)
        print("\n\033[38;5;214mWallet address and seed phrase matched. Wallet cracked. "
              f"{btc_amount} BTC has been deposited to your wallet address.\033[0m")
        print(f"Wallet: {wallet}\n")

        # Ask the user if they want to continue
        choice = input("Do you want to continue mining? (Y/N): ").strip().upper()
        if choice == 'N':
            print("Mining session ended. Goodbye!")
            break
        elif choice != 'Y':
            print("Invalid input. Please enter 'Y' to continue or 'N' to stop.")

# Start the simulation
if __name__ == "__main__":
    simulate_bitcoin_miner()
