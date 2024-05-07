from crew import CustomCrew

if __name__ == "__main__":
    print("## Welcome to Writer AI")
    print("-------------------------------")
    storyline = "A young prince explores and expands the outer galaxies to become the greatest king. but is this what he really wanted?"

    custom_crew = CustomCrew(storyline=storyline)
    result = custom_crew.run()
    print("-------------------------------")
    print(result)
    if result:
        with open("output.txt", "w") as f:
            f.write(result)

