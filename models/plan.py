from LLM.llm_api import LLMAPI
from LLM.prompt.step_prompt import generate_step_prompt


class PlanModel:
    def __init__(self):
        self.llm_api = LLMAPI()

    def plan(self, objects, relations):
        # 生成探索过程中每一步的prompt
        prompt = generate_step_prompt(objects, relations)

        # 调用LLM API获取动作序列
        response = self.llm_api.call(prompt)

        # 解析LLM响应，提取动作序列
        actions = self._parse_response(response)

        return actions

    def _parse_response(self, response):
        # TODO: 实现解析LLM响应的逻辑，提取动作序列
        pass
