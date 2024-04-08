# 3D Object Exploration

This repository contains the code and pipeline for generating scene graphs from simulated environments using multi-view observations and GPT-4.

## Overview

The project aims to construct a scene graph that represents objects and their interrelations within a simulated environment. The pipeline processes multi-view RGB images from the simulation, utilizes GPT-4 to identify objects and their relationships, and suggests actions to reveal unseen objects.

## Pipeline

1. **Observation Collection**: Convert multi-view observations from the simulation environment into RGB images.
2. **GPT-4 Processing**: Feed the images and prompts into GPT-4V to obtain objects, their relationships, and suggested actions.
3. **Action Execution**: Determine if GPT-4 suggests new actions. If so, execute these actions to gather new observations. If not, conclude the exploration.
4. **Scene Graph Update**: Update the scene graph with new data after executing actions and obtaining new observations.
5. **Evaluation**: Compare the generated scene graph against the ground truth data using the defined metrics.

## Evaluation Metrics

The success of the scene graph generation will be evaluated based on the following metrics:

- **Object Num**: The count of distinct objects identified (vertices in the scene graph).
- **Relation**: The number of relationships between objects (edges in the scene graph).
- **Action Num**: The number of actions taken to fully explore the scene and uncover all objects and their relations.

## Dataset

The dataset consists of environments and actions that we have created, featuring 5-10 different scenes. This dataset is used to train and evaluate our model.

## Usage

Instructions on how to set up the environment, run the pipeline, and evaluate the results will be provided in this section.

## Contributing

We welcome contributions to this project. Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- Thanks to the team that developed GPT-4 for providing the tools necessary for this project.
- Appreciation goes to all contributors who have invested time in improving the scene graph generation pipeline.
