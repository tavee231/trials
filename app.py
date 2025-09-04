import random
import streamlit as st

def play_game():
    if 'credits' not in st.session_state:
        st.session_state.credits = 1000
    if 'game_active' not in st.session_state:
        st.session_state.game_active = True
    if 'message' not in st.session_state:
        st.session_state.message = ""
    if 'comp_color' not in st.session_state:
        st.session_state.comp_color = ""
    if 'guess' not in st.session_state:
        st.session_state.guess = ""
    if 'wager' not in st.session_state:
        st.session_state.wager = 0

    st.title("Gcash Kulay Sugal Game")

    st.write(f"Gcash Money mo: {st.session_state.credits}")

    if not st.session_state.game_active:
        st.write(f"Talo kana ya! Ito na pera MO!: {st.session_state.credits}. Salamat sa Paglalaro!")
        if st.button("Maglaro Muli"):
            st.session_state.credits = 1000
            st.session_state.game_active = True
            st.session_state.message = ""
            st.session_state.comp_color = ""
            st.session_state.guess = ""
            st.session_state.wager = 0
        return

    # Input wager
    wager = st.number_input(
        "Magkano tataya mo pang-sugal Ya?:",
        min_value=1,
        max_value=st.session_state.credits,
        step=1,
        value=1,
        key="wager_input"
    )

    # Input color guess
    guess = st.selectbox(
        "Pili ka ng Kulay (RED, BLUE, WHITE):",
        options=['RED', 'BLUE', 'WHITE'],
        index=0,
        key="color_guess"
    )

    if st.button("Taya!"):
        st.session_state.wager = wager
        st.session_state.guess = guess
        colors = ['RED', 'BLUE', 'WHITE']
        comp_color = random.choice(colors)
        st.session_state.comp_color = comp_color

        st.write(f"Computer chose: {comp_color}")

        if guess == comp_color:
            st.session_state.credits += wager
            st.session_state.message = "NANALO KA!"
        else:
            st.session_state.credits -= wager
            st.session_state.message = "WHAHAHAHAHA TALO!"

        if st.session_state.credits <= 0:
            st.session_state.message += "\nUbos na lahat ng Pera Mo ya! tapos na ang laro."
            st.session_state.game_active = False

    if st.session_state.message:
        st.write(st.session_state.message)

    if st.session_state.game_active:
        continue_game = st.radio(
            "Gusto Mo Pa Bang Maglaro?",
            options=['Y', 'N'],
            index=0,
            key="continue_game"
        )
        if continue_game == 'N':
            st.session_state.game_active = False
            st.write(f"Talo kana ya! Ito na pera MO!: {st.session_state.credits}. Salamat sa Paglalaro!")

if __name__ == "__main__":
    play_game()