import random
import threading
import time
from models import Session, Puzzles, ActiveGame, Users
from utils import send_message, normalize_text

def start_puzzle(group_id):
    session = Session()
    # Check if there's an active game
    active = session.query(ActiveGame).filter_by(group_id=group_id).first()
    if active:
        session.close()
        return "A game is already active in this group."

    # Select random puzzle
    puzzles = session.query(Puzzles).all()
    if not puzzles:
        session.close()
        return "No puzzles available."

    puzzle = random.choice(puzzles)
    # Store active game
    active_game = ActiveGame(group_id=group_id, game_type='puzzle', state_data=str(puzzle.id))
    session.add(active_game)
    session.commit()
    session.close()

    # Send puzzle message
    message = f"🧩 Puzzle Time! 🧩\n\n{puzzle.question}\n\nPrize: {puzzle.prize_amount} coins\n\nYou have 2 minutes to answer!"
    send_message(group_id, message)

    # Start timer
    timer = threading.Timer(120, timeout_puzzle, args=[group_id, puzzle.answer])
    timer.start()

    return "Puzzle started."

def timeout_puzzle(group_id, answer):
    session = Session()
    active = session.query(ActiveGame).filter_by(group_id=group_id, game_type='puzzle').first()
    if active:
        session.delete(active)
        session.commit()
        send_message(group_id, f"⏰ Time's up! The answer was: {answer}")
    session.close()

def check_answer(group_id, user_id, message):
    session = Session()
    active = session.query(ActiveGame).filter_by(group_id=group_id, game_type='puzzle').first()
    if not active:
        session.close()
        return False

    puzzle_id = int(active.state_data)
    puzzle = session.query(Puzzles).filter_by(id=puzzle_id).first()
    if normalize_text(message) == normalize_text(puzzle.answer):
        # Win
        user = session.query(Users).filter_by(user_id=user_id, group_id=group_id).first()
        if user:
            user.balance += puzzle.prize_amount
            session.commit()
        session.delete(active)
        session.commit()
        send_message(group_id, f"🎉 Congratulations {user_id}! You won {puzzle.prize_amount} coins. Answer: {puzzle.answer}")
        session.close()
        return True
    session.close()
    return False

def handle_bet(group_id, user_id, color, amount):
    session = Session()
    user = session.query(Users).filter_by(user_id=user_id, group_id=group_id).first()
    if not user or user.balance < amount:
        session.close()
        return "Insufficient balance."

    user.balance -= amount
    session.commit()
    session.close()

    # Simulate bet result (random)
    winner_color = random.choice(['red', 'blue'])
    if color.lower() == winner_color:
        prize = amount * 2  # Double the bet
        user.balance += prize
        session = Session()
        session.commit()
        session.close()
        send_message(group_id, f"🎉 {user_id} won the bet! Prize: {prize} coins. Winner color: {winner_color}")
    else:
        send_message(group_id, f"😢 {user_id} lost the bet. Winner color: {winner_color}")

    return "Bet placed."