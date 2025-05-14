from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey , Float
from sqlalchemy.orm import declarative_base, relationship
from database import Base

class Employee(Base):
    __tablename__ = "employee"

    employeeID = Column(String(255), primary_key=True, index=True)
    userId = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    DOP = Column(String(255), nullable=False)
    phoneNumber = Column(String(20), nullable=False)
    profileImage = Column(String(255), nullable=True)
    coverImage = Column(String(255), nullable=True)
    gender = Column(String(10), nullable=False)
    address = Column(String(500), nullable=False)
    description = Column(Text, nullable=True)
    jobTitle = Column(String(255), nullable=False)
    cv = Column(String(255), nullable=True)

    # job_applications = relationship("JobApplicant", back_populates="employees")

class JobApplicant(Base):
    __tablename__ = "jobs_applicants"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employeeID = Column(String, ForeignKey("employees.employeeID"), nullable=False)
    employerID = Column(String, nullable=False)
    jobID = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(50), nullable=False)
    score = Column(Float, nullable=True)

    # employees = relationship("Employee", back_populates="job_applications")