# models/perception.py

import re


class PerceptionModel:
    def __init__(self, llm_api):
        self.llm_api = llm_api

    def perceive_and_plan(self, images):
        prompt = self.llm_api.generate_initial_prompt(images)
        response = self.llm_api.send_request(prompt, images)

        relations, actions = self.parse_response(response)

        return relations, actions

    def next_actions(self, action, images):
        prompt = self.llm_api.generate_step_prompt(action, images)
        response = self.llm_api.send_request(prompt, images)

        relations, actions = self.parse_response(response)

        return relations, actions

    def parse_response(self, response):
        relation_pattern = r"\[Relation\]:\s*(.*?)\s*\[Action\]"
        action_pattern = r"\[Action\]:\s*(.*)"

        relation_match = re.search(relation_pattern, response, re.DOTALL)
        action_match = re.search(action_pattern, response)

        relations = []
        actions = []

        if relation_match:
            relation_text = relation_match.group(1).strip()
            relation_lines = relation_text.split("\n")
            for line in relation_lines:
                line = line.strip()
                if line:
                    relation = tuple(part.strip() for part in line.strip("()").split(", "))
                    relations.append(relation)

        if action_match:
            action_text = action_match.group(1).strip()
            actions = [action.strip() for action in action_text.split(".") if action.strip()]

        return relations, actions

    def test_parse_response(self):
        example_response = '''[Analysis]: From the provided images of the tabletop environment, it appears that the main visible objects are a desk with multiple drawers, possibly with items either inside or behind it, which are not currently visible. Both images show a desk from different perspectives. The first image shows an open drawer which provides a clue that there might be additional unopened drawers with potentially hidden items inside. In the second image, which provides a wider view, additional unopened drawers can be seen. A table lamp is visible and does not appear to block access to any drawers but rather serves as an object on the tabletop. The presence of these drawers invites exploration to determine what they contain.

[Relation]:
(drawer1, desk, on)
(drawer2, desk, on)
(table lamp, desk, on)

[Action]:
Open the 3rd drawer of the desk. (drawer numbering reassessed based on provided image showing multiple drawers where not all are open.)'''

        relations, actions = self.parse_response(example_response)

        print("Relations:")
        for relation in relations:
            print(relation)

        print("\nActions:")
        for action in actions:
            print(action)


if __name__ == "__main__":
    perception_model = PerceptionModel(None)
    perception_model.test_parse_response()
