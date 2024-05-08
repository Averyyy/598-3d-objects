# main.py

import os
from LLM.llm_api import LLMAPI
from models.perception import PerceptionModel
from models.action import ActionModel
# from models.graph import GraphModel
from utils.image_utils import load_images


def main():
    # Set up the environment
    data_path = "data"
    llm_api = LLMAPI()
    perception_model = PerceptionModel(llm_api)
    action_model = ActionModel(llm_api)
    # graph_model = GraphModel()

    # Load images from the initial state folder (data/0)
    initial_state_folder = os.path.join(data_path, "0")
    images = load_images(initial_state_folder)

    # Perception and Plan
    relations, actions = perception_model.perceive_and_plan(images)

    # Action and Exploration
    current_state_folder = initial_state_folder
    while actions:
        action = actions.pop(0)
        new_state_folder = action_model.execute_action(action, relations)
        if new_state_folder:
            current_state_folder = new_state_folder
            new_state_images = load_images(current_state_folder)
            new_relations, next_action = perception_model.next_actions(action, new_state_images)
            if not new_relations:
                break

            relations.extend(new_relations)

            if next_action:
                actions.append(next_action)
            else:
                break
        else:
            break

    # Memory and Graph Generation
    # scene_graph = graph_model.generate_graph(relations)

    print("Scene Graph:")
    print(relations)


if __name__ == "__main__":
    main()
