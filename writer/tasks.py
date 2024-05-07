from crewai import Task
from textwrap import dedent
import random
import string

class CustomTasks:
    def __init__(self):
        self.__tip_section = "If you do your BEST WORK, I'll give you a $10,000 commission!"

    # TODO modify so that in the output the chapters are also generated
    def write_shallow(self, agent, storyline):
        return Task(
            description=dedent(
                f"""
                Based on the storyline: {storyline},
                write a novel, divide it into chapters, and add all the chapters into a list for the other writers for reference.
                """
            ),
            agent=agent,
            output_file="summary.txt",
            expected_output=dedent(
                """
                Novel has been successfully written. Chapters have been divided and added to the summary file.
                """
            )
        )

    
    def orchestrate(self, agent):
        return Task(
            description=dedent(
                f"""
                Oversee the process of writing chapters.
                If there is a chapter in the list, assign it to a writing agent and ensure the work gets done.
                Do this until there are no chapters left.
                {self.__tip_section}
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                All chapters have been successfully written.
                """
            )
        )
    
    def generate_chapter_name(self):
        # Generate a random chapter name using letters and digits
        chapter_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return "Chapter_" + chapter_name
    
    def write_chapter(self, agent):
        chapter_name = self.generate_chapter_name()
        return Task(
            description=dedent(
                f"""
                Take a chapter from the list generated in Task 1 and expand it briefly using sophisticated language.
                {self.__tip_section}
                Once done, remove the chapter from the list so that other writers can write the rest of them.
                """
            ),
            agent=agent,
            output_file=f"{chapter_name}.md",
            expected_output=dedent(
                f"""
                Chapter '{chapter_name}' has been successfully written.
                """
            )
        )

