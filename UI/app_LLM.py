import streamlit as st
from openai import OpenAI
client = OpenAI()

# ---------------- MEMORY ----------------
if "memory" not in st.session_state:
    st.session_state.memory = {
        "goal": "",
        "completed": [],
        "pending": [],
        "current_step": ""
    }

memory = st.session_state.memory

# ---------------- PLANNER ----------------


def planner(goal):
    prompt = f"""
    Break the following goal into 3-5 clear actionable steps.

    Goal: {goal}

    Return only steps as a numbered list.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    steps = response.choices[0].message.content.split("\n")

    # Clean steps
    steps = [s.strip("1234567890. ") for s in steps if s.strip()]
    return steps

# ---------------- EXECUTOR ----------------
def executor(step):
    prompt = f"""
    Explain how to complete this task step-by-step in simple terms:

    Task: {step}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ---------------- UI ----------------
st.title("🧠 Agentic AI Task Executor")

# Input goal
goal = st.text_input("Enter your goal:")

if st.button("Start Agent"):
    memory["goal"] = goal
    memory["pending"] = planner(goal)
    memory["completed"] = []
    memory["current_step"] = ""

# Show plan
if memory["pending"]:
    st.subheader("📋 Plan")
    for step in memory["pending"]:
        st.write("•", step)

# Run next step
if st.button("Run Next Step"):
    if memory["pending"]:
        step = memory["pending"].pop(0)
        memory["current_step"] = step

        st.subheader("👉 Current Step")
        st.write(step)

        result = executor(step)
        st.subheader("🤖 Suggestion")
        st.write(result)

# Completion buttons
if memory["current_step"]:
    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Mark as Completed"):
            memory["completed"].append(memory["current_step"])
            memory["current_step"] = ""

    with col2:
        if st.button("❌ Not Completed"):
            memory["pending"].append(memory["current_step"])
            memory["current_step"] = ""

# Status
st.subheader("📊 Progress")
st.write("✅ Completed:", memory["completed"])
st.write("⏳ Pending:", memory["pending"])

# Completion message
if not memory["pending"] and not memory["current_step"] and memory["goal"]:
    st.success("🎉 Goal Completed!")