import streamlit as st
import requests


def call_nebius_api(api_key, model, messages, max_tokens=1000, temperature=0.7):
    """
    Reusable function to call Nebius AI Studio API
    
    Args:
        api_key (str): Nebius AI Studio API key
        model (str): Model name to use
        messages (list): List of message dictionaries with 'role' and 'content'
        max_tokens (int): Maximum tokens to generate
        temperature (float): Temperature for response generation
    
    Returns:
        tuple: (success: bool, content: str or error_message: str)
    """
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }
        
        response = requests.post(
            "https://api.studio.nebius.ai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            return True, content
        else:
            return False, f"API Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return False, f"Error: {str(e)}"


def welcome_screen():
    st.title("🚀 AI Multi-Tool")
    st.write("Welcome to your AI-powered toolkit using Nebius AI Studio!")
    
    st.info(
        "**Get started:** Enter your Nebius AI Studio API key in the sidebar to begin using the tools.",
        icon="👈"
    )


def chatbot_interface():
    st.title("💬 AI Multi-Tool Chatbot")
    st.write(
        "This chatbot uses Nebius AI Studio API. "
    )
    
    # API configuration
    if not api_key:
        st.info("Please add your Nebius AI Studio API on the sidebar key to continue.", icon="🗝️")
        return
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                messages = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
                
                success, result = call_nebius_api(
                    api_key=api_key,
                    model=model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                
                if success:
                    st.markdown(result)
                    st.session_state.messages.append({"role": "assistant", "content": result})
                else:
                    st.error(result)


def text_checker_interface():
    st.title("📝 Text Checker")
    st.write("Fix and improve your text using AI. You can customize the instructions below.")
    
    # API configuration check
    if not api_key:
        st.info("Please add your Nebius AI Studio API key in the sidebar to continue.", icon="🗝️")
        return
    
    # Default instruction
    default_instruction = "Please fix the following text by:\n"\
        "- Correcting grammar and spelling errors\n"\
        "- Improving sentence structure and clarity\n"\
        "- Ensuring proper punctuation\n"\
        "- Making the text more readable and professional\n\n"\
        "Return only the corrected text without any comments or explanations."\

    # Instruction customization
    with st.expander("📋 Instructions", expanded=False):
        instruction = st.text_area(
            "Editing Instructions",
            value=default_instruction,
            height=200,
            help="You can customize how the AI should fix your text"
        )
    
    # Use default if not customized
    if 'instruction' not in locals():
        instruction = default_instruction
    
    # Text input
    st.subheader("📥 Input Text")
    input_text = st.text_area(
        "Enter text to check:",
        height=300,
        placeholder="Paste your text here..."
    )
    
    if st.button("🔧 Fix Text", type="primary", disabled=not input_text):
        with st.spinner("Fixing text..."):
            messages = [
                {"role": "system", "content": instruction},
                {"role": "user", "content": input_text}
            ]
            
            success, result = call_nebius_api(
                api_key=api_key,
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            if success:
                st.subheader("✅ Fixed Text")
                st.code(result, language=None)
            else:
                st.error(result)


def recipe_creator_interface():
    st.title("👨‍🍳 Recipe Creator")
    st.write("Create delicious recipes based on your ingredients and preferences!")
    
    # API configuration check
    if not api_key:
        st.info("Please add your Nebius AI Studio API key in the sidebar to continue.", icon="🗝️")
        return
    
    # Recipe creation form
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("🥕 Ingredients")
        ingredients = st.text_area(
            "Enter your available ingredients:",
            height=120,
            placeholder="e.g., chicken breast, broccoli, rice, garlic, olive oil..."
        )
    
    with col2:
        st.subheader("🍳 Cooking Method")
        cooking_methods = [
            "Any method",
            "Steamed",
            "Boiled", 
            "Fried",
            "Baked",
            "Grilled",
            "Roasted",
            "Sautéed",
            "Stir-fried",
            "Braised"
        ]
        
        cooking_method = st.selectbox(
            "Preferred cooking method:",
            cooking_methods,
            help="Choose your preferred way of cooking"
        )
        
        st.subheader("⏱️ Options")
        servings = st.number_input("Number of servings:", min_value=1, max_value=12, value=4)
        dietary_restrictions = st.text_input("Dietary restrictions:", placeholder="vegetarian, gluten-free, etc.")
    
    if st.button("🍽️ Create Recipe", type="primary", disabled=not ingredients):
        with st.spinner("Creating your recipe..."):
            # Build the recipe instruction prompt
            recipe_instruction = f"""Create a detailed recipe using the provided ingredients. Follow this exact format:

**RECIPE NAME**: [Creative name for the dish]

**INGREDIENTS** (for {servings} servings):
- [List all ingredients with precise measurements]

**COOKING TIME**: 
- Prep time: [X minutes]
- Cook time: [X minutes] 
- Total time: [X minutes]

**INSTRUCTIONS**:
1. [Step-by-step cooking instructions, numbered clearly]
2. [Each step should be clear and specific]
3. [Include cooking times and temperatures where relevant]

**COOKING NOTES**:
- [Any helpful tips or variations]
- [Storage instructions if applicable]

**NUTRITIONAL HIGHLIGHTS**:
- [Brief nutritional benefits of key ingredients]

REQUIREMENTS:
- Primary cooking method should be: {cooking_method if cooking_method != 'Any method' else 'use the most suitable method'}
- Number of servings: {servings}
- Dietary restrictions: {dietary_restrictions if dietary_restrictions else 'None'}
- Use only the provided ingredients (you may suggest common pantry items like salt, pepper, oil if needed)
- Provide exact measurements and cooking times
- Make the recipe practical and easy to follow"""

            messages = [
                {"role": "system", "content": recipe_instruction},
                {"role": "user", "content": f"Available ingredients: {ingredients}"}
            ]
            
            success, result = call_nebius_api(
                api_key=api_key,
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.3  # Lower temperature for more consistent recipe format
            )
            
            if success:
                st.subheader("📖 Your Recipe")
                st.markdown(result)
                
                # Add a copy-friendly version
                with st.expander("📋 Copy Recipe", expanded=False):
                    st.text_area("Recipe text for copying:", value=result, height=400)
            else:
                st.error(result)


# Sidebar for navigation
with st.sidebar:
    st.title("AI Multi-Tool")
    st.write("Your AI-powered toolkit")
    
    # API configuration
    api_key = st.text_input(
        "Nebius AI Studio API Key", 
        type="password",
        help="Enter your API key from Nebius AI Studio"
    )
    if not api_key:
        st.info("Please add your Nebius AI Studio API key to continue.", icon="🗝️")
        st.markdown(
            "**How to get your API key:**\n"
            "1. Visit [Nebius AI Studio API Keys](https://studio.nebius.com/settings/api-keys)\n"
            "2. Sign up or log in to your account\n"
            "3. Generate a new API key\n"
            "4. Copy and paste it above\n\n"
            "📖 [Full documentation](https://docs.nebius.com/studio/api/authentication)"
        )

    # Model selection
    model_options = {
        "meta-llama/Meta-Llama-3.1-8B-Instruct-fast": "🚀 Fast 8B Llama - Quick responses, good for general chat",
        "deepseek-ai/DeepSeek-R1-fast": "🧠 DeepSeek R1 - Advanced reasoning model, fast version",
        "Qwen/Qwen2.5-72B-Instruct-fast": "⚡ Qwen 72B - Large Chinese model, excellent multilingual support",
        "google/gemma-2-9b-it-fast": "🔬 Google Gemma 9B - Efficient Google model, fast inference",
        "mistralai/Mistral-Nemo-Instruct-2407": "🇫🇷 Mistral Nemo - European model, balanced performance"
    }
    
    model = st.selectbox(
        "Select Model",
        options=list(model_options.keys()),
        index=0,
        help="Choose the AI model for your conversation"
    )
    
    # Show model description
    st.caption(f"{model_options[model]}")
    
    # Advanced settings
    with st.expander("⚙️ Advanced Settings", expanded=False):
        max_tokens = st.slider(
            "Max Tokens",
            min_value=128,
            max_value=8192,
            value=4096,
            step=128,
            help="Maximum number of tokens to generate. Higher values allow longer responses but cost more."
        )
        
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1,
            help="Controls randomness in responses. Lower values (0.1-0.3) are more focused and deterministic, higher values (0.7-1.0) are more creative and varied."
        )

    st.divider()
    
    page = st.selectbox("Choose a tool", ["Chatbot", "Text Checker", "Recipe Creator"])

# Main content area
if not api_key:
    welcome_screen()
elif page == "Chatbot":
    chatbot_interface()
elif page == "Text Checker":
    text_checker_interface()
elif page == "Recipe Creator":
    recipe_creator_interface()
