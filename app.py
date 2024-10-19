import streamlit as st
from main import predict_profanity, censor_text

def main():
    st.set_page_config(page_title="ProfanityAPI - Fast & Free Profanity Filter", page_icon="🚫", layout="wide")

    # Custom CSS
    st.markdown("""
    <style>
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        font-size: 16px;
    }
    .stButton > button {
        font-size: 18px;
        font-weight: bold;
        padding: 10px 20px;
    }
    .result-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("🚫 ProfanityAPI - Fast & Free Profanity Filter")
    st.write("Detecting toxic content has never been easier. Try our fast, free, and open-source profanity filter for your web apps.")

    # Key features
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("✅ **Much faster and cheaper** than AI")
    with col2:
        st.markdown("🎯 **Pretty accurate**")
    with col3:
        st.markdown("🆓 **100% free & open-source**")

    st.markdown("---")

    # Main content
    st.subheader("Try it out!")
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
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.subheader("Original Text:")
                st.write(user_input)
                st.markdown("</div>", unsafe_allow_html=True)
            with col2:
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                st.subheader("Censored Text:")
                st.write(censored_output)
                st.markdown("</div>", unsafe_allow_html=True)

            # Visual representation of profanity score
            st.subheader("Profanity Score Meter:")
            st.progress(profanity_score)
            if profanity_score > 0.7:
                st.error("⚠️ High profanity detected!")
            elif profanity_score > 0.3:
                st.warning("⚠️ Moderate profanity detected.")
            else:
                st.success("✅ Low profanity detected.")
        else:
            st.warning("Please enter some text to check.")

    st.markdown("---")

    # Why use ProfanityAPI
    st.subheader("Why use ProfanityAPI?")
    st.write("Moderating profanity is a thankless job. If you run a web app with any kind of user-generated content, it's your responsibility to keep things in order.")
    
    st.write("Profanity on your website:")
    st.markdown("- **Scares away new visitors**: Imagine your ideal customer waddling through a minefield of four-letter words to find your amazing product. Not exactly a recipe for conversion, is it?")
    st.markdown("- **Makes you look bad**: Your sweet grandma wants to see what her sunshine is doing on the internet and stumbles upon your website. Do you really need her to put on a hazmat suit first?")

    st.subheader("There's a better way")
    st.write("Let ProfanityAPI do the dirty work of keeping your user input clean.")

    API usage example
    st.subheader("How to use the API")
    st.code("""
const res = await fetch('https://ml-profanity-detector.onrender.com/check_profanity', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ message }),
})
    """, language="javascript")

    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #888;'>Made with ❤️ in Bennett | © Anvesh Mishra | <a href='https://github.com/mr-anvesh/ML_Profanity_Detector' target='_blank'>Star on GitHub</a></p>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
