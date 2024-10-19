import streamlit as st
from main import predict_profanity, censor_text

def main():
    st.set_page_config(page_title="AI-Powered Profanity Filter", page_icon="🚫")

    st.title("AI-Powered Profanity Filter")
    st.write("Enter your text below to check for profanity and censor it if necessary.")

    user_input = st.text_area("Enter your text:", height=150)

    if st.button("Check and Censor"):
        if user_input:
            profanity_score = predict_profanity(user_input)
            censored_output = censor_text(user_input)

            st.subheader("Results:")
            st.write(f"Profanity score: {profanity_score:.2f}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Text:")
                st.write(user_input)
            with col2:
                st.subheader("Censored Text:")
                st.write(censored_output)

            # Visual representation of profanity score
            st.subheader("Profanity Score Meter:")
            st.progress(profanity_score)
            if profanity_score > 0.7:
                st.error("High profanity detected!")
            elif profanity_score > 0.3:
                st.warning("Moderate profanity detected.")
            else:
                st.success("Low profanity detected.")
        else:
            st.warning("Please enter some text to check.")

if __name__ == "__main__":
    main()
