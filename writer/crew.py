from agents import WriterAgents
from tasks import CustomTasks
from crewai import Crew

class CustomCrew:
    def __init__(self, storyline):
        self.storyline = storyline
    
    def run(self):
        agents = WriterAgents()
        tasks = CustomTasks()

        manager = agents.manager()
        novel_writer_1 = agents.novel_writer()
        chapter_writer_1 = agents.chapter_writer()
        chapter_writer_2 = agents.chapter_writer()

        manage = tasks.orchestrate(manager)
        write_novel = tasks.write_shallow(novel_writer_1, self.storyline)
        write_chapter_1 = tasks.write_chapter(chapter_writer_1)
        write_chapter_2 = tasks.write_chapter(chapter_writer_2)

        crew = Crew(
            agents=[manager, novel_writer_1, chapter_writer_1, chapter_writer_2],
            tasks=[manage, write_novel, write_chapter_1, write_chapter_2],
            verbose=True,
        )

        return crew.kickoff()


