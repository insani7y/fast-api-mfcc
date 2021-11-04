from typing import List

from pydantic import BaseModel


class MFCCResponse(BaseModel):
    mfcc: List[List[float]]
