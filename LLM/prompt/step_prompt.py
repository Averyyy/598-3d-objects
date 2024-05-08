# LLM/prompt/step_prompt.py

def generate_step_prompt(completed_actions, new_image_paths):
    prompt = f"""
Previously, we have completed the following actions: {completed_actions}. Note that when we perform a certain action, we will restore the operation, for instance, when we perform an 'open the drawer' action, we will then close it. 

After the current action {completed_actions[-1]}, the environment will change to the new state shown in the picture. You might observe some new objects within it.

Please format your responses as follows: '[Completed Action]: <the action that has been taken so far, including the previous completed action and the current completed action>; \n\n[New Observation]: <the new objects observed after the action>; \n\n[Next Action]: <the next action to take for environmental exploration>.'
"""
    return prompt.strip()
