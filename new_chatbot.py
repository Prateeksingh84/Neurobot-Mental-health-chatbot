import gradio as gr
from groq import Groq
import base64

# --- Setup: Groq API client ---
groq_api = Groq(api_key="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")

# --- Load background image as base64 ---
def get_base64(background_path):
    with open(background_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# --- Response Generator ---
def generate_response(user_input, history):
    history.append({"role": "user", "content": user_input})
    response = groq_api.chat.completions.create(
        model="llama3-70b-8192",
        messages=history,
        temperature=0.7,
        max_tokens=150,
        top_p=1
    )
    ai_response = response.choices[0].message.content.strip()
    history.append({"role": "assistant", "content": ai_response})

    chat_transcript = "\n\n".join(
        [f"**{'You' if m['role'] == 'user' else 'AI'}:** {m['content']}" for m in history]
    )
    return chat_transcript, history

# --- Affirmation Generator ---
def generate_affirmation():
    prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed."
    response = groq_api.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100,
        top_p=1
    )
    return response.choices[0].message.content.strip()

# --- Meditation Guide Generator ---
def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation script to help someone relax and reduce stress."
    response = groq_api.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=300,
        top_p=1
    )
    return response.choices[0].message.content.strip()

# --- Gradio Interface ---
def interface():
    background_b64 = get_base64("background.png")

    with gr.Blocks(css=f"""
    body {{
        background-image: url("data:image/png;base64,{background_b64}");
        background-size: cover;
        background-position: center;
        font-family: 'Segoe UI', sans-serif;
    }}
    .gr-button {{
        margin-top: 8px;
    }}
    """) as demo:

        gr.Markdown("""
        <div style="text-align:center;">
            <h1 style="margin-bottom: 0;">🧠 Mental Health Support Agent</h1>
            <p style="font-size: 16px; margin-top: 0;">Your AI companion for emotional wellbeing</p>
        </div>
        """)

        state = gr.State([])

        with gr.Row():
            with gr.Column(scale=2):
                chatbot = gr.Textbox(label="Conversation", lines=20, interactive=False, show_copy_button=True)
            with gr.Column(scale=1):
                output_affirmation = gr.Textbox(label="💬 Affirmation", lines=2)
                output_meditation = gr.Textbox(label="🧘 Guided Meditation", lines=5)

        user_input = gr.Textbox(label="How can I help you today?", placeholder="Ask something...", lines=2)

        with gr.Row():
            submit_btn = gr.Button("💌 Send Message", variant="primary")
            affirmation_btn = gr.Button("🌟 Get Affirmation")
            meditation_btn = gr.Button("🧘‍♀️ Get Meditation Guide")

        submit_btn.click(fn=generate_response, inputs=[user_input, state], outputs=[chatbot, state])
        affirmation_btn.click(fn=generate_affirmation, inputs=[], outputs=output_affirmation)
        meditation_btn.click(fn=generate_meditation_guide, inputs=[], outputs=output_meditation)

    demo.launch()

# --- Run App ---
if __name__ == "__main__":
    interface()
