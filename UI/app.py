import streamlit as st
import random

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
    if "linear regression" in goal.lower():
        return [
            "Understand concept of linear regression",
            "Learn mathematical formula",
            "Implement using Python"
        ]
    else:
        return [
            "Understand basics",
            "Practice examples",
            "Build mini project"
        ]

# ---------------- EXECUTOR ----------------
def executor(step):
    responses = {
        "Understand concept of linear regression":
            "Read about how a straight line fits data points.",
        "Learn mathematical formula":
            "Study equation: y = wx + b and gradient descent.",
        "Implement using Python":
            "Use sklearn LinearRegression on sample dataset."
    }
    return responses.get(step, "Follow tutorials and practice.")

# ---------------- UI ----------------
st.title("🧠 Agentic AI Task Executor (Dummy Version)")

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