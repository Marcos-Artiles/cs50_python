#main function that contais the guest list
def main():
  names = ["Mario", "Luigi", "Daisy", "Yoshi"]

  for name in names:
    print(write_letter(name, "Princess Peach"))

#function that recives the guests and the sender to print the letters
def write_letter(receiver, sender):
  return f"""
    +----------------------------------------+
      Dear {receiver},

      You are cordially invited to a ball at
      Peach's Castle this evening, 7:00 PM.

      Sincerely,
      {sender}
    +----------------------------------------+
    """

main()