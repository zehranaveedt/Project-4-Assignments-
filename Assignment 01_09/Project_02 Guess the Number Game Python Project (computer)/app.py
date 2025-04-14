import streamlit as st
import random

    
st.title("🎮 Guess the Number Game!")
st.write("Think you can crack the secret number? Try your luck!🧠😃")
st.write("Think of a number between 1 and 100 and test your guessing skills! 🎯")
st.write("🔹 You have 6 attempts to find the secret number.")

st.session_state.secret_number = 47

if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)


if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 6

st.info(f"📌 Attempts remaining: {st.session_state.attempts_left}")


guess = st.number_input("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)


if st.button("Submit"):
    if st.session_state.attempts_left > 0:
        if guess == st.session_state.secret_number:
            st.success(f"🎉 Congratulations! You guessed the right number: {guess}")
            st.balloons()
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts_left = 6
        else:
            st.session_state.attempts_left -= 1
            difference = abs(st.session_state.secret_number - guess)

            
            if difference >= 40:
                hint = "❌ Too High" if guess > st.session_state.secret_number else "❌ Too Low"
                st.error(hint)
            elif difference >= 20:
                hint = "⚠ Medium range"
                st.warning(hint)
            elif difference >= 10:
                hint = "🟡 Very Close!"
                st.info(hint)
            else:
                hint = "🟢 Almost there!"
                st.success(hint)

            st.info(f"📌 Attempts remaining: {st.session_state.attempts_left}") 

            if st.session_state.attempts_left == 0:
                st.error(f"💥 Game Over! The correct number was {st.session_state.secret_number}")
                st.write("🔄 Try Again!")


if st.session_state.attempts_left == 0:
    if st.button("🔄 Restart Game"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts_left = 6
        st.rerun()