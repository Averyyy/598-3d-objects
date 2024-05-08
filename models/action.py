# models/action.py

import os
import json
from sklearn.metrics.pairwise import cosine_similarity
from utils.embedding_utils import get_embedding
from utils.image_utils import load_images
import re


class ActionModel:
    def __init__(self, llm_api):
        self.llm_api = llm_api
        self.embeddings = self.load_or_generate_embeddings()

    def execute_action(self, action, relations):
        # Find the matching state folder based on the action
        state_folder = self.find_matching_state_folder(action)

        if state_folder:
            # Load the images from the state folder
            state_images = load_images(state_folder)

            # Generate the step prompt based on the action and state images
            prompt = self.llm_api.generate_step_prompt(action, state_images)

            # Send the prompt to the LLM API for processing
            response = self.llm_api.send_request(prompt, state_images)

            # Parse the response to extract new relations
            new_relations = self.parse_response(response)

            # Append the new relations to the existing relations list
            relations.extend(new_relations)

            # Check if the action indicates no further action required
            if self.is_no_further_action_required(response):
                return None

            return state_folder
        else:
            return None

    def load_or_generate_embeddings(self):
        embeddings = {}
        data_path = "data"

        # Iterate over each folder in the data directory
        for folder_name in os.listdir(data_path):
            folder_path = os.path.join(data_path, folder_name)
            if os.path.isdir(folder_path):
                embedding_path = os.path.join(folder_path, "embedding.json")
                if os.path.exists(embedding_path):
                    # Load the embedding from the cached file
                    with open(embedding_path, "r") as f:
                        embedding = json.load(f)
                else:
                    # Generate the embedding for the folder description
                    description_path = os.path.join(folder_path, "description.txt")
                    with open(description_path, "r") as f:
                        description = f.read().strip()
                    embedding = get_embedding(description)
                    # Cache the embedding
                    with open(embedding_path, "w") as f:
                        json.dump(embedding, f)
                embeddings[folder_name] = embedding

        return embeddings

    def find_matching_state_folder(self, action):
        # Generate the embedding for the action
        action_embedding = get_embedding(action)

        # Calculate the cosine similarity between the action embedding and each folder embedding
        similarities = {}
        for folder_name, folder_embedding in self.embeddings.items():
            similarity = cosine_similarity([action_embedding], [folder_embedding])[0][0]
            similarities[folder_name] = similarity

        # Find the folder with the highest similarity
        max_similarity_folder = max(similarities, key=similarities.get)

        return os.path.join("data", max_similarity_folder)

    def is_no_further_action_required(self, response):
        no_action_required_sample = "No further action required - All potential storage compartments and objects that could conceal other items have been inspected."
        similarity = cosine_similarity([get_embedding(response)], [get_embedding(no_action_required_sample)])[0][0]
        return similarity > 0.7

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
