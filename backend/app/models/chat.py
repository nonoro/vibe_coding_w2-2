from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    """채팅 요청 모델"""
    message: str
    user_id: Optional[str] = None


class ChatResponse(BaseModel):
    """채팅 응답 모델"""
    response: str
    status: str = "success"
    
    def process_response(self, data: str) -> str:
        """응답 처리 메서드 - 수정된 버전"""
        # 버그 수정: 올바른 타입 힌트와 구현
        return f"처리된 응답: {data}"