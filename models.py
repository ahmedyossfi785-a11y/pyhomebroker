from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    group_id = Column(String, nullable=False)
    balance = Column(Integer, default=0)
    messages_count = Column(Integer, default=0)
    is_admin = Column(Boolean, default=False)
    is_muted = Column(Boolean, default=False)
    last_daily_claim = Column(DateTime, default=None)

class GroupSettings(Base):
    __tablename__ = 'group_settings'
    id = Column(Integer, primary_key=True)
    group_id = Column(String, nullable=False, unique=True)
    welcome_status = Column(Boolean, default=True)
    welcome_message = Column(Text, default="Welcome to the group!")

class Puzzles(Base):
    __tablename__ = 'puzzles'
    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    answer = Column(String, nullable=False)
    prize_amount = Column(Integer, default=1000)

class ActiveGame(Base):
    __tablename__ = 'active_games'
    id = Column(Integer, primary_key=True)
    group_id = Column(String, nullable=False)
    game_type = Column(String, nullable=False)  # 'puzzle', 'xo', 'bet'
    state_data = Column(Text, nullable=False)  # JSON or text for game state
    active_player = Column(String, default=None)  # user_id if applicable

# Database setup
engine = create_engine('sqlite:///boruto_bot.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)