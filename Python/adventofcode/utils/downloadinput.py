if __name__ == "__main__":
    import sys
    import requests
    import datetime
    import os

    aoc_midnight = (datetime.datetime.utcnow() + datetime.timedelta(hours=-5))

    if len(sys.argv) == 1:
        year = aoc_midnight.year
        day = aoc_midnight.day
    elif len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]

    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
                     cookies={"session": os.environ["AOC_SESSION"]})

    filename = f"../aoc{year}/input{day}.txt"
    with open(filename, "w") as f:
        f.write(r.text)
    print("Wrote ", filename)
