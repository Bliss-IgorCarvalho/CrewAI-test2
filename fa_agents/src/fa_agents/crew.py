from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, tool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from fa_agents.tools.requirements_tools import (
    FunctionalSpecReaderTool,
    MeetingNotesReaderTool,
    ChangeRequestWriterTool,
    ChangelogWriterTool
)
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FaAgents():
    """FaAgents crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def requirements_analyst_1(self) -> Agent:
        return Agent(
            config=self.agents_config['requirements_analyst_1'], 
            verbose=True
        )

    @agent
    def requirements_analyst_2(self) -> Agent:
        return Agent(
            config=self.agents_config['requirements_analyst_2'], 
            verbose=True
        )

    @task
    def generate_change_requests(self) -> Task:
        return Task(
            config=self.tasks_config['generate_change_requests'], 
        )

    @task
    def update_spec_and_changelog(self) -> Task:
        return Task(
            config=self.tasks_config['update_spec_and_changelog'], 
        )

    @tool
    def functional_spec_reader(self):
        return FunctionalSpecReaderTool()

    @tool
    def meeting_notes_reader(self):
        return MeetingNotesReaderTool()

    @tool
    def change_request_writer(self):
        return ChangeRequestWriterTool()

    @tool
    def changelog_writer(self):
        return ChangelogWriterTool()

    @crew
    def crew(self) -> Crew:
        """Creates the FaAgents crew"""
        tools = {
            'functional_spec_reader': FunctionalSpecReaderTool,
            'meeting_notes_reader': MeetingNotesReaderTool,
            'change_request_writer': ChangeRequestWriterTool,
            'changelog_writer': ChangelogWriterTool,
        }
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            tools=tools,
            process=Process.sequential,
            verbose=True,
        )
