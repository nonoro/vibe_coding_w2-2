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
    
    # 의도적 버그: 잘못된 타입 힌트
    def process_response(self, data: int) -> str:  # data는 실제로 str이어야 함
        """응답 처리 메서드 - 버그 포함"""
        # 버그: str을 int로 처리하려고 시도
        return data + 100  # TypeError 발생 예정