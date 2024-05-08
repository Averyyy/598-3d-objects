# LLM/prompt/initial_prompt.py

def generate_initial_prompt(object_list):
    prompt = f"""
Instruction: You are an assistant tasked with aiding in the construction of a complete scene graph for a tabletop environment. The objective is to identify all objects hidden from the current observation in the tabletop setting. Your role involves selecting appropriate actions or opting not to take any action based on commonsense knowledge in response to queries with current observations. Your responses will guide a robot in efficiently exploring the environment. Approach each step thoughtfully, and analyze the fundamental problem deeply, considering the potential vagueness or inaccuracy in the queries. Adhere to the provided formats in your instructions.

User: Analyze and provide your final answer for each new query object/part category, considering the given surrounding objects and observations in the tabletop scene from different viewpoints. The query object/part will be input with a list.  

Format your responses as follows: "[Analysis]: <your reasoning process>; \n\n [Relation]: <list of relation triples>(object1, object2, on/in/belong) \n\n [Action]: <list of action (base on object list)>".  Be comprehensive and avoid repeating my question.

The relation describes the relations between the objects. The objects should only be the ones in the input object list. Choose from three types of relations: 
1. On. 
2. In. 
3. Belong. All drawers should be along, in is only used for situations like placing them inside drawers and cabinets.
The items should be triples like (apple, table, on). pay attention to clearly identify how many drawers there belong to the object, and explore those that have not yet been explored.

For the action,  choose from three types of actions: 
1. Open the `{{number}}` door or drawer of the object. (if there are multiple drawers in an object, please include a locker number in your response with the column-major order, for example if we want to open the top drawer of the object, we can say open the 1st drawer of the object. and door or drawer number recount from different objects, if our desk and cabinet both have drawer, desk and cabinet both have 1st drawer）
2. Pick up a "special object", special object means the object block further exploration
(a.An object big enough to hide or cover something under, just like a cloth or cover 
 b. An object prevents me from opening doors and drawers )
3. No action.

Remember to give you action once at a time. Sample output: "[Analysis]: I will open the 1st drawer of the desk. The drawer is likely to contain hidden objects. \n\n [Relation]: (drawer1, desk, on) \n\n [Action]: Open the 1st drawer of the desk."

The primary goal is to select an action that has the potential to reveal hidden objects. The secondary goal is to act efficiently, performing only necessary actions to uncover hidden objects. 

object list: {', '.join(object_list)}
"""
    return prompt.strip()
