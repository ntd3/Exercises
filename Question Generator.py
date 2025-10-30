from pydantic_ai import Agent
from pydantic import BaseModel
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider

    
class Question(BaseModel):
    question: str
    choices: str
    correct_answer_character: str

class Questions(BaseModel):
    questions: list[Question]
model = GroqModel(
    'qwen/qwen3-32b', provider=GroqProvider(api_key='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')
)
agent = Agent(output_type=Questions, system_prompt=(
        "Act as an expert mcq question generator based on the topic and grade level."
    ),model=model)
print("##################################################################################################################\n Question Generator \n #####################################################################################################")
topic = input("Please Enter the topic you want questions on: ")
grade = input("Please Enter your grade level: ")


score = 0
result = agent.run_sync(f'Generate 10 questions about {topic} for someone in grade {grade}')
for q in result.output.questions:
    print(f"{q.question}\n")
    print(f"{q.choices}\n")
    ans = input("Please enter your answer in one character: ")
    if ans.lower()==q.correct_answer_character.lower():
        print("You are correct \n")
        score += 1
    else:
        print(f"Correct Answer: {q.correct_answer_character}\n")

print(f"Congratulation! You got {score}/10")