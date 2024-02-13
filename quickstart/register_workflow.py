import logging

import littlehorse
from littlehorse.config import LHConfig
from littlehorse.model.common_enums_pb2 import VariableType
from littlehorse.workflow import Workflow, WorkflowThread

from quickstart.worker import greeting

logging.basicConfig(level=logging.INFO)


# The logic for our WfSpec (worfklow) lives in this function!
def get_workflow() -> Workflow:

    def quickstart_workflow(wf: WorkflowThread) -> None:        
        # Define an input variable
        the_name = wf.add_variable("input-name", VariableType.STR).searchable()

        # Execute the 'greet' task and pass in the variable as an argument.
        wf.execute("greet", the_name)

    # Provide the name of the WfSpec and a function which has the logic.
    return Workflow("quickstart", quickstart_workflow)


def main() -> None:
    logging.info("Registering WfSpec and TaskDef")

    # Configuration loaded from environment variables
    config = LHConfig()
    wf = get_workflow()

    littlehorse.create_task_def(greeting, "greet", config)
    littlehorse.create_workflow_spec(wf, config)


if __name__ == "__main__":
    main()
