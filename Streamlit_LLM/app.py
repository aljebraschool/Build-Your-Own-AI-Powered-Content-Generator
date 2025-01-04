import cohere
import streamlit as st


# Set up Cohere client
co = cohere.ClientV2(st.secrets["COHERE_API_KEY"]) 



def generate_writeup(write_up_type, topic, tone, length, temperature):
    prompt = f"""
    
        Generate a {write_up_type} about {topic}. Follow these guidelines. 

        - Length : {length} words
        - Tone : {tone}
        - Format : Properly structured with paragraphs. Ensure the content is engaging and informative. Avoid unnecessary commentary or fillers
        - Include : clear introduction, body and conclusion

        Use these structures for different content types:

        Blog Post:
        - Engaging hook
        - Personal perspective
        - Actionable insights
        - Conversational style
        - Clear takeaways

        Article:
        - Formal introduction
        - Well-researched points
        - Expert analysis
        - Professional tone
        - Citations where relevant

        Technical Guide:
        - Step-by-step instructions
        - Code examples if relevant
        - Technical specifications
        - Practical implementation
        - Troubleshooting tips

        Social Media Post:
        - Attention-grabbing opener
        - Concise message
        - Engaging call-to-action
        - Relevant hashtags
        - Shareable format

    Now write a {write_up_type} about {topic}:
       """
    
    response = co.chat(
        messages = [{"role": "user", "content": prompt}],
        model="command-r-plus-08-2024",
        temperature = temperature
    )
    

    return response.message.content[0].text


def generate_title(content, content_type, temperature):
    prompt = f"""
            Generate an engaging title for this {content_type}. The title should be :

            - Attention-grabbing
            - Relevant to the content
            - SEO-friendly
            - Under 60 characters
            - No clickbait

            content: {content[:500]}

            Title : 

            """
    response = co.chat(
        messages = [{'role': "user", "content": prompt}],
        model="command-r-plus-08-2024",
        temperature = temperature
    )
    

    return response.message.content[0].text
    


#frontend code
st.write("📝 Professional Write-up Generator")

form = st.form(key="user_settings")

# Move these variables to be accessible outside the form
content = ""
title = ""

with form:
    # Content type selection
    content_type = st.selectbox(
        "Content Type",
        ["Blog Post", "Article", "Technical Guide", "Social Media Post"],
        key = "content_type"
    )

    # Topic input
    st.write("Enter your topic")
    topic_input = st.text_input("Topic", key="topic_input")

     # Create three columns for additional settings
    col_1, col_2, col_3 = st.columns(3)

    with col_1:
        # Tone selection
        tone = st.select_slider(
            "Tone",
            options = ["formal", "Professional", "Neutral", "causal", "conversational"],
            value = "Professional",
            key = "tone_input"
        )
    with col_2:
        # Length selection
        lenght = st.select_slider(
        "Length (words)",
        options=[300, 500, 750, 1000, 1500, 2000],
        value = 500,
        key = "input_length"
        )
    with col_3:
        # Creativity level
        creativity = st.slider(
            "Creativity",
            min_value = 0.1,
            max_value = 0.9,
            value = 0.5, 
            key = "creativity_input",
            help="Lower values for more focused content, higher for more creative"
        )

    generate_button = form.form_submit_button("Generate Content")

    if generate_button:
        if topic_input == "":
            st.error("Topic field cannot be blank")
        
        else:
            st.spinner("Generating your content...")
            # Generate content
            content = generate_writeup(content_type, topic_input, tone, lenght, creativity)
            title = generate_title(content, content_type, creativity)


            # Display results
            st.markdown("""---""")
            # st.markdown(f"## {title}")
            st.markdown(content)
                
    # Move download button outside the form
if content:  # Only show download button if content has been generated
    st.download_button(
        label="Download as Text",
        data=f"{title}\n\n{content}",
        file_name=f"{content_type.lower().replace(' ', '_')}.txt",
        mime="text/plain"
    )