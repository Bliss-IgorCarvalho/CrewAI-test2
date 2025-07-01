#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from fa_agents.crew import FaAgents

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def read_all_files_in_dir(directory):
    content = ''
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content += f'\n--- {file_path} ---\n'
                content += f.read() + '\n'
    return content

def run():
    """
    Run the crew.
    """
    functional_spec = read_all_files_in_dir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../inputs/functional_specification')))
    meeting_notes = read_all_files_in_dir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../inputs/meet_notes')))
    cr_examples = read_all_files_in_dir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../knowledge/samples/CRs_samples')))
    cl_examples = read_all_files_in_dir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../knowledge/samples/CL_samples')))
    inputs = {
        'functional_spec': functional_spec,
        'meeting_notes': meeting_notes,
        'cr_examples': cr_examples,
        'cl_examples': cl_examples,
        'current_year': str(datetime.now().year)
    }
    
    try:
        FaAgents().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        FaAgents().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FaAgents().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        FaAgents().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
