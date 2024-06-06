from typing import Literal

from pydantic import BaseModel, Field


class InputModel(BaseModel):
    language: Literal[
        'English',
        'Korean',
    ] = Field(
        default='Korean',
    )
    llm_type: Literal['chatgpt', 'huggingface'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    output: str = Field(
        description='Expected Questions',
    )
