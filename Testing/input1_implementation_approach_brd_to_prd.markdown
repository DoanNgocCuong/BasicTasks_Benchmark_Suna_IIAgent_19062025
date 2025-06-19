# 📘 Implementation Approach Template – Daily Talk Activity for Pika Robot

This template helps Learning Designers convert any **Daily Talk concept** into a complete, structured activity PRD. It ensures all activities align with **Pika’s personality** and educational goals for children aged 5–7.

---

## 🧠 0. Purpose of This File

This is a **step-by-step blueprint** for turning a raw Daily Talk idea into a complete, deployable PRD. It ensures consistent generation, QA, and deployment of engaging, meaningful, and educational activities.

> - **Input:** Concept idea (short description from Learning Designer)  
> - **Output:** Full PRD in Markdown, with `flow` YAML for engine generation

---

## 1. 🔍 Step-by-Step Agent Workflow

### 🔹 Step 1 – Interpret the Concept
- Read and understand the **activity name** and **description**
- Determine the **core emotional or developmental need** (e.g., curiosity, safety, connection)
- Define the **learning goal** (e.g., vocabulary exposure, confidence building)
- Check for the `include_english_vocab` field:
  - If `true`, weave 1–3 simple English chunks into the flow naturally
  - If `false` or absent, omit English instruction

### 🔹 Step 2 – Map to Technical Design

| Attribute          | How to Decide                                                                  |
|--------------------|--------------------------------------------------------------------------------|
| `structure_type`   | - Informative? → `Fixed`<br>- Follows rules? → `Rule-based`<br>- Depends on user input? → `Scenario` |
| `tone`             | Default is `playful` or `warm` unless topic suggests otherwise                 |
| `language_target`  | Select `vocab` or `phrases` based on the `include_english_vocab` input         |

---

## 2. 🧠 General Overview (PRD Metadata Template)

| Field               | Description                                               |
|--------------------|-----------------------------------------------------------|
| **Activity Name**   | Title of the activity (e.g., "Funny Fact Friday")        |
| **Type**            | Daily Talk (`Fixed`, `Scenario`, `Rule-based`)           |
| **Primary Goal**    | `Mood Uplift`, `Habit Formation`, or `Personalization`   |
| **Target Group**    | Children aged 5–7                                        |
| **User Input**      | Voice and/or Button interactions                         |
| **Include English?**| `true` if English vocab should be introduced             |

---

## 3. 🔁 Technical Learning Flow Mapping

| Phase                  | Purpose                                            | AI Agent Role                         | Output Type         |
|------------------------|----------------------------------------------------|----------------------------------------|----------------------|
| **Concept Selection**  | Match child needs to engaging topic                | Select topic and supporting content    | Selected Topic       |
| **Structuring Flow**   | Guide child interaction through 5-phase design     | Design interaction, embed English if needed | Prompt Sequence |
| **Tone & Voice**       | Keep tone warm and humorous                        | Use Pika’s voice quirks and humor      | Script Dialogue      |
| **Data Hook Design**   | Capture small profile details                      | Save preferences or responses          | User Profile Log     |
| **Emotion Handling**   | End with mood check for balance                    | Trigger emoji scale or physical CTA    | Mood Metric Feedback |

🔹 Note: Each response must have at most one clear call-to-action directed to the user. Prioritize clarity and avoid multiple requests/question within the same message.
---

## 4. 🧱 Implementation Blocks

### A. Input Required
- **Topic Tags:** Category (e.g., Emotions, Food)
- **Fact Set / Prompts:** Preloaded text, riddles, stories, etc.
- **Target Vocabulary (optional):** 1–3 simple English words or chunks (only used if `include_english_vocab = true`)
- **Optional Media:** Images or audio cues to support the story or fact
- **Include English?** Boolean flag (`true` or `false`)

---

### B. Flow Template (For AI Agents to Generate)

```yaml
concept: <Activity Name>
core_need: <curiosity / connection / fun>
structure_type: <Fixed / Rule-based / Scenario>
primary_outcome: <Mood Uplift / Habit / Personalization>
include_english_vocab: true/false
language_target: <vocab / phrases / none>
tone: <playful / warm / humorous>

flow:
  - phase: Greeting & Hook
    action: introduce_topic
    sample: "Hey hey! Want to hear something super silly about <topic>?"

  - phase: Activity Body
    repeat:
      - content: "<Insert fun fact, mini story, or silly riddle>"
        vocab: "<English word>" # Only if include_english_vocab = true
        action: 
          - prompt_user_with_action
          - expected_behavior: "repeat_after_pika / answer_simple_question / tell_a_short_story"
        hook: "<funny reaction or joke>"

  - phase: Recap
    action: summary_or_reflection
    prompt: "Which part did you like most?" 
    data_hook: save_user_response

  - phase: Call to Action
    task: "Wanna draw it or tell someone about it?"

  - phase: Mood Check
    action: show_emoji_buttons
    prompt: "Cậu cảm thấy thế nào sau hoạt động vừa rồi với Pika? Rất thích, bình thường hay không thích lắm? Hãy bấm nút tương ứng với biểu tượng trên màn hình nha."
    post_response_action: 
      - say_thank_you: "Cảm ơn cậu."
      - end_conversation: true
```

> ✅ *If `include_english_vocab = false`, the `vocab` and `repeat_word` actions should be skipped.*

---

## 5. 🧩 Learning Design Keywords Applied

| Keyword                   | Purpose & Impact                                                       |
|---------------------------|------------------------------------------------------------------------|
| **Affective Scaffolding** | Pika supports mood and confidence through voice, praise, and feedback |
| **Dialogue-Based Learning** | Children are prompted to **speak** in response to Pika                 |
| **English Chunking (optional)** | Simple English is inserted only when relevant and explicitly requested |
| **Playful Learning Loop**  | Structure: Hook → Activity → Response → CTA → Mood Check              |
| **Data Hook Engineering**  | Tag favorite topics and words for personalization                     |
| **Input-Output Mapping**   | Every prompt from Pika triggers a **verbal or emotional output** from the child |
