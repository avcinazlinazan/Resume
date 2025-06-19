from pydantic import BaseModel, Field
from typing import List, Optional

class Experience(BaseModel):
    company: str = Field(..., description="Çalışılan şirketin adı")
    summary: str = Field(..., description="Şirkette yapılan işlerin özeti")

class ResumeStructured(BaseModel):
    title: Optional[str] = Field(None, description="Kişinin mesleki ünvanı")
    summary: Optional[str] = Field(None, description="Kısa özgeçmiş özeti")
    experiences: List[Experience] = Field(default_factory=list, description="Çalışılan şirketler ve özetleri")
    skills: List[str] = Field(default_factory=list, description="Teknik beceriler")
    soft_skills: List[str] = Field(default_factory=list, description="Kişisel beceriler")
    certificates: List[str] = Field(default_factory=list, description="Sertifikalar")
    languages: List[str] = Field(default_factory=list, description="Konuşulan diller")